from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT


class ExperimentReport:
    """Writes Experiment Engine reports and dashboard JSON."""

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.output_dir = repo_root / "reports" / "experiments"

    def write(self, results: list[dict[str, Any]]) -> dict[str, str]:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "summary": self.output_dir / "experiment_summary.md",
            "results": self.output_dir / "experiment_results.md",
            "comparison": self.output_dir / "experiment_comparison.md",
            "dashboard": self.output_dir / "dashboard.json",
        }
        files["summary"].write_text(self._summary(results), encoding="utf-8")
        files["results"].write_text(self._results(results), encoding="utf-8")
        files["comparison"].write_text(self._comparison(results), encoding="utf-8")
        files["dashboard"].write_text(json.dumps({"experiments": results}, ensure_ascii=False, indent=2), encoding="utf-8")
        return {name: str(path.relative_to(self.repo_root)) for name, path in files.items()}

    def _summary(self, results: list[dict[str, Any]]) -> str:
        lines = ["# Experiment Summary", "", "Experiment Engine compares baseline and candidate Compass versions using reproducible scorecard metrics.", ""]
        for result in results:
            lines.extend(
                [
                    f"## {result['experiment_id']} - {result.get('name')}",
                    "",
                    f"- Target: {result.get('target')}",
                    f"- Baseline: {result.get('baseline_version')}",
                    f"- Candidate: {result.get('candidate_version')}",
                    f"- Status: {result.get('status')}",
                    f"- Winner: {result.get('winner')}",
                    f"- Reason: {result.get('winner_reason')}",
                    "",
                ]
            )
        return "\n".join(lines)

    def _results(self, results: list[dict[str, Any]]) -> str:
        lines = ["# Experiment Results", ""]
        for result in results:
            lines.extend([f"## {result['experiment_id']}", "", "### Baseline Metrics", ""])
            for key, value in result.get("baseline_metrics", {}).items():
                lines.append(f"- {key}: {self._fmt(value)}")
            lines.extend(["", "### Candidate Metrics", ""])
            for key, value in result.get("candidate_metrics", {}).items():
                lines.append(f"- {key}: {self._fmt(value)}")
            lines.append("")
        return "\n".join(lines)

    def _comparison(self, results: list[dict[str, Any]]) -> str:
        lines = ["# Experiment Comparison", ""]
        for result in results:
            lines.extend([f"## {result['experiment_id']}", ""])
            comparisons = result.get("comparison", {}).get("comparisons", {})
            for key, comparison in comparisons.items():
                lines.append(
                    f"- {key}: {comparison.get('winner')} "
                    f"(baseline={self._fmt(comparison.get('baseline'))}, candidate={self._fmt(comparison.get('candidate'))}) - {comparison.get('reason')}"
                )
            lines.append("")
        return "\n".join(lines)

    def _fmt(self, value: Any) -> str:
        return "N/A" if value is None else str(value)
