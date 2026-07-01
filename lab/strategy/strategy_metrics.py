from __future__ import annotations

from math import sqrt
from statistics import mean, pstdev
from typing import Any


class StrategyMetrics:
    """Calculates research-only portfolio simulation metrics."""

    def calculate(self, simulation: dict[str, Any], benchmark_return: float | None = None) -> dict[str, Any]:
        trades = simulation.get("trades", [])
        returns = [float(trade["return_percent"]) for trade in trades if isinstance(trade.get("return_percent"), (int, float))]
        total_return = float(simulation.get("total_return", 0))
        holding_days = [int(trade.get("holding_days", 0)) for trade in trades]
        years = max(max(holding_days, default=0) / 365, 1 / 365)
        return {
            "cagr": round(((1 + total_return / 100) ** (1 / years) - 1) * 100, 2) if total_return > -100 else None,
            "total_return": round(total_return, 2),
            "win_rate": self._rate(len([value for value in returns if value > 0]), len(returns)),
            "sharpe_ratio": self._sharpe(returns),
            "max_drawdown": self._max_drawdown(simulation.get("equity_curve", [])),
            "alpha": round(total_return - benchmark_return, 2) if benchmark_return is not None else None,
            "beta": None,
            "volatility": round(pstdev(returns), 2) if len(returns) > 1 else None,
            "average_holding_period": round(mean(holding_days), 2) if holding_days else None,
        }

    def _rate(self, numerator: int, denominator: int) -> float | None:
        if denominator == 0:
            return None
        return round(numerator / denominator * 100, 2)

    def _sharpe(self, returns: list[float]) -> float | None:
        if len(returns) < 2:
            return None
        deviation = pstdev(returns)
        if deviation == 0:
            return None
        return round(mean(returns) / deviation * sqrt(len(returns)), 3)

    def _max_drawdown(self, equity_curve: list[dict[str, Any]]) -> float | None:
        values = [float(row["value"]) for row in equity_curve if isinstance(row.get("value"), (int, float))]
        if not values:
            return None
        peak = values[0]
        max_drawdown = 0.0
        for value in values:
            peak = max(peak, value)
            drawdown = (value - peak) / peak * 100 if peak else 0
            max_drawdown = min(max_drawdown, drawdown)
        return round(max_drawdown, 2)
