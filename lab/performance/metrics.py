from __future__ import annotations

from statistics import mean, median
from typing import Any


class PerformanceMetrics:
    """Calculates Compass performance metrics from evaluated rows."""

    def summarize(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        completed = [row for row in rows if row.get("status") == "completed"]
        returns = [float(row["return_percent"]) for row in completed if isinstance(row.get("return_percent"), (int, float))]
        wins = [value for value in returns if value > 0]
        losses = [value for value in returns if value < 0]
        benchmark_returns = [
            float(row["benchmark_return_percent"])
            for row in completed
            if isinstance(row.get("benchmark_return_percent"), (int, float))
        ]
        alpha_values = [
            float(row["alpha_percent"])
            for row in completed
            if isinstance(row.get("alpha_percent"), (int, float))
        ]
        return {
            "evaluated_count": len(rows),
            "completed_count": len(completed),
            "pending_count": len(rows) - len(completed),
            "discovery_success_rate": self._rate(len(wins), len(completed)),
            "average_return": self._average(returns),
            "median_return": round(median(returns), 2) if returns else None,
            "win_rate": self._rate(len(wins), len(completed)),
            "loss_rate": self._rate(len(losses), len(completed)),
            "alpha_vs_benchmark": self._average(alpha_values),
            "benchmark_average_return": self._average(benchmark_returns),
            "max_drawdown": self._max_drawdown(completed),
            "average_holding_return": self._average(returns),
        }

    def grouped(self, rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
        output: dict[str, list[dict[str, Any]]] = {}
        for row in rows:
            value = row.get(key) or "Unknown"
            if isinstance(value, list):
                for item in value:
                    output.setdefault(str(item), []).append(row)
            else:
                output.setdefault(str(value), []).append(row)
        return {name: self.summarize(items) for name, items in sorted(output.items())}

    def _rate(self, numerator: int, denominator: int) -> float | None:
        if denominator == 0:
            return None
        return round(numerator / denominator * 100, 2)

    def _average(self, values: list[float]) -> float | None:
        return round(mean(values), 2) if values else None

    def _max_drawdown(self, rows: list[dict[str, Any]]) -> float | None:
        values = [float(row["return_percent"]) for row in rows if isinstance(row.get("return_percent"), (int, float))]
        if not values:
            return None
        peak = values[0]
        max_drawdown = 0.0
        for value in values:
            peak = max(peak, value)
            max_drawdown = min(max_drawdown, value - peak)
        return round(max_drawdown, 2)
