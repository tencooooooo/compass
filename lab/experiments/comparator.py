from __future__ import annotations

from typing import Any


COMPARISON_KEYS = (
    "discovery_success_rate",
    "average_return",
    "alpha",
    "win_rate",
    "max_drawdown",
    "sharpe_ratio",
    "strategy_ranking",
    "performance_score",
)


class Comparator:
    """Compares baseline and candidate metrics and decides a winner."""

    def compare(self, baseline: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
        comparisons = {}
        baseline_score = 0.0
        candidate_score = 0.0
        usable = 0
        for key in COMPARISON_KEYS:
            left = baseline.get(key)
            right = candidate.get(key)
            outcome = self._compare_value(key, left, right)
            comparisons[key] = {"baseline": left, "candidate": right, **outcome}
            if outcome["winner"] == "Baseline":
                baseline_score += 1
                usable += 1
            elif outcome["winner"] == "Candidate":
                candidate_score += 1
                usable += 1
            elif outcome["winner"] == "Tie":
                usable += 1
        if usable == 0:
            winner = "Inconclusive"
            reason = "No comparable completed metrics are available yet."
        elif candidate_score > baseline_score:
            winner = "Candidate"
            reason = f"Candidate wins {candidate_score} metrics vs baseline {baseline_score}."
        elif baseline_score > candidate_score:
            winner = "Baseline"
            reason = f"Baseline wins {baseline_score} metrics vs candidate {candidate_score}."
        else:
            winner = "Tie"
            reason = "Baseline and candidate are tied on comparable metrics."
        return {
            "winner": winner,
            "reason": reason,
            "baseline_score": baseline_score,
            "candidate_score": candidate_score,
            "comparisons": comparisons,
        }

    def _compare_value(self, key: str, baseline: Any, candidate: Any) -> dict[str, Any]:
        if baseline is None or candidate is None:
            return {"winner": "Inconclusive", "reason": "Metric is not available for both versions."}
        try:
            left = float(baseline)
            right = float(candidate)
        except (TypeError, ValueError):
            return {"winner": "Inconclusive", "reason": "Metric is not numeric."}
        if key == "max_drawdown":
            if right > left:
                return {"winner": "Candidate", "reason": "Candidate has lower drawdown severity."}
            if left > right:
                return {"winner": "Baseline", "reason": "Baseline has lower drawdown severity."}
        else:
            if right > left:
                return {"winner": "Candidate", "reason": "Candidate metric is higher."}
            if left > right:
                return {"winner": "Baseline", "reason": "Baseline metric is higher."}
        return {"winner": "Tie", "reason": "Metric is equal."}
