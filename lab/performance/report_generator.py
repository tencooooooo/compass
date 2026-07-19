from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT


class ReportGenerator:
    """Writes Performance Evaluation reports."""

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.output_dir = repo_root / "reports" / "performance"

    def write(self, evaluation: dict[str, Any], metrics: dict[str, Any]) -> dict[str, str]:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "summary": self.output_dir / "performance_summary.md",
            "discovery": self.output_dir / "discovery_accuracy.md",
            "benchmark": self.output_dir / "benchmark_comparison.md",
            "sector": self.output_dir / "sector_accuracy.md",
            "theme": self.output_dir / "theme_accuracy.md",
            "dashboard": self.output_dir / "dashboard_metrics.json",
        }
        files["summary"].write_text(self._summary(evaluation, metrics), encoding="utf-8")
        files["discovery"].write_text(self._discovery_report(metrics), encoding="utf-8")
        files["benchmark"].write_text(self._benchmark_report(evaluation), encoding="utf-8")
        files["sector"].write_text(self._group_report("Sector Accuracy", metrics["sector_accuracy"]), encoding="utf-8")
        files["theme"].write_text(self._group_report("Theme Accuracy", metrics["theme_accuracy"]), encoding="utf-8")
        files["dashboard"].write_text(json.dumps(metrics["dashboard"], ensure_ascii=False, indent=2), encoding="utf-8")
        return {name: str(path.relative_to(self.repo_root)) for name, path in files.items()}

    def _summary(self, evaluation: dict[str, Any], metrics: dict[str, Any]) -> str:
        overall = metrics["overall"]
        lines = [
            "# Performance Summary",
            "",
            "Performance Evaluation is Compass's scorecard. It measures outcomes without changing Feedback, Learning, Knowledge, or Scoring.",
            "",
            f"- Evaluation date: {evaluation['evaluation_date']}",
            f"- Signals: {len(evaluation.get('signals', []))}",
            f"- Evaluation rows: {overall.get('evaluated_count', 0)}",
            f"- Completed rows: {overall.get('completed_count', 0)}",
            f"- Pending rows: {overall.get('pending_count', 0)}",
            f"- Discovery Success Rate: {self._fmt(overall.get('discovery_success_rate'))}",
            f"- Average Return: {self._fmt(overall.get('average_return'))}",
            f"- Median Return: {self._fmt(overall.get('median_return'))}",
            f"- Win Rate: {self._fmt(overall.get('win_rate'))}",
            f"- Loss Rate: {self._fmt(overall.get('loss_rate'))}",
            f"- Alpha vs Benchmark: {self._fmt(overall.get('alpha_vs_benchmark'))}",
            f"- Worst Return: {self._fmt(overall.get('worst_return'))}",
            "",
            "## Note",
            "",
            "Rows remain pending until the full evaluation period has elapsed and price data is available.",
            "",
        ]
        return "\n".join(lines)

    def _group_report(self, title: str, grouped: dict[str, Any]) -> str:
        lines = [f"# {title}", ""]
        for name, item in grouped.items():
            lines.extend(
                [
                    f"## {name}",
                    "",
                    f"- Evaluated: {item.get('evaluated_count', 0)}",
                    f"- Completed: {item.get('completed_count', 0)}",
                    f"- Pending: {item.get('pending_count', 0)}",
                    f"- Success Rate: {self._fmt(item.get('discovery_success_rate'))}",
                    f"- Average Return: {self._fmt(item.get('average_return'))}",
                    f"- Win Rate: {self._fmt(item.get('win_rate'))}",
                    f"- Alpha vs Benchmark: {self._fmt(item.get('alpha_vs_benchmark'))}",
                    "",
                ]
            )
        return "\n".join(lines)

    def _discovery_report(self, metrics: dict[str, Any]) -> str:
        lines = ["# Discovery Accuracy", "", "## Period Accuracy", ""]
        lines.append(self._group_report("Periods", metrics["periods"]))
        lines.extend(["", "## Discovery Score Accuracy", ""])
        lines.append(self._group_report("Score Buckets", metrics.get("score_accuracy", {})))
        lines.extend(["", "## Confidence Accuracy", ""])
        lines.append(self._group_report("Confidence", metrics.get("confidence_accuracy", {})))
        lines.extend(["", "## Confidence Validation Result Distribution", ""])
        lines.append(self._confidence_distribution_report(metrics.get("confidence_result_distribution", {})))
        lines.extend(["", "## Pattern Accuracy", ""])
        lines.append(self._group_report("Patterns", metrics.get("pattern_accuracy", {})))
        lines.extend(["", "## Market Intelligence Accuracy", ""])
        lines.append(self._group_report("Market", metrics.get("market_accuracy", {})))
        return "\n".join(lines)

    def _confidence_distribution_report(self, grouped: dict[str, Any]) -> str:
        lines = ["# Confidence Result Distribution", ""]
        for confidence, item in grouped.items():
            distribution = item.get("validation_results", {})
            lines.extend(
                [
                    f"## {confidence}",
                    "",
                    f"- Evaluated: {item.get('evaluated_count', 0)}",
                    f"- Completed: {item.get('completed_count', 0)}",
                    f"- Hit Rate: {self._fmt(item.get('hit_rate'))}",
                    f"- Excellent: {distribution.get('Excellent', 0)}",
                    f"- Good: {distribution.get('Good', 0)}",
                    f"- Neutral: {distribution.get('Neutral', 0)}",
                    f"- Poor: {distribution.get('Poor', 0)}",
                    f"- Pending: {distribution.get('Pending', 0)}",
                    "",
                ]
            )
        return "\n".join(lines)

    def _benchmark_report(self, evaluation: dict[str, Any]) -> str:
        lines = ["# Benchmark Comparison", "", "Benchmarks: S&P500, Nasdaq100, Russell2000.", ""]
        for row in evaluation.get("rows", [])[:50]:
            benchmark = row.get("benchmark", {})
            lines.extend(
                [
                    f"## {row.get('ticker')} - {row.get('period')} days",
                    "",
                    f"- Status: {row.get('status')}",
                    f"- Return: {self._fmt(row.get('return_percent'))}",
                    f"- Benchmark average: {self._fmt(benchmark.get('average_return_percent'))}",
                    f"- Alpha: {self._fmt(row.get('alpha_percent'))}",
                    "",
                ]
            )
        return "\n".join(lines)

    def _fmt(self, value: Any) -> str:
        if value is None:
            return "N/A"
        return f"{value:.2f}%" if isinstance(value, float) else str(value)
