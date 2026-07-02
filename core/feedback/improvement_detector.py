from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from utils.values import safe_float


SUCCESS_RESULTS = {"Excellent", "Good"}
FAILURE_RESULTS = {"Poor"}
PENDING_RESULTS = {"Neutral"}


def pct(numerator: int | float, denominator: int | float) -> float | None:
    if denominator == 0:
        return None
    return round(float(numerator) / float(denominator) * 100, 2)


def average(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def classify_reason(text: str) -> str:
    normalized = text.lower()
    if any(token in normalized for token in ["研究開発", "r&d", "rd"]):
        return "R&D"
    if any(token in normalized for token in ["per", "peg", "pbr", "valuation", "バリュエーション"]):
        return "Valuation"
    if any(token in normalized for token in ["momentum", "モメンタム"]):
        return "Momentum"
    if any(token in normalized for token in ["news", "ニュース"]):
        return "News"
    if any(token in normalized for token in ["financial", "財務", "fcf", "cash", "利益率"]):
        return "Financial Health"
    if any(token in normalized for token in ["event", "出来高", "株価反応"]):
        return "Event Reaction"
    if any(token in normalized for token in ["sector", "セクター"]):
        return "Sector Context"
    if any(token in normalized for token in ["growth", "成長", "売上"]):
        return "Growth"
    return "Other"


def aggregate_reason_categories(rows: list[dict[str, Any]], result_filter: set[str]) -> list[dict[str, Any]]:
    counter: Counter[str] = Counter()
    examples: dict[str, str] = {}
    for row in rows:
        if row.get("validation_result") not in result_filter:
            continue
        for reason in row.get("discovery_reasons", []) or []:
            category = classify_reason(str(reason))
            counter[category] += 1
            examples.setdefault(category, str(reason))
    return [
        {"category": category, "count": count, "example": examples.get(category, "")}
        for category, count in counter.most_common()
    ]


def result_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    counter = Counter(row.get("validation_result", "Unknown") for row in rows)
    return {
        "Excellent": counter.get("Excellent", 0),
        "Good": counter.get("Good", 0),
        "Neutral": counter.get("Neutral", 0),
        "Poor": counter.get("Poor", 0),
        "Unknown": counter.get("Unknown", 0),
    }


def group_rows(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "Unknown")].append(row)
    results: list[dict[str, Any]] = []
    for name, group in sorted(grouped.items()):
        complete = [row for row in group if row.get("period_complete")]
        successes = [row for row in complete if row.get("validation_result") in SUCCESS_RESULTS]
        failures = [row for row in complete if row.get("validation_result") in FAILURE_RESULTS]
        returns = [safe_float(row.get("return_percent")) for row in complete]
        returns = [value for value in returns if value is not None]
        results.append(
            {
                key: name,
                "total_count": len(group),
                "completed_count": len(complete),
                "success_count": len(successes),
                "failure_count": len(failures),
                "success_rate": pct(len(successes), len(complete)),
                "failure_rate": pct(len(failures), len(complete)),
                "average_return": average(returns),
                "result_counts": result_counts(group),
            }
        )
    return results


def score_buckets(rows: list[dict[str, Any]], scoring_by_ticker: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    buckets = {
        "High Score (75+)": [],
        "Mid Score (60-74)": [],
        "Low Score (<60)": [],
        "Unknown": [],
    }
    for row in rows:
        ticker = str(row.get("ticker") or "").upper()
        score = safe_float(scoring_by_ticker.get(ticker, {}).get("total_score"))
        if score is None:
            buckets["Unknown"].append(row)
        elif score >= 75:
            buckets["High Score (75+)"].append(row)
        elif score >= 60:
            buckets["Mid Score (60-74)"].append(row)
        else:
            buckets["Low Score (<60)"].append(row)
    return [
        {
            "bucket": name,
            "total_count": len(group),
            "completed_count": len([row for row in group if row.get("period_complete")]),
            "result_counts": result_counts(group),
        }
        for name, group in buckets.items()
    ]


def detect_improvement_candidates(analysis: dict[str, Any]) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    completed_count = analysis["overview"]["completed_count"]
    pending_count = analysis["overview"]["pending_count"]

    if completed_count == 0:
        candidates.append(
            {
                "priority": "High",
                "area": "Validation Horizon",
                "candidate": "検証期間が未完了の候補を成功/失敗判定から分離し、十分な期間が経過するまで改善判断を保留する。",
                "reason": f"完了済みValidationが0件で、未完了が{pending_count}件あります。",
            }
        )

    for sector in analysis.get("sector_accuracy", []):
        if sector.get("completed_count") == 0:
            continue
        if sector.get("failure_rate") is not None and sector["failure_rate"] >= 40:
            candidates.append(
                {
                    "priority": "Medium",
                    "area": "Sector Accuracy",
                    "candidate": f"{sector['sector']} セクターのMomentum補正または評価条件を見直す。",
                    "reason": f"完了済みValidationの失敗率が {sector['failure_rate']}% です。",
                }
            )

    high_bucket = next((item for item in analysis.get("score_accuracy", []) if item["bucket"].startswith("High")), None)
    if high_bucket and high_bucket.get("completed_count", 0) > 0:
        counts = high_bucket.get("result_counts", {})
        if counts.get("Poor", 0) > counts.get("Excellent", 0) + counts.get("Good", 0):
            candidates.append(
                {
                    "priority": "High",
                    "area": "Score Accuracy",
                    "candidate": "高スコア企業の評価でValuationまたはMomentumの重みを再確認する。",
                    "reason": "High Score bucketでPoorが成功件数を上回っています。",
                }
            )

    for category in analysis.get("failure_patterns", [])[:3]:
        candidates.append(
            {
                "priority": "Low",
                "area": category["category"],
                "candidate": f"{category['category']} に関する失敗パターンをKnowledgeへ追加候補としてレビューする。",
                "reason": category.get("example", ""),
            }
        )

    if not candidates:
        candidates.append(
            {
                "priority": "Low",
                "area": "Knowledge Review",
                "candidate": "成功/失敗パターンの蓄積を継続し、完了済みValidationが増えてからKnowledge更新を検討する。",
                "reason": "現時点では自動的に強い改善仮説を出すだけの完了済み検証が不足しています。",
            }
        )

    return candidates
