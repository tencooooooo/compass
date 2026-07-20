from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT
from lab.performance.evaluator import DEFAULT_PERIODS, Evaluator
from lab.performance.metrics import PerformanceMetrics
from lab.performance.report_generator import ReportGenerator


class PerformanceEngine:
    """Builds Compass's long-term analysis performance scorecard."""

    @classmethod
    def run(cls, periods: tuple[int, ...] = DEFAULT_PERIODS) -> dict[str, Any]:
        evaluation = Evaluator(periods=periods).evaluate()
        calculator = PerformanceMetrics()
        rows = evaluation["rows"]
        metrics = {
            "overall": calculator.summarize(rows),
            "periods": {str(period): calculator.summarize([row for row in rows if row.get("period") == period]) for period in periods},
            "sector_accuracy": calculator.grouped(rows, "sector"),
            "theme_accuracy": calculator.grouped(rows, "themes"),
            "pattern_accuracy": calculator.grouped(rows, "patterns"),
            "score_accuracy": calculator.grouped(rows, "discovery_score_bucket"),
            "confidence_accuracy": calculator.grouped(rows, "confidence"),
            "confidence_result_distribution": calculator.validation_distribution_by(rows, "confidence"),
            "signal_strength_accuracy": calculator.grouped(rows, "signal_strength"),
            "signal_strength_result_distribution": calculator.validation_distribution_by(rows, "signal_strength"),
            "market_accuracy": calculator.grouped(rows, "market_status"),
        }
        metrics["dashboard"] = cls._dashboard(evaluation, metrics)
        outputs = ReportGenerator().write(evaluation, metrics)
        history_path = cls._write_history(evaluation, metrics)
        return {
            "success": True,
            "evaluation_date": evaluation["evaluation_date"],
            "signals": len(evaluation.get("signals", [])),
            "rows": len(rows),
            "outputs": outputs,
            "history": str(history_path.relative_to(REPO_ROOT)),
        }

    @classmethod
    def _dashboard(cls, evaluation: dict[str, Any], metrics: dict[str, Any]) -> dict[str, Any]:
        return {
            "evaluation_date": evaluation["evaluation_date"],
            "overall": metrics["overall"],
            "periods": metrics["periods"],
            "sector_accuracy": metrics["sector_accuracy"],
            "theme_accuracy": metrics["theme_accuracy"],
            "pattern_accuracy": metrics["pattern_accuracy"],
            "score_accuracy": metrics["score_accuracy"],
            "confidence_accuracy": metrics["confidence_accuracy"],
            "confidence_result_distribution": metrics["confidence_result_distribution"],
            "signal_strength_accuracy": metrics["signal_strength_accuracy"],
            "signal_strength_result_distribution": metrics["signal_strength_result_distribution"],
            "market_accuracy": metrics["market_accuracy"],
        }

    @classmethod
    def _write_history(cls, evaluation: dict[str, Any], metrics: dict[str, Any]) -> Path:
        path = REPO_ROOT / "memory" / "performance" / "history.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        history = []
        if path.exists():
            try:
                history = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                history = []
        # 同日の再実行(workflow_dispatch/retry)で重複行が溜まらないよう、評価日+期間で最新結果に上書きする。
        merged: dict[tuple[str, int], dict[str, Any]] = {}
        for item in history:
            if isinstance(item, dict) and item.get("evaluation_date") is not None and item.get("period") is not None:
                merged[(str(item["evaluation_date"]), int(item["period"]))] = item
        for period, summary in metrics["periods"].items():
            entry = {
                "evaluation_date": evaluation["evaluation_date"],
                "period": int(period),
                "success_rate": summary.get("discovery_success_rate"),
                "average_return": summary.get("average_return"),
                "alpha": summary.get("alpha_vs_benchmark"),
                "benchmark": "S&P500/Nasdaq100/Russell2000",
            }
            merged[(str(entry["evaluation_date"]), entry["period"])] = entry
        history = [merged[key] for key in sorted(merged)]
        path.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")
        return path


if __name__ == "__main__":
    print(PerformanceEngine.run())
