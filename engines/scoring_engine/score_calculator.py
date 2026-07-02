from __future__ import annotations

from typing import Any

import pandas as pd

from utils.news_sentiment import sentiment_counts
from utils.price_data import trading_day_momentum


GROWTH_THRESHOLDS = {
    "excellent": 30.0,
    "good": 15.0,
    "positive": 0.0,
}

VALUATION_RULES = [
    ("trailing_pe", "PER", 5, [(0, 25, 5), (25, 40, 3), (40, 70, 1)]),
    ("forward_pe", "Forward PER", 5, [(0, 25, 5), (25, 40, 3), (40, 70, 1)]),
    ("peg_ratio", "PEG", 5, [(0, 1, 5), (1, 2, 3), (2, 4, 1)]),
    ("price_to_book", "PBR", 5, [(0, 8, 5), (8, 20, 3), (20, 50, 1)]),
]


def safe_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return None if pd.isna(number) else number


def clamp(value: float, minimum: float = 0, maximum: float = 20) -> float:
    return max(minimum, min(maximum, value))


def rounded_score(value: float) -> int:
    return int(round(clamp(value)))


def is_present(value: Any) -> bool:
    return safe_float(value) is not None if isinstance(value, (int, float, str)) else value not in (None, "", [], {})


def score_positive_number(value: Any, points: float, label: str, reasons: list[str], missing: list[str]) -> float:
    number = safe_float(value)
    if number is None:
        missing.append(label)
        reasons.append(f"{label} が取得できないため、この項目は加点していません。")
        return 0
    if number > 0:
        reasons.append(f"{label} がプラスで確認できるため加点しています。")
        return points
    reasons.append(f"{label} がプラスではないため、加点を抑えています。")
    return 0


def momentum_for_days(prices: pd.DataFrame, days: int) -> float | None:
    return trading_day_momentum(prices, days)


def score_return(change_percent: float | None, label: str, reasons: list[str], missing: list[str]) -> float:
    if change_percent is None:
        missing.append(label)
        reasons.append(f"{label} の騰落率が計算できないため加点していません。")
        return 0
    if change_percent >= 15:
        reasons.append(f"{label} が {change_percent:.2f}% と強い上昇を示しています。")
        return 3
    if change_percent >= 0:
        reasons.append(f"{label} が {change_percent:.2f}% とプラス圏です。")
        return 2
    if change_percent >= -10:
        reasons.append(f"{label} は {change_percent:.2f}% と小幅なマイナスです。")
        return 1
    reasons.append(f"{label} は {change_percent:.2f}% と大きめの下落です。")
    return 0


def classify_news(news_items: list[dict[str, Any]]) -> tuple[int, int]:
    counts = sentiment_counts(news_items)
    return counts["positive"], counts["negative"]


def yoy_growth(latest: Any, prior: Any) -> float | None:
    latest_value = safe_float(latest)
    prior_value = safe_float(prior)
    if latest_value is None or prior_value in (None, 0):
        return None
    return round((latest_value - prior_value) / abs(prior_value) * 100, 2)


def score_growth_rate(value: float | None, label: str, points: float, reasons: list[str], missing: list[str]) -> float:
    if value is None:
        missing.append(label)
        reasons.append(f"{label} が計算できないため、成長率項目は加点していません。")
        return 0
    if value >= GROWTH_THRESHOLDS["excellent"]:
        reasons.append(f"{label} は {value:.2f}% で、+{GROWTH_THRESHOLDS['excellent']:.0f}%以上の高成長です。")
        return points
    if value >= GROWTH_THRESHOLDS["good"]:
        reasons.append(f"{label} は {value:.2f}% で、+{GROWTH_THRESHOLDS['good']:.0f}%以上の成長です。")
        return points * 0.65
    if value >= GROWTH_THRESHOLDS["positive"]:
        reasons.append(f"{label} は {value:.2f}% で、プラス成長を維持しています。")
        return points * 0.35
    reasons.append(f"{label} は {value:.2f}% で、前年同期比ではマイナスです。")
    return 0


def latest_and_prior_year_quarter(financials: dict[str, Any], key: str) -> tuple[Any, Any]:
    rows = financials.get("quarterly_financials")
    if not isinstance(rows, list) or len(rows) < 5:
        return None, None
    latest = rows[0] if isinstance(rows[0], dict) else {}
    prior = rows[4] if isinstance(rows[4], dict) else {}
    return latest.get(key), prior.get(key)


def calculate_growth_fallback(financials: dict[str, Any], extra_missing: list[str] | None = None) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    revenue = safe_float(financials.get("total_revenue"))
    if revenue is None:
        missing.append("total_revenue")
        reasons.append("売上データが取得できないため、売上項目は加点していません。")
    elif revenue >= 100_000_000_000:
        score += 5
        reasons.append("売上規模が大きく、事業規模の強さが確認できます。")
    elif revenue > 0:
        score += 3
        reasons.append("売上がプラスで確認できます。")
    else:
        reasons.append("売上がプラスではないため、売上項目の加点を抑えています。")

    score += score_positive_number(financials.get("eps"), 5, "EPS", reasons, missing)
    score += score_positive_number(financials.get("net_income"), 4, "純利益", reasons, missing)
    score += score_positive_number(financials.get("operating_income"), 2, "営業利益", reasons, missing)

    rnd = safe_float(financials.get("research_and_development"))
    if rnd is None:
        missing.append("research_and_development")
        reasons.append("研究開発費が取得できないため、R&D項目は加点していません。")
    elif rnd > 0:
        score += 4
        reasons.append("研究開発費が確認でき、将来成長への投資が続いています。")
    else:
        reasons.append("研究開発費が確認できないため、R&D項目の加点を抑えています。")

    for label in extra_missing or []:
        if label not in missing:
            missing.append(label)
    reasons.append("四半期時系列が不足しているため、Growthは最新値中心の従来ロジックへフォールバックしています。")
    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Financials", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "total_revenue": financials.get("total_revenue"),
            "eps": financials.get("eps"),
            "net_income": financials.get("net_income"),
            "operating_income": financials.get("operating_income"),
            "research_and_development": financials.get("research_and_development"),
            "revenue_yoy_growth": None,
            "eps_yoy_growth": None,
        },
    }


def calculate_growth(financials: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    revenue_latest, revenue_prior = latest_and_prior_year_quarter(financials, "total_revenue")
    eps_latest, eps_prior = latest_and_prior_year_quarter(financials, "eps")
    revenue_growth = yoy_growth(revenue_latest, revenue_prior)
    eps_growth = yoy_growth(eps_latest, eps_prior)
    if revenue_growth is None and eps_growth is None:
        return calculate_growth_fallback(financials, ["revenue_growth"])

    score += score_growth_rate(revenue_growth, "revenue_growth", 5, reasons, missing)
    score += score_growth_rate(eps_growth, "eps_growth", 5, reasons, missing)
    score += score_positive_number(financials.get("net_income"), 3, "純利益", reasons, missing)
    score += score_positive_number(financials.get("operating_income"), 2, "営業利益", reasons, missing)

    rnd = safe_float(financials.get("research_and_development"))
    if rnd is None:
        missing.append("research_and_development")
        reasons.append("研究開発費が取得できないため、R&D項目は加点していません。")
    elif rnd > 0:
        score += 4
        reasons.append("研究開発費が確認でき、将来成長への投資が続いています。")
    else:
        reasons.append("研究開発費が確認できないため、R&D項目の加点を抑えています。")

    revenue = safe_float(financials.get("total_revenue"))
    if revenue is None:
        missing.append("total_revenue")
        reasons.append("売上規模データが取得できないため、規模項目は加点していません。")
    elif revenue >= 100_000_000_000:
        score += 3
        reasons.append("売上規模が大きく、事業規模の強さが確認できます。")
    elif revenue > 0:
        score += 1.5
        reasons.append("売上がプラスで確認できます。")

    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Financials", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "total_revenue": financials.get("total_revenue"),
            "eps": financials.get("eps"),
            "net_income": financials.get("net_income"),
            "operating_income": financials.get("operating_income"),
            "research_and_development": financials.get("research_and_development"),
            "revenue_yoy_growth": revenue_growth,
            "eps_yoy_growth": eps_growth,
        },
    }


def calculate_financial_health(financials: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    score += score_positive_number(financials.get("cash"), 4, "現金", reasons, missing)

    liabilities = safe_float(financials.get("total_liabilities"))
    equity = safe_float(financials.get("shareholders_equity"))
    debt = safe_float(financials.get("long_term_debt"))

    if equity is None:
        missing.append("shareholders_equity")
        reasons.append("自己資本が取得できないため、自己資本項目は加点していません。")
    elif equity > 0:
        score += 5
        reasons.append("自己資本がプラスで、財務基盤を確認できます。")
    else:
        reasons.append("自己資本がプラスではないため、財務健全性の加点を抑えています。")

    if liabilities is None:
        missing.append("total_liabilities")
        reasons.append("総負債が取得できないため、負債項目は加点していません。")
    elif equity and equity > 0:
        debt_to_equity = liabilities / equity
        if debt_to_equity <= 1:
            score += 5
            reasons.append(f"総負債/自己資本が {debt_to_equity:.2f} 倍で、負債負担は相対的に抑えられています。")
        elif debt_to_equity <= 2:
            score += 3
            reasons.append(f"総負債/自己資本が {debt_to_equity:.2f} 倍で、負債負担は中程度です。")
        else:
            score += 1
            reasons.append(f"総負債/自己資本が {debt_to_equity:.2f} 倍で、負債負担の確認が必要です。")
    elif liabilities >= 0:
        score += 2
        reasons.append("総負債は取得できていますが、自己資本との比較が不十分です。")

    if debt is None:
        missing.append("long_term_debt")
        reasons.append("長期債務が取得できないため、債務構成の確認が必要です。")
    elif debt == 0:
        score += 2
        reasons.append("長期債務が0として取得されており、債務負担は限定的です。")
    elif liabilities and liabilities > 0 and debt / liabilities <= 0.5:
        score += 2
        reasons.append("長期債務が総負債に対して過度に大きくないため加点しています。")
    else:
        score += 1
        reasons.append("長期債務が確認できるため、返済負担の継続確認が必要です。")

    current_ratio = safe_float(financials.get("current_ratio"))
    if current_ratio is None:
        missing.append("current_ratio")
        reasons.append("Current Ratio が取得できないため、短期支払余力は評価を控えています。")
    elif current_ratio >= 1.5:
        score += 4
        reasons.append(f"Current Ratio が {current_ratio:.2f} で、短期支払余力が確認できます。")
    elif current_ratio >= 1:
        score += 2
        reasons.append(f"Current Ratio が {current_ratio:.2f} で、最低限の短期支払余力があります。")
    else:
        reasons.append(f"Current Ratio が {current_ratio:.2f} で、短期支払余力は追加確認が必要です。")

    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Financials", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "cash": financials.get("cash"),
            "total_liabilities": financials.get("total_liabilities"),
            "shareholders_equity": financials.get("shareholders_equity"),
            "long_term_debt": financials.get("long_term_debt"),
            "current_ratio": financials.get("current_ratio"),
        },
    }


def fixed_valuation_points(value: float, bands: list[tuple[int, int, int]]) -> int:
    for lower, upper, band_points in bands:
        if lower < value <= upper:
            return band_points
    return 0


def percentile_rank_lower_is_better(value: float, values: list[float]) -> float | None:
    clean_values = sorted(item for item in values if item > 0)
    if len(clean_values) < 2:
        return None
    lower_count = sum(1 for item in clean_values if item < value)
    equal_count = sum(1 for item in clean_values if item == value)
    percentile = (lower_count + (equal_count - 1) / 2) / (len(clean_values) - 1) * 100
    return round(max(0, min(100, percentile)), 2)


def calculate_valuation(company: dict[str, Any], sector_companies: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    sector_peers = sector_companies or []
    use_sector_relative = len(sector_peers) >= 5
    percentile_metrics: dict[str, Any] = {}

    for key, label, points, bands in VALUATION_RULES:
        value = safe_float(company.get(key))
        if value is None:
            missing.append(key)
            reasons.append(f"{label} が取得できないため加点していません。")
            continue

        if use_sector_relative:
            peer_values = [number for peer in sector_peers if (number := safe_float(peer.get(key))) is not None and number > 0]
            percentile = percentile_rank_lower_is_better(value, peer_values)
            if percentile is None or len(peer_values) < 5:
                awarded = fixed_valuation_points(value, bands)
                reasons.append(f"{label} はセクター内有効データが {len(peer_values)} 件のため、固定閾値へフォールバックしています。")
            elif percentile <= 25:
                awarded = points
                reasons.append(f"{label} はセクター内 {percentile:.2f} パーセンタイル / 母数 {len(peer_values)} で、相対的に割安寄りです。")
            elif percentile <= 75:
                awarded = 3
                reasons.append(f"{label} はセクター内 {percentile:.2f} パーセンタイル / 母数 {len(peer_values)} で、中位レンジです。")
            else:
                awarded = 0
                reasons.append(f"{label} はセクター内 {percentile:.2f} パーセンタイル / 母数 {len(peer_values)} で、相対的な加点は抑えています。")
            percentile_metrics[f"{key}_percentile"] = percentile
            percentile_metrics[f"{key}_peer_count"] = len(peer_values)
        else:
            awarded = fixed_valuation_points(value, bands)
            reasons.append(f"セクター比較対象が {len(sector_peers)} 社のため、{label} は固定閾値で評価しています。")

        score += min(points, awarded)
        if not use_sector_relative or percentile_metrics.get(f"{key}_percentile") is None:
            if awarded >= 4:
                reasons.append(f"{label} は {value:.2f} で、評価ルール上は過度な割高さが抑えられています。")
            elif awarded > 0:
                reasons.append(f"{label} は {value:.2f} で、バリュエーション面は中立から注意寄りです。")
            else:
                reasons.append(f"{label} は {value:.2f} で、バリュエーション面の加点は抑えています。")

    reasons.append("バリュエーションは割安判断ではなく、追加調査のための相対評価です。")
    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Company", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "trailing_pe": company.get("trailing_pe"),
            "forward_pe": company.get("forward_pe"),
            "peg_ratio": company.get("peg_ratio"),
            "price_to_book": company.get("price_to_book"),
            "sector_peer_count": len(sector_peers),
            **percentile_metrics,
        },
    }


def calculate_momentum(prices: pd.DataFrame) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    if prices.empty:
        return {
            "score": 0,
            "max_score": 20,
            "reasons": ["価格CSVが取得できないため、Momentumは評価していません。"],
            "evidence": ["Prices", "Knowledge"],
            "missing_data": ["prices"],
            "metrics": {},
        }

    prices = prices.sort_values("date").reset_index(drop=True)
    returns = {
        "1M": momentum_for_days(prices, 30),
        "3M": momentum_for_days(prices, 90),
        "6M": momentum_for_days(prices, 180),
        "1Y": momentum_for_days(prices, 365),
    }
    for label, value in returns.items():
        score += score_return(value, label, reasons, missing)

    latest_volume = safe_float(prices.iloc[-1].get("volume"))
    average_volume = safe_float(prices.tail(30)["volume"].mean())
    if latest_volume is None or average_volume in (None, 0):
        missing.append("volume")
        reasons.append("出来高データが不足しているため、Volume項目は加点していません。")
    else:
        volume_ratio = latest_volume / average_volume
        if volume_ratio >= 1.2:
            score += 4
            reasons.append(f"直近出来高が30日平均の {volume_ratio:.2f} 倍で、市場関心の高まりが確認できます。")
        elif volume_ratio >= 0.8:
            score += 3
            reasons.append(f"直近出来高が30日平均の {volume_ratio:.2f} 倍で、通常水準の流動性があります。")
        else:
            score += 1
            reasons.append(f"直近出来高が30日平均の {volume_ratio:.2f} 倍で、市場関心はやや弱めです。")

    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Prices", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            **returns,
            "latest_volume": latest_volume,
            "average_volume_30d": average_volume,
        },
    }


def calculate_news(news_items: list[dict[str, Any]], events: list[dict[str, Any]]) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    if not news_items:
        missing.append("news")
        reasons.append("ニュースが取得できないため、News項目は評価を控えています。")
    else:
        positive, negative = classify_news(news_items)
        coverage_points = min(6, len(news_items) / 20 * 6)
        score += coverage_points
        reasons.append(f"ニュース件数は {len(news_items)} 件で、情報量に応じて {coverage_points:.1f} 点を加点しています。")

        sentiment_score = max(0, min(8, 4 + positive - negative))
        score += sentiment_score
        reasons.append(f"ニュース見出し・要約の簡易分類では、好材料 {positive} 件、悪材料 {negative} 件です。")

    event_changes = [safe_float(event.get("price_change_percent")) for event in events]
    event_changes = [value for value in event_changes if value is not None]
    if not events:
        missing.append("events")
        reasons.append("イベントDBが取得できないため、イベント項目は加点していません。")
    elif not event_changes:
        missing.append("event_price_reaction")
        score += 2
        reasons.append("イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。")
    else:
        average_reaction = sum(event_changes) / len(event_changes)
        if average_reaction > 1:
            score += 6
            reasons.append(f"イベント後の平均株価反応が {average_reaction:.2f}% とプラスです。")
        elif average_reaction >= -1:
            score += 4
            reasons.append(f"イベント後の平均株価反応が {average_reaction:.2f}% と中立圏です。")
        else:
            score += 1
            reasons.append(f"イベント後の平均株価反応が {average_reaction:.2f}% と弱く、注意が必要です。")

    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["News", "Events", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "news_count": len(news_items),
            "event_count": len(events),
            "events_with_price_reaction": len(event_changes),
        },
    }


def confidence_from_missing(parts: dict[str, dict[str, Any]], prices: pd.DataFrame, news_items: list[dict[str, Any]]) -> dict[str, Any]:
    total_missing = sum(len(part.get("missing_data", [])) for part in parts.values())
    missing_labels = {label for part in parts.values() for label in part.get("missing_data", [])}
    available_sections = 0
    if not prices.empty and len(prices) >= 120:
        available_sections += 1
    if parts["Growth"]["score"] > 0:
        available_sections += 1
    if parts["Financial Health"]["score"] > 0:
        available_sections += 1
    if parts["Valuation"]["score"] > 0:
        available_sections += 1
    if len(news_items) >= 5:
        available_sections += 1

    completeness = (available_sections / 5) * 100 - min(35, total_missing * 5)
    has_event_reaction_gap = "event_price_reaction" in missing_labels
    if completeness >= 85 and total_missing == 0 and not has_event_reaction_gap:
        level = "High"
    elif completeness >= 50:
        level = "Medium"
    else:
        level = "Low"

    reasons = [
        f"利用可能な主要データ領域は5領域中 {available_sections} 領域です。",
        f"欠損または計算不可の項目数は {total_missing} 件です。",
    ]
    if level == "Low":
        reasons.append("欠損が多いため、スコアは参考度を下げて扱う必要があります。")
    elif level == "Medium":
        reasons.append("主要データは一定程度ありますが、欠損や未取得項目が残っています。")
    else:
        reasons.append("主要データが比較的そろっており、説明可能性は高めです。")
    if has_event_reaction_gap:
        reasons.append("イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。")

    return {
        "level": level,
        "completeness_score": round(max(0, min(100, completeness)), 2),
        "reasons": reasons,
    }


def calculate_company_score(
    ticker: str,
    company: dict[str, Any],
    financials: dict[str, Any],
    news_items: list[dict[str, Any]],
    events: list[dict[str, Any]],
    prices: pd.DataFrame,
    sector_companies: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    parts = {
        "Growth": calculate_growth(financials),
        "Financial Health": calculate_financial_health(financials),
        "Valuation": calculate_valuation(company, sector_companies),
        "Momentum": calculate_momentum(prices),
        "News": calculate_news(news_items, events),
    }
    total_score = sum(part["score"] for part in parts.values())
    confidence = confidence_from_missing(parts, prices, news_items)
    evidence_sources = sorted({source for part in parts.values() for source in part["evidence"]})

    return {
        "ticker": ticker,
        "company_name": company.get("company_name"),
        "total_score": total_score,
        "max_score": 100,
        "confidence": confidence,
        "scores": parts,
        "evidence_sources": evidence_sources,
    }
