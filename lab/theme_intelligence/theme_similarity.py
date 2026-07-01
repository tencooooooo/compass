from itertools import combinations
from math import sqrt
from typing import Any


class ThemeSimilarity:
    """Calculates theme-to-theme similarity from companies, sectors, and metrics."""

    def calculate(self, themes: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
        vectors = {theme: self._vector(item) for theme, item in themes.items()}
        output: dict[str, list[dict[str, Any]]] = {theme: [] for theme in themes}
        for left, right in combinations(sorted(themes), 2):
            similarity = self._cosine(vectors[left], vectors[right])
            reasons = self._reasons(themes[left], themes[right])
            output[left].append({"theme": right, "similarity": round(similarity, 3), "reasons": reasons})
            output[right].append({"theme": left, "similarity": round(similarity, 3), "reasons": reasons})
        return {theme: sorted(rows, key=lambda item: item["similarity"], reverse=True)[:5] for theme, rows in output.items()}

    def _vector(self, item: dict[str, Any]) -> list[float]:
        validation = item.get("validation", {})
        return [
            self._num(item.get("company_count")) / 10,
            self._num(item.get("average_score")) / 100,
            self._num(item.get("average_discovery")) / 100,
            self._num(item.get("momentum", {}).get("average_1m")) / 100,
            (self._num(validation.get("Excellent")) + self._num(validation.get("Good"))) / 10,
            self._num(validation.get("Poor")) / 10,
        ]

    def _cosine(self, left: list[float], right: list[float]) -> float:
        dot = sum(a * b for a, b in zip(left, right))
        left_norm = sqrt(sum(a * a for a in left))
        right_norm = sqrt(sum(b * b for b in right))
        if left_norm == 0 or right_norm == 0:
            return 0.0
        return dot / (left_norm * right_norm)

    def _reasons(self, left: dict[str, Any], right: dict[str, Any]) -> list[str]:
        left_tickers = {company.get("ticker") for company in left.get("companies", [])}
        right_tickers = {company.get("ticker") for company in right.get("companies", [])}
        shared_tickers = sorted(ticker for ticker in left_tickers & right_tickers if ticker)
        left_sectors = {company.get("sector") for company in left.get("companies", [])}
        right_sectors = {company.get("sector") for company in right.get("companies", [])}
        shared_sectors = sorted(sector for sector in left_sectors & right_sectors if sector)
        reasons = []
        if shared_tickers:
            reasons.append(f"Shared companies: {', '.join(shared_tickers[:5])}")
        if shared_sectors:
            reasons.append(f"Shared sectors: {', '.join(shared_sectors[:3])}")
        if abs(self._num(left.get("average_discovery")) - self._num(right.get("average_discovery"))) <= 5:
            reasons.append("Similar average Discovery score")
        if abs(self._num(left.get("momentum", {}).get("average_1m")) - self._num(right.get("momentum", {}).get("average_1m"))) <= 5:
            reasons.append("Similar short-term momentum")
        return reasons or ["Theme metric similarity"]

    def _num(self, value: Any) -> float:
        try:
            return float(value or 0)
        except (TypeError, ValueError):
            return 0.0
