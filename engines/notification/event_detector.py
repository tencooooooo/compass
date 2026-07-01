from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
from typing import Any


IMPORTANT_NEWS_KEYWORDS = {
    "M&A": ["acquire", "acquisition", "merger", "buyout", "takeover", "買収", "合併"],
    "決算": ["earnings", "revenue", "eps", "guidance", "quarter", "決算", "売上", "利益"],
    "CEO交代": ["ceo", "cfo", "resign", "steps down", "appointed", "交代", "辞任"],
    "大型契約": ["contract", "deal", "partnership", "agreement", "cloud", "government", "契約"],
    "新製品": ["launch", "unveil", "new product", "platform", "chip", "service", "発表", "新製品"],
    "配当": ["dividend", "増配", "減配", "配当"],
    "自社株買い": ["buyback", "repurchase", "自社株買い"],
    "規制": ["regulation", "probe", "antitrust", "export", "ban", "規制", "調査"],
    "訴訟": ["lawsuit", "settlement", "court", "patent", "訴訟", "和解"],
    "設備投資": ["factory", "data center", "capex", "facility", "investment", "設備投資"],
}


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def safe_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def safe_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def event_id(*parts: Any) -> str:
    raw = "|".join(str(part) for part in parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:20]


def base_event(event_type: str, priority: str, title: str, summary: str, **extra: Any) -> dict[str, Any]:
    return {
        "event_type": event_type,
        "priority": priority,
        "title": title,
        "summary": summary,
        "detected_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        **extra,
    }


def detect_discovery_alerts(project_root: Path, rules: dict[str, Any]) -> list[dict[str, Any]]:
    threshold = safe_float(rules.get("discovery_score")) or 90
    data = load_json(project_root / "reports" / "discovery" / "discovery_candidates.json", {})
    events: list[dict[str, Any]] = []
    for candidate in safe_list(data.get("candidates")):
        score = safe_float(candidate.get("discovery_score"))
        if score is None or score < threshold:
            continue
        ticker = candidate.get("ticker")
        event = base_event(
            event_type="discovery_alert",
            priority="High",
            title="Discovery Alert",
            summary=f"High Potential Company Detected: {ticker}",
            emoji="🧭",
            ticker=ticker,
            details=[
                f"Score: {score:.0f}",
                f"Confidence: {candidate.get('confidence') or 'N/A'}",
                "Reason:",
                *safe_list(candidate.get("discovery_reasons"))[:3],
            ],
            evidence=["Discovery", "Scoring", "Market Intelligence", "Knowledge"],
        )
        event["event_id"] = event_id(event["event_type"], ticker, int(score), data.get("generated_at"))
        events.append(event)
    return events


def current_score_snapshot(project_root: Path) -> dict[str, Any]:
    data = load_json(project_root / "reports" / "scoring" / "company_scores.json", {})
    snapshot: dict[str, Any] = {}
    for item in safe_list(data.get("results")):
        ticker = str(item.get("ticker") or "").upper()
        if ticker:
            snapshot[ticker] = item.get("total_score")
    return snapshot


def detect_score_change_alerts(project_root: Path, rules: dict[str, Any], previous_scores: dict[str, Any]) -> list[dict[str, Any]]:
    threshold = safe_float(rules.get("score_change")) or 5
    current_scores = current_score_snapshot(project_root)
    events: list[dict[str, Any]] = []
    for ticker, current_score in current_scores.items():
        previous_score = safe_float(previous_scores.get(ticker))
        current_value = safe_float(current_score)
        if previous_score is None or current_value is None:
            continue
        diff = current_value - previous_score
        if abs(diff) < threshold:
            continue
        arrow = "↑" if diff > 0 else "↓"
        sign = "+" if diff > 0 else ""
        event = base_event(
            event_type="score_change_alert",
            priority="Medium" if abs(diff) < 10 else "High",
            title="Score Change Alert",
            summary=f"{ticker}: {previous_score:.0f} {arrow} {current_value:.0f} ({sign}{diff:.0f})",
            emoji="📊",
            ticker=ticker,
            details=[
                f"Previous Score: {previous_score:.0f}",
                f"Current Score: {current_value:.0f}",
                f"Change: {sign}{diff:.0f}",
            ],
            evidence=["Scoring", "Knowledge"],
        )
        event["event_id"] = event_id(event["event_type"], ticker, previous_score, current_value)
        events.append(event)
    return events


def current_market_snapshot(project_root: Path) -> dict[str, Any]:
    data = load_json(project_root / "reports" / "market" / "market_dashboard.json", {})
    snapshot: dict[str, Any] = {}
    for sector in safe_list(data.get("sectors")):
        trend = sector.get("trend", {}) if isinstance(sector, dict) else {}
        name = sector.get("sector")
        if name:
            snapshot[name] = {
                "momentum": trend.get("momentum"),
                "news": trend.get("news"),
                "financial_health": trend.get("financial_health"),
            }
    return snapshot


def detect_market_trend_alerts(project_root: Path, rules: dict[str, Any], previous_market: dict[str, Any]) -> list[dict[str, Any]]:
    if not rules.get("market_change", True):
        return []
    current_market = current_market_snapshot(project_root)
    events: list[dict[str, Any]] = []
    for sector, current_trend in current_market.items():
        previous_trend = previous_market.get(sector)
        if not isinstance(previous_trend, dict) or previous_trend == current_trend:
            continue
        changed = [
            f"{key}: {previous_trend.get(key) or 'N/A'} -> {current_trend.get(key) or 'N/A'}"
            for key in ["momentum", "news", "financial_health"]
            if previous_trend.get(key) != current_trend.get(key)
        ]
        event = base_event(
            event_type="market_trend_alert",
            priority="Medium",
            title="Market Trend Alert",
            summary=f"{sector} trend changed.",
            emoji="📈",
            details=changed,
            evidence=["Market Intelligence", "Knowledge"],
        )
        event["event_id"] = event_id(event["event_type"], sector, json.dumps(current_trend, sort_keys=True))
        events.append(event)
    return events


def classify_news(item: dict[str, Any]) -> list[str]:
    text = f"{item.get('title') or ''} {item.get('summary') or ''}".lower()
    categories = []
    for category, keywords in IMPORTANT_NEWS_KEYWORDS.items():
        if any(keyword.lower() in text for keyword in keywords):
            categories.append(category)
    return categories


def detect_important_news_alerts(project_root: Path, rules: dict[str, Any], max_news: int) -> list[dict[str, Any]]:
    if not rules.get("important_news", True):
        return []
    news_dir = project_root / "storage" / "raw" / "news"
    news_items: list[dict[str, Any]] = []
    for path in news_dir.glob("*.json"):
        news_items.extend(item for item in safe_list(load_json(path, [])) if isinstance(item, dict))
    news_items.sort(key=lambda item: item.get("published_at") or "", reverse=True)

    events: list[dict[str, Any]] = []
    for item in news_items:
        categories = classify_news(item)
        if not categories:
            continue
        ticker = item.get("ticker")
        event = base_event(
            event_type="important_news_alert",
            priority="Medium",
            title="Important News Alert",
            summary=str(item.get("title") or "Untitled news"),
            emoji="📰",
            ticker=ticker,
            details=[
                f"Category: {', '.join(categories)}",
                f"Published: {item.get('published_at') or 'N/A'}",
                f"Publisher: {item.get('publisher') or item.get('source') or 'N/A'}",
            ],
            evidence=["News", "Knowledge: news_analysis_rules.md"],
            url=item.get("url"),
        )
        event["event_id"] = event_id(event["event_type"], ticker, item.get("published_at"), item.get("title"))
        events.append(event)
        if len(events) >= max_news:
            break
    return events


def detect_validation_alerts(project_root: Path, rules: dict[str, Any]) -> list[dict[str, Any]]:
    target_result = str(rules.get("validation", "Excellent"))
    data = load_json(project_root / "reports" / "validation" / "validation_history.json", [])
    events: list[dict[str, Any]] = []
    for row in safe_list(data):
        if row.get("validation_result") != target_result:
            continue
        ticker = row.get("ticker")
        return_percent = safe_float(row.get("return_percent"))
        return_text = "N/A" if return_percent is None else f"{return_percent:+.2f}%"
        event = base_event(
            event_type="validation_alert",
            priority="High",
            title="Validation Alert",
            summary=f"Discovery Candidate -> {target_result}: {ticker}",
            emoji="✅",
            ticker=ticker,
            details=[
                f"Period: {row.get('period') or 'N/A'}",
                f"Return: {return_text}",
                f"Discovery Score: {row.get('discovery_score') or 'N/A'}",
                f"Confidence: {row.get('confidence') or 'N/A'}",
            ],
            evidence=["Validation", "Prices", "Discovery", "Knowledge"],
        )
        event["event_id"] = event_id(event["event_type"], ticker, row.get("period"), row.get("discovery_date"), target_result)
        events.append(event)
    return events


def workflow_failure_event(status: str, run_number: str, failed_step: str, error: str) -> dict[str, Any]:
    event = base_event(
        event_type="workflow_failure",
        priority="Emergency",
        title="Compass Workflow Failed",
        summary=f"Workflow status: {status}",
        emoji="❌",
        details=[
            f"Step: {failed_step or 'Unknown'}",
            f"Error: {error or 'See GitHub Actions logs for details.'}",
            f"GitHub Actions Run Number: {run_number or 'N/A'}",
        ],
        evidence=["GitHub Actions"],
    )
    event["event_id"] = event_id(event["event_type"], run_number, status, failed_step)
    return event


def detect_events(
    project_root: Path,
    rules: dict[str, Any],
    previous_scores: dict[str, Any],
    previous_market: dict[str, Any],
    max_news: int,
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    events.extend(detect_discovery_alerts(project_root, rules))
    events.extend(detect_score_change_alerts(project_root, rules, previous_scores))
    events.extend(detect_market_trend_alerts(project_root, rules, previous_market))
    events.extend(detect_important_news_alerts(project_root, rules, max_news))
    events.extend(detect_validation_alerts(project_root, rules))
    return events
