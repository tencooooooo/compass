from __future__ import annotations


VALIDATION_PERIODS = {
    "1w": 7,
    "1m": 30,
    "3m": 90,
    "6m": 180,
    "1y": 365,
}

VALIDATION_THRESHOLDS = {
    "1w": {"excellent": 3.0, "good": 1.5, "poor": -1.5, "benchmark_excellent": 2.0, "benchmark_good": 1.0, "benchmark_poor": -1.0},
    "1m": {"excellent": 6.0, "good": 3.0, "poor": -3.0, "benchmark_excellent": 4.0, "benchmark_good": 2.0, "benchmark_poor": -2.0},
    "3m": {"excellent": 10.0, "good": 5.0, "poor": -5.0, "benchmark_excellent": 7.0, "benchmark_good": 3.0, "benchmark_poor": -3.0},
    "6m": {"excellent": 13.0, "good": 7.0, "poor": -7.0, "benchmark_excellent": 9.0, "benchmark_good": 4.0, "benchmark_poor": -4.0},
    "1y": {"excellent": 15.0, "good": 8.0, "poor": -8.0, "benchmark_excellent": 10.0, "benchmark_good": 5.0, "benchmark_poor": -5.0},
}


def period_label_for_days(days: int) -> str:
    """日数から最も近い検証期間ラベルを返します。"""
    return min(VALIDATION_PERIODS, key=lambda label: abs(VALIDATION_PERIODS[label] - days))


def threshold_note(period_label: str) -> str:
    threshold = VALIDATION_THRESHOLDS[period_label]
    return (
        "Validation thresholds "
        f"{period_label}: Excellent >= {threshold['excellent']}% or benchmark diff >= {threshold['benchmark_excellent']}%; "
        f"Good >= {threshold['good']}% or benchmark diff >= {threshold['benchmark_good']}%; "
        f"Poor <= {threshold['poor']}% or benchmark diff <= {threshold['benchmark_poor']}%."
    )


def classify_result(return_percent: float | None, benchmark_diff: float | None, period_complete: bool, period_label: str) -> str:
    if return_percent is None or not period_complete:
        return "Neutral"
    threshold = VALIDATION_THRESHOLDS[period_label]
    if return_percent >= threshold["excellent"] or (benchmark_diff is not None and benchmark_diff >= threshold["benchmark_excellent"]):
        return "Excellent"
    if return_percent >= threshold["good"] or (benchmark_diff is not None and benchmark_diff >= threshold["benchmark_good"]):
        return "Good"
    if return_percent <= threshold["poor"] or (benchmark_diff is not None and benchmark_diff <= threshold["benchmark_poor"]):
        return "Poor"
    return "Neutral"
