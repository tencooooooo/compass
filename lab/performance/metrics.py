from __future__ import annotations

from statistics import mean, median
from typing import Any

from engines.validation.thresholds import classify_result, period_label_for_days


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
            "worst_return": round(min(returns), 2) if returns else None,
            "average_holding_return": self._average(returns),
            **self._ticker_equal_weight(rows, completed),
        }

    def _ticker_equal_weight(self, rows: list[dict[str, Any]], completed: list[dict[str, Any]]) -> dict[str, Any]:
        """同一銘柄の連続Discoveryによる擬似反復を除いた銘柄等重みの指標。

        行単位の平均は繰り返し発掘された銘柄(例: 高スコアを連発した1銘柄)に支配されるため、
        銘柄ごとの平均を先に取ってから銘柄間で等重み平均する。行単位指標と併記して解釈する。
        """
        returns_by_ticker: dict[str, list[float]] = {}
        alpha_by_ticker: dict[str, list[float]] = {}
        for row in completed:
            ticker = row.get("ticker")
            if not ticker:
                continue
            if isinstance(row.get("return_percent"), (int, float)):
                returns_by_ticker.setdefault(str(ticker), []).append(float(row["return_percent"]))
            if isinstance(row.get("alpha_percent"), (int, float)):
                alpha_by_ticker.setdefault(str(ticker), []).append(float(row["alpha_percent"]))
        ticker_mean_returns = [mean(values) for values in returns_by_ticker.values()]
        ticker_mean_alphas = [mean(values) for values in alpha_by_ticker.values()]
        ticker_wins = [value for value in ticker_mean_returns if value > 0]
        return {
            "unique_ticker_count": len({str(row["ticker"]) for row in rows if row.get("ticker")}),
            "completed_ticker_count": len(returns_by_ticker),
            "ticker_equal_weight_average_return": self._average(ticker_mean_returns),
            "ticker_equal_weight_alpha": self._average(ticker_mean_alphas),
            "ticker_equal_weight_win_rate": self._rate(len(ticker_wins), len(ticker_mean_returns)),
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

    def validation_distribution_by(self, rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
        groups: dict[str, list[dict[str, Any]]] = {}
        for row in rows:
            groups.setdefault(str(row.get(key) or "Unknown"), []).append(row)
        return {name: self._validation_distribution(items) for name, items in sorted(groups.items())}

    def _rate(self, numerator: int, denominator: int) -> float | None:
        if denominator == 0:
            return None
        return round(numerator / denominator * 100, 2)

    def _average(self, values: list[float]) -> float | None:
        return round(mean(values), 2) if values else None

    def _validation_distribution(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        completed = [row for row in rows if row.get("status") == "completed"]
        counts = {"Excellent": 0, "Good": 0, "Neutral": 0, "Poor": 0, "Pending": len(rows) - len(completed)}
        for row in completed:
            counts[self._validation_result(row)] += 1
        successful = counts["Excellent"] + counts["Good"]
        return {
            "evaluated_count": len(rows),
            "completed_count": len(completed),
            "validation_results": counts,
            "hit_rate": self._rate(successful, len(completed)),
        }

    def _validation_result(self, row: dict[str, Any]) -> str:
        existing = row.get("validation_result")
        if existing in {"Excellent", "Good", "Neutral", "Poor"}:
            return str(existing)
        try:
            value = float(row.get("return_percent"))
        except (TypeError, ValueError):
            return "Neutral"
        alpha = row.get("alpha_percent")
        benchmark_diff = float(alpha) if isinstance(alpha, (int, float)) else None
        # Validation Engineと同じ期間別閾値で分類する。7日行を1y基準(15%)で判定しないため。
        try:
            days = int(row.get("period"))
        except (TypeError, ValueError):
            days = 365
        return classify_result(value, benchmark_diff, True, period_label_for_days(days))

