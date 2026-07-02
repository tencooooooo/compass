from __future__ import annotations

import re
from typing import Any

import pandas as pd

from utils.news_sentiment import sentiment_counts
from utils.price_data import trading_day_momentum
from utils.values import safe_float


def clamp(value: float, minimum: float = 0, maximum: float = 100) -> float:
    return max(minimum, min(maximum, value))


def momentum_for_days(prices: pd.DataFrame, days: int) -> float | None:
    return trading_day_momentum(prices, days)


def extract_section(markdown: str, start_heading: str, stop_headings: list[str]) -> str:
    start = markdown.find(start_heading)
    if start < 0:
        return ""
    content_start = start + len(start_heading)
    stop_positions = [markdown.find(stop, content_start) for stop in stop_headings]
    stop_positions = [pos for pos in stop_positions if pos >= 0]
    end = min(stop_positions) if stop_positions else len(markdown)
    return markdown[content_start:end].strip()


def first_bullets(section: str, limit: int = 3) -> list[str]:
    bullets: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped[2:])
        if len(bullets) >= limit:
            break
    return bullets


def extract_analysis_points(markdown: str) -> dict[str, list[str]]:
    strengths = extract_section(markdown, "### 強み", ["### 弱み", "### 今後の注目ポイント", "### リスク要因", "## 7."])
    watch = extract_section(markdown, "### 今後の注目ポイント", ["### リスク要因", "## 7."])
    risks = extract_section(markdown, "### リスク要因", ["## 7."])
    return {
        "strengths": first_bullets(strengths),
        "watch_points": first_bullets(watch),
        "risks": first_bullets(risks, limit=2),
    }


def news_signal(news_items: list[dict[str, Any]]) -> tuple[int, int]:
    counts = sentiment_counts(news_items)
    return counts["positive"], counts["negative"]


def event_reaction(events: list[dict[str, Any]]) -> dict[str, Any]:
    changes = [safe_float(event.get("price_change_percent")) for event in events]
    changes = [value for value in changes if value is not None]
    if not changes:
        return {"average": None, "count": len(events), "with_reaction": 0}
    return {
        "average": sum(changes) / len(changes),
        "count": len(events),
        "with_reaction": len(changes),
    }


def confidence_level(missing_count: int, scoring_confidence: str | None, market_available: bool) -> str:
    if missing_count == 0 and scoring_confidence == "High" and market_available:
        return "High"
    if missing_count <= 3 and scoring_confidence in {"High", "Medium"}:
        return "Medium"
    return "Low"


def sector_context(sector: str, market_dashboard: dict[str, Any]) -> dict[str, Any]:
    for sector_data in market_dashboard.get("sectors", []):
        if sector_data.get("sector") == sector:
            return sector_data
    return {}


def score_from_momentum(value: float | None, points: float, label: str, reasons: list[str], missing: list[str]) -> float:
    if value is None:
        missing.append(label)
        reasons.append(f"{label}モメンタムが計算できないため加点していません。")
        return 0
    if value >= 15:
        reasons.append(f"{label}モメンタムが {value:.2f}% と強く、市場関心が確認できます。")
        return points
    if value >= 0:
        reasons.append(f"{label}モメンタムが {value:.2f}% とプラス圏です。")
        return points * 0.65
    if value >= -10:
        reasons.append(f"{label}モメンタムは {value:.2f}% と弱めですが、大きな崩れではありません。")
        return points * 0.25
    reasons.append(f"{label}モメンタムは {value:.2f}% と弱く、候補評価では注意点です。")
    return 0


def build_candidate(
    ticker: str,
    company: dict[str, Any],
    financials: dict[str, Any],
    news_items: list[dict[str, Any]],
    events: list[dict[str, Any]],
    prices: pd.DataFrame,
    score_result: dict[str, Any],
    company_report: str,
    market_dashboard: dict[str, Any],
) -> dict[str, Any]:
    reasons: list[str] = []
    watch_points: list[str] = []
    evidence = {"Company", "Financials", "Prices", "News", "Events", "Scoring", "Market Intelligence", "Knowledge"}
    missing: list[str] = []

    score_parts = score_result.get("scores", {})
    scoring_total = safe_float(score_result.get("total_score")) or 0
    scoring_confidence = (score_result.get("confidence") or {}).get("level")
    discovery_score = 0.0

    growth_score = safe_float((score_parts.get("Growth") or {}).get("score"))
    financial_health_score = safe_float((score_parts.get("Financial Health") or {}).get("score"))
    valuation_score = safe_float((score_parts.get("Valuation") or {}).get("score"))
    news_score = safe_float((score_parts.get("News") or {}).get("score"))

    if growth_score is None:
        missing.append("Growth score")
    else:
        discovery_score += (growth_score / 20) * 15
        reasons.append(f"Scoring EngineのGrowthが {growth_score:.0f}/20 で、成長性の基礎条件が確認できます。")

    if financial_health_score is None:
        missing.append("Financial Health score")
    else:
        discovery_score += (financial_health_score / 20) * 12
        reasons.append(f"Financial Healthが {financial_health_score:.0f}/20 で、継続調査に必要な財務基盤を評価しています。")

    if valuation_score is not None:
        discovery_score += (valuation_score / 20) * 6
        if valuation_score < 8:
            watch_points.append("バリュエーション面のスコアが低く、期待先行や割高さの確認が必要です。")
    else:
        missing.append("Valuation score")

    if news_score is not None:
        discovery_score += (news_score / 20) * 6
        reasons.append(f"Newsスコアが {news_score:.0f}/20 で、材料の量と市場関心を候補評価に反映しています。")
    else:
        missing.append("News score")

    rnd = safe_float(financials.get("research_and_development"))
    fcf = safe_float(financials.get("free_cash_flow"))
    eps = safe_float(financials.get("eps") or company.get("eps"))
    revenue = safe_float(financials.get("total_revenue"))
    if revenue and revenue > 0:
        discovery_score += 2
        reasons.append("売上が取得でき、事業規模の確認ができます。")
    else:
        missing.append("total_revenue")
    if eps and eps > 0:
        discovery_score += 2
        reasons.append("EPSがプラスで、利益を伴う成長候補として確認できます。")
    else:
        missing.append("eps")
    if rnd and rnd > 0:
        discovery_score += 3
        reasons.append("研究開発費が確認でき、将来成長への投資シグナルがあります。")
    else:
        missing.append("research_and_development")
    if fcf and fcf > 0:
        discovery_score += 3
        reasons.append("FCFがプラスで、成長投資を支える現金創出力があります。")
    else:
        missing.append("free_cash_flow")

    momentum = {
        "1m": momentum_for_days(prices, 30),
        "3m": momentum_for_days(prices, 90),
        "6m": momentum_for_days(prices, 180),
        "1y": momentum_for_days(prices, 365),
    }
    discovery_score += score_from_momentum(momentum["1m"], 4, "1M", reasons, missing)
    discovery_score += score_from_momentum(momentum["3m"], 5, "3M", reasons, missing)
    discovery_score += score_from_momentum(momentum["6m"], 5, "6M", reasons, missing)
    discovery_score += score_from_momentum(momentum["1y"], 8, "1Y", reasons, missing)

    positive_news, watch_news = news_signal(news_items)
    if positive_news:
        discovery_score += min(4, positive_news * 0.75)
        reasons.append(f"ニュース内に好材料候補が {positive_news} 件あり、追加調査の入口になります。")
    if watch_news:
        watch_points.append(f"注意材料になり得るニュース表現が {watch_news} 件あります。")
    if len(news_items) >= 5:
        discovery_score += 2
        reasons.append("直近ニュースが一定数あり、市場関心を追跡しやすい状態です。")
    else:
        missing.append("recent_news")

    reaction = event_reaction(events)
    if reaction["with_reaction"]:
        if reaction["average"] and reaction["average"] > 0:
            discovery_score += 3
            reasons.append(f"イベント後の平均株価反応が {reaction['average']:.2f}% とプラスです。")
        else:
            discovery_score += 1
            watch_points.append("イベント後の平均株価反応は強くなく、材料への市場反応は確認が必要です。")
    elif events:
        discovery_score += 1
        watch_points.append("Event Databaseはありますが、株価反応が未取得のイベントが多い状態です。")
    else:
        missing.append("events")

    sector = company.get("sector") or "Unknown"
    sector_data = sector_context(sector, market_dashboard)
    market_available = bool(sector_data)
    if sector_data:
        trend = sector_data.get("trend", {})
        sector_avg_score = safe_float(sector_data.get("average_score"))
        if sector_avg_score and scoring_total >= sector_avg_score:
            discovery_score += 3
            reasons.append(f"{sector}内の平均スコア以上で、セクター内でも追加調査候補になり得ます。")
        if trend.get("news") == "High":
            discovery_score += 1
            reasons.append(f"{sector}はニュース量がHighで、市場関心が高いセクターです。")
        if trend.get("financial_health") == "Good":
            discovery_score += 2
            reasons.append(f"{sector}のFinancial Health傾向はGoodで、セクター文脈は比較的安定しています。")
        if trend.get("momentum") in {"Risk-Off", "Weak"}:
            watch_points.append(f"{sector}のセクターモメンタムは{trend.get('momentum')}で、短期環境は慎重に見る必要があります。")
    else:
        missing.append("sector_context")

    analysis_points = extract_analysis_points(company_report)
    strengths = analysis_points["strengths"]
    if strengths:
        reasons.append("企業分析レポートに強みが記録されており、定性面の確認材料があります。")
    watch_points.extend(analysis_points["watch_points"])
    watch_points.extend(analysis_points["risks"])

    if scoring_total >= 75:
        discovery_score += 2
        reasons.append("総合スコアが75点以上で、追加調査候補としての基礎点が高いです。")
    elif scoring_total >= 65:
        discovery_score += 1
        reasons.append("総合スコアが65点以上で、候補として確認する価値があります。")

    confidence = confidence_level(len(missing), scoring_confidence, market_available)
    discovery_score = int(round(clamp(discovery_score)))
    if discovery_score >= 75:
        status = "Primary Candidate"
    elif discovery_score >= 60:
        status = "Watch Candidate"
    else:
        status = "Not Selected"

    return {
        "ticker": ticker,
        "company": company.get("company_name") or ticker,
        "sector": sector,
        "industry": company.get("industry"),
        "discovery_score": discovery_score,
        "status": status,
        "discovery_reasons": reasons[:10],
        "strengths": strengths or ["企業分析レポートから明確な強みを抽出できませんでした。"],
        "watch_points": list(dict.fromkeys(watch_points))[:8] or ["現時点では主要なWatch Pointを抽出できませんでした。"],
        "confidence": confidence,
        "evidence": sorted(evidence),
        "missing_data": missing,
        "metrics": {
            "scoring_total": scoring_total,
            "growth_score": growth_score,
            "financial_health_score": financial_health_score,
            "valuation_score": valuation_score,
            "news_score": news_score,
            "momentum": momentum,
            "positive_news": positive_news,
            "watch_news": watch_news,
            "event_count": reaction["count"],
            "events_with_reaction": reaction["with_reaction"],
            "sector_average_score": sector_data.get("average_score"),
        },
    }


def select_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected = [candidate for candidate in candidates if candidate["status"] != "Not Selected"]
    if selected:
        return sorted(selected, key=lambda item: item["discovery_score"], reverse=True)
    return sorted(candidates, key=lambda item: item["discovery_score"], reverse=True)[:3]
