from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
from typing import Any

from core.feedback.improvement_detector import (
    SUCCESS_RESULTS,
    aggregate_reason_categories,
    detect_improvement_candidates,
    group_rows,
    pct,
    result_counts,
    score_buckets,
)


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def safe_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def load_collection(directory: Path) -> dict[str, Any]:
    if not directory.exists():
        return {}
    return {path.stem: load_json(path, {}) for path in sorted(directory.glob("*.json"))}


def scoring_by_ticker(project_root: Path) -> dict[str, dict[str, Any]]:
    data = load_json(project_root / "reports" / "scoring" / "company_scores.json", {})
    return {
        str(item.get("ticker")).upper(): item
        for item in safe_list(data.get("results"))
        if isinstance(item, dict) and item.get("ticker")
    }


def validation_rows(project_root: Path) -> list[dict[str, Any]]:
    report_rows = load_json(project_root / "reports" / "validation" / "validation_history.json", [])
    if report_rows:
        return safe_list(report_rows)

    rows: list[dict[str, Any]] = []
    for item in load_collection(project_root / "memory" / "validations").values():
        rows.extend(safe_list(item.get("rows")))
    return rows


def confidence_accuracy(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped = group_rows(rows, "confidence")
    expected_order = {"High": 0, "Medium": 1, "Low": 2, "Unknown": 3}
    return sorted(grouped, key=lambda item: expected_order.get(item.get("confidence"), 9))


def event_accuracy(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets = {"Has Events": [], "No Events": []}
    for row in rows:
        if int(row.get("event_count") or 0) > 0:
            buckets["Has Events"].append(row)
        else:
            buckets["No Events"].append(row)
    return [
        {
            "event_bucket": name,
            "total_count": len(group),
            "completed_count": len([row for row in group if row.get("period_complete")]),
            "result_counts": result_counts(group),
        }
        for name, group in buckets.items()
    ]


def analyze_feedback(project_root: Path, generated_at: str) -> dict[str, Any]:
    rows = validation_rows(project_root)
    completed_rows = [row for row in rows if row.get("period_complete")]
    pending_rows = [row for row in rows if not row.get("period_complete")]
    success_rows = [row for row in completed_rows if row.get("validation_result") in SUCCESS_RESULTS]
    failure_rows = [row for row in completed_rows if row.get("validation_result") == "Poor"]

    memory_root = project_root / "memory"
    scoring = scoring_by_ticker(project_root)
    result_counter = Counter(row.get("validation_result") for row in rows)
    completed_counter = Counter(row.get("validation_result") for row in completed_rows)

    analysis = {
        "generated_at": generated_at,
        "inputs": {
            "discovery_memory_count": len(load_collection(memory_root / "discoveries")),
            "validation_memory_count": len(load_collection(memory_root / "validations")),
            "company_memory_count": len(load_collection(memory_root / "companies")),
            "sector_memory_count": len(load_collection(memory_root / "sectors")),
            "scoring_count": len(scoring),
            "knowledge_files_used": [
                "feedback_framework.md",
                "improvement_patterns.md",
                "success_patterns.md",
                "failure_patterns.md",
                "scoring_rules.md",
                "validation_rules.md",
            ],
        },
        "overview": {
            "validation_count": len(rows),
            "completed_count": len(completed_rows),
            "pending_count": len(pending_rows),
            "success_count": len(success_rows),
            "failure_count": len(failure_rows),
            "success_rate": pct(len(success_rows), len(completed_rows)),
            "failure_rate": pct(len(failure_rows), len(completed_rows)),
            "result_counts": dict(result_counter),
            "completed_result_counts": dict(completed_counter),
        },
        "discovery_accuracy": group_rows(rows, "validation_result"),
        "score_accuracy": score_buckets(rows, scoring),
        "confidence_accuracy": confidence_accuracy(rows),
        "sector_accuracy": group_rows(rows, "sector"),
        "event_accuracy": event_accuracy(rows),
        "success_patterns": aggregate_reason_categories(completed_rows, {"Excellent", "Good"}),
        "failure_patterns": aggregate_reason_categories(completed_rows, {"Poor"}),
        "pending_patterns": aggregate_reason_categories(pending_rows, {"Neutral"}),
    }
    analysis["improvement_candidates"] = detect_improvement_candidates(analysis)
    return analysis
