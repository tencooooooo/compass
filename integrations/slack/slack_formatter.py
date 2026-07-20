from __future__ import annotations

from collections import Counter
from datetime import datetime
import json
from pathlib import Path
from typing import Any


ARTIFACT_NAME = "compass-generated-outputs"


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def safe_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def fmt_value(value: Any, default: str = "N/A") -> str:
    return default if value in (None, "") else str(value)


def score_results_by_ticker(score_data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    results = safe_list(score_data.get("results"))
    return {str(item.get("ticker")).upper(): item for item in results if isinstance(item, dict) and item.get("ticker")}


def format_top_candidates(discovery_data: dict[str, Any], limit: int) -> tuple[int, list[str]]:
    candidates = safe_list(discovery_data.get("candidates"))
    lines = []
    for index, candidate in enumerate(candidates[:limit], start=1):
        ticker = fmt_value(candidate.get("ticker"))
        score = fmt_value(candidate.get("discovery_score"))
        confidence = fmt_value(candidate.get("confidence"))
        signal = fmt_value(candidate.get("signal_strength"))
        lines.append(f"{index}. {ticker} ({score}) - Confidence: {confidence} / Signal: {signal}")
    return len(candidates), lines or ["初回実行またはDiscovery候補なし"]


def format_score_changes(current_scores: dict[str, Any], previous_scores: dict[str, Any] | None) -> list[str]:
    if not previous_scores:
        return ["初回実行"]

    current = score_results_by_ticker(current_scores)
    previous = score_results_by_ticker(previous_scores)
    changes = []
    for ticker, current_item in sorted(current.items()):
        if ticker not in previous:
            continue
        current_score = current_item.get("total_score")
        previous_score = previous[ticker].get("total_score")
        if current_score is None or previous_score is None:
            continue
        diff = float(current_score) - float(previous_score)
        sign = "+" if diff >= 0 else ""
        changes.append(f"{ticker}: {previous_score} -> {current_score} ({sign}{diff:.0f})")
    return changes or ["前回比較データなし"]


def format_market_summary(market_data: dict[str, Any]) -> list[str]:
    sectors = safe_list(market_data.get("sectors"))
    lines = []
    for sector in sectors:
        trend = sector.get("trend", {}) if isinstance(sector, dict) else {}
        lines.append(
            f"{fmt_value(sector.get('sector'))}: "
            f"Momentum {fmt_value(trend.get('momentum'))}, "
            f"News {fmt_value(trend.get('news'))}, "
            f"Financial Health {fmt_value(trend.get('financial_health'))}"
        )
    return lines or ["Market Intelligence未生成"]


def format_important_news(market_data: dict[str, Any], news_dir: Path, limit: int) -> list[str]:
    events = safe_list(market_data.get("top_events"))
    titles = [event.get("title") for event in events if isinstance(event, dict) and event.get("title")]
    if not titles:
        news_items: list[dict[str, Any]] = []
        for path in news_dir.glob("*.json"):
            news_items.extend(item for item in safe_list(load_json(path, [])) if isinstance(item, dict))
        news_items.sort(key=lambda item: item.get("published_at") or "", reverse=True)
        titles = [item.get("title") for item in news_items if item.get("title")]
    return [f"- {title}" for title in titles[:limit]] or ["重要ニュースなし"]


def validation_counts(validation_rows: list[dict[str, Any]]) -> list[str]:
    if not validation_rows:
        return ["Validation未生成"]

    latest_date = max(str(row.get("validation_date") or "") for row in validation_rows)
    latest_rows = [row for row in validation_rows if str(row.get("validation_date") or "") == latest_date]
    counts = Counter(row.get("validation_result") for row in latest_rows)
    return [
        f"Excellent: {counts.get('Excellent', 0)}",
        f"Good: {counts.get('Good', 0)}",
        f"Neutral: {counts.get('Neutral', 0)}",
        f"Poor: {counts.get('Poor', 0)}",
    ]


def build_section(title: str, lines: list[str]) -> str:
    body = "\n".join(lines)
    return f"*{title}*\n{body}"


def build_success_text(project_root: Path, context: dict[str, str], config: dict[str, Any]) -> str:
    discovery_data = load_json(project_root / "reports" / "discovery" / "discovery_candidates.json", {})
    market_data = load_json(project_root / "reports" / "market" / "market_dashboard.json", {})
    current_scores = load_json(project_root / "reports" / "scoring" / "company_scores.json", {})
    previous_scores = load_json(project_root / "reports" / "scoring" / "company_scores_previous.json", None)
    validation_data = load_json(project_root / "reports" / "validation" / "validation_history.json", [])

    top_limit = int(config.get("top_candidates", 3))
    max_news = int(config.get("max_news", 5))
    candidate_count, top_candidates = format_top_candidates(discovery_data, top_limit)
    market = market_data.get("market", {}) if isinstance(market_data, dict) else {}
    ticker_count = market.get("ticker_count") or context.get("ticker_count") or "N/A"

    sections = [
        "🧭 *Compass Daily Research Report*",
        build_section(
            "実行結果",
            [
                f"実行日時: {context.get('timestamp')}",
                "処理結果: Success",
                f"対象銘柄数: {ticker_count}",
                f"GitHub Actions Run Number: {context.get('run_number', 'N/A')}",
            ],
        ),
        build_section(
            "Discovery Summary",
            [f"新しいDiscovery候補数: {candidate_count}", "Top Candidates", *top_candidates],
        ),
        build_section("Score Changes", format_score_changes(current_scores, previous_scores)),
        build_section("Market Summary", format_market_summary(market_data if isinstance(market_data, dict) else {})),
        build_section(
            "Important News",
            format_important_news(market_data if isinstance(market_data, dict) else {}, project_root / "storage" / "raw" / "news", max_news),
        ),
        build_section("Validation Summary", validation_counts(safe_list(validation_data))),
        build_section("Artifacts", [ARTIFACT_NAME]),
    ]
    return "\n\n".join(sections)


def build_failure_text(context: dict[str, str]) -> str:
    return "\n\n".join(
        [
            "❌ *Compass Workflow Failed*",
            build_section(
                "Failure",
                [
                    f"Step: {context.get('failed_step') or 'Unknown'}",
                    f"Error: {context.get('error') or 'See GitHub Actions logs for details.'}",
                    f"Timestamp: {context.get('timestamp')}",
                    f"GitHub Actions Run Number: {context.get('run_number', 'N/A')}",
                ],
            ),
        ]
    )


def build_payload(text: str) -> dict[str, Any]:
    return {
        "text": text,
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text[:3000],
                },
            }
        ],
    }


def current_timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")
