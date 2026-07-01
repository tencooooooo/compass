from __future__ import annotations

from pathlib import Path
from datetime import date
from typing import Any

from api.services.data_loader import REPO_ROOT, read_json
from lab.experiments.comparator import Comparator


class ExperimentRunner:
    """Runs baseline vs candidate comparisons from Compass scorecard data."""

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.comparator = Comparator()

    def run(self, definition: dict[str, Any]) -> dict[str, Any]:
        baseline_metrics = self._baseline_metrics(definition)
        candidate_metrics = self._candidate_metrics(definition)
        comparison = self.comparator.compare(baseline_metrics, candidate_metrics)
        return {
            **self._json_safe(definition),
            "baseline_metrics": baseline_metrics,
            "candidate_metrics": candidate_metrics,
            "winner": comparison["winner"],
            "winner_reason": comparison["reason"],
            "comparison": comparison,
            "status": self._status(definition, comparison["winner"]),
        }

    def _baseline_metrics(self, definition: dict[str, Any]) -> dict[str, Any]:
        performance = read_json("reports/performance/dashboard_metrics.json", {})
        strategy = read_json("reports/strategy/dashboard.json", {})
        return self._extract_metrics(performance, strategy)

    def _candidate_metrics(self, definition: dict[str, Any]) -> dict[str, Any]:
        candidate_path = definition.get("candidate_metrics_path")
        if candidate_path:
            data = read_json(str(candidate_path), {})
            if data:
                return data
        # Until a candidate run is provided, use current metrics as a reproducible placeholder.
        performance = read_json("reports/performance/dashboard_metrics.json", {})
        strategy = read_json("reports/strategy/dashboard.json", {})
        return self._extract_metrics(performance, strategy)

    def _extract_metrics(self, performance: dict[str, Any], strategy: dict[str, Any]) -> dict[str, Any]:
        overall = performance.get("overall", {}) if isinstance(performance, dict) else {}
        best_strategy = self._best_strategy(strategy)
        return {
            "discovery_success_rate": overall.get("discovery_success_rate"),
            "average_return": overall.get("average_return"),
            "alpha": overall.get("alpha_vs_benchmark") or (best_strategy.get("metrics", {}) or {}).get("alpha"),
            "win_rate": overall.get("win_rate") or (best_strategy.get("metrics", {}) or {}).get("win_rate"),
            "max_drawdown": overall.get("max_drawdown") or (best_strategy.get("metrics", {}) or {}).get("max_drawdown"),
            "sharpe_ratio": (best_strategy.get("metrics", {}) or {}).get("sharpe_ratio"),
            "strategy_ranking": self._strategy_rank_score(strategy),
            "performance_score": self._performance_score(overall, best_strategy),
        }

    def _best_strategy(self, strategy: dict[str, Any]) -> dict[str, Any]:
        rows = strategy.get("strategies", []) if isinstance(strategy, dict) else []
        if not rows:
            return {}
        return sorted(rows, key=lambda row: (row.get("metrics", {}) or {}).get("total_return") or -999, reverse=True)[0]

    def _strategy_rank_score(self, strategy: dict[str, Any]) -> float | None:
        rows = strategy.get("strategies", []) if isinstance(strategy, dict) else []
        if not rows:
            return None
        returns = [(row.get("metrics", {}) or {}).get("total_return") for row in rows]
        numeric = [float(value) for value in returns if isinstance(value, (int, float))]
        return round(sum(numeric) / len(numeric), 2) if numeric else None

    def _performance_score(self, overall: dict[str, Any], best_strategy: dict[str, Any]) -> float | None:
        values = [
            overall.get("discovery_success_rate"),
            overall.get("average_return"),
            overall.get("alpha_vs_benchmark"),
            (best_strategy.get("metrics", {}) or {}).get("total_return"),
        ]
        numeric = [float(value) for value in values if isinstance(value, (int, float))]
        return round(sum(numeric) / len(numeric), 2) if numeric else None

    def _status(self, definition: dict[str, Any], winner: str) -> str:
        configured = definition.get("status") or "Pending"
        if winner == "Inconclusive":
            return "Pending"
        return configured if configured != "Pending" else "Completed"

    def _json_safe(self, value: Any) -> Any:
        if isinstance(value, date):
            return value.isoformat()
        if isinstance(value, dict):
            return {key: self._json_safe(item) for key, item in value.items()}
        if isinstance(value, list):
            return [self._json_safe(item) for item in value]
        return value
