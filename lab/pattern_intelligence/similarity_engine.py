from itertools import combinations
from math import sqrt
from typing import Any


class SimilarityEngine:
    """Calculates company similarity from extracted feature vectors."""

    def calculate(self, features: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
        companies = features.get("companies", {})
        vectors = {ticker: self._vector(item) for ticker, item in companies.items()}
        output: dict[str, list[dict[str, Any]]] = {ticker: [] for ticker in companies}
        for left, right in combinations(sorted(companies), 2):
            score = self._cosine(vectors[left], vectors[right])
            reasons = self._reasons(companies[left], companies[right])
            pair = {"ticker": right, "similarity": round(score, 3), "reasons": reasons}
            output[left].append(pair)
            output[right].append({"ticker": left, "similarity": round(score, 3), "reasons": reasons})
        return {ticker: sorted(rows, key=lambda item: item["similarity"], reverse=True)[:5] for ticker, rows in output.items()}

    def _vector(self, item: dict[str, Any]) -> list[float]:
        financials = item.get("financials", {})
        activity = item.get("activity", {})
        validation = item.get("validation", {})
        results = validation.get("results", {})
        return [
            self._num(financials.get("rd_ratio")),
            self._num(financials.get("profit_margin")),
            self._num(financials.get("operating_margin")),
            self._num(financials.get("eps")) / 100,
            self._num(financials.get("trailing_pe")) / 100,
            self._num(activity.get("momentum_1m")) / 100,
            self._num(activity.get("momentum_3m")) / 100,
            self._num(activity.get("news_count")) / 20,
            self._num(activity.get("event_count")) / 20,
            self._num(results.get("Excellent") + results.get("Good")) / 5,
        ]

    def _cosine(self, left: list[float], right: list[float]) -> float:
        dot = sum(a * b for a, b in zip(left, right))
        left_norm = sqrt(sum(a * a for a in left))
        right_norm = sqrt(sum(b * b for b in right))
        if left_norm == 0 or right_norm == 0:
            return 0.0
        return dot / (left_norm * right_norm)

    def _reasons(self, left: dict[str, Any], right: dict[str, Any]) -> list[str]:
        reasons = []
        if left.get("sector") == right.get("sector"):
            reasons.append(f"Same sector: {left.get('sector')}")
        if left.get("market", {}).get("sector_trend") == right.get("market", {}).get("sector_trend"):
            reasons.append("Similar sector trend context")
        if abs(self._num(left.get("activity", {}).get("momentum_1m")) - self._num(right.get("activity", {}).get("momentum_1m"))) < 5:
            reasons.append("Similar 1M momentum")
        if abs(self._num(left.get("financials", {}).get("profit_margin")) - self._num(right.get("financials", {}).get("profit_margin"))) < 0.1:
            reasons.append("Similar profit margin range")
        return reasons or ["Feature vector similarity"]

    def _num(self, value: Any) -> float:
        try:
            return float(value or 0)
        except (TypeError, ValueError):
            return 0.0
