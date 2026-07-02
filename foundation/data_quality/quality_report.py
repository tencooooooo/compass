from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT


class QualityReport:
    """Writes Data Quality reports and dashboard payloads."""

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.report_dir = repo_root / "reports" / "data_quality"
        self.storage_dir = repo_root / "storage" / "quality"

    def write(self, result: dict[str, Any]) -> dict[str, str]:
        self.report_dir.mkdir(parents=True, exist_ok=True)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "provider_scores": self.storage_dir / "provider_scores.json",
            "history": self.storage_dir / "history.json",
            "issues": self.storage_dir / "issues.json",
            "summary": self.report_dir / "quality_summary.md",
            "ranking": self.report_dir / "provider_ranking.md",
            "detected_issues": self.report_dir / "detected_issues.md",
            "dashboard": self.report_dir / "dashboard.json",
        }
        files["provider_scores"].write_text(json.dumps(result["providers"], ensure_ascii=False, indent=2), encoding="utf-8")
        files["issues"].write_text(json.dumps(result["issues"], ensure_ascii=False, indent=2), encoding="utf-8")
        files["history"].write_text(json.dumps(self._history(result), ensure_ascii=False, indent=2), encoding="utf-8")
        files["summary"].write_text(self._summary(result), encoding="utf-8")
        files["ranking"].write_text(self._ranking(result), encoding="utf-8")
        files["detected_issues"].write_text(self._issues(result), encoding="utf-8")
        files["dashboard"].write_text(json.dumps(self._dashboard(result), ensure_ascii=False, indent=2), encoding="utf-8")
        return {name: str(path.relative_to(self.repo_root)) for name, path in files.items()}

    def _history(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        path = self.storage_dir / "history.json"
        history = []
        if path.exists():
            try:
                history = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                history = []
        history.append(
            {
                "evaluation_date": result["evaluation_date"],
                "overall_quality_score": result["overall_quality_score"],
                "providers": [
                    {"provider": row["provider"], "quality_score": row["quality_score"]}
                    for row in result["providers"]
                ],
            }
        )
        return history[-100:]

    def _summary(self, result: dict[str, Any]) -> str:
        lines = [
            "# Data Quality Summary",
            "",
            "Data Quality Engine evaluates Compass input data before analysis. It does not stop workflows; low scores create warnings for human review.",
            "",
            f"- Evaluation date: {result['evaluation_date']}",
            f"- Overall Quality Score: {result['overall_quality_score']}",
            f"- Providers evaluated: {len(result['providers'])}",
            f"- Warning threshold: {result['warning_threshold']}",
            f"- Warning: {result['warning']}",
            "",
            "## Provider Scores",
            "",
        ]
        for row in result["providers"]:
            lines.append(f"- {row['provider']}: {row['quality_score']} (freshness {row['freshness']}, completeness {row['completeness']}, reliability {row['reliability']})")
        return "\n".join(lines) + "\n"

    def _ranking(self, result: dict[str, Any]) -> str:
        rows = sorted(result["providers"], key=lambda row: row["quality_score"], reverse=True)
        lines = ["# Provider Ranking", ""]
        for index, row in enumerate(rows, start=1):
            lines.append(f"{index}. {row['provider']} - Quality Score {row['quality_score']} ({row['source_type']})")
        return "\n".join(lines) + "\n"

    def _issues(self, result: dict[str, Any]) -> str:
        lines = ["# Detected Data Quality Issues", ""]
        if not result["issues"]:
            lines.append("- No data quality issues detected.")
        for issue in result["issues"]:
            lines.append(f"- {issue['provider']} / {issue['category']}: {issue['severity']}")
        return "\n".join(lines) + "\n"

    def _dashboard(self, result: dict[str, Any]) -> dict[str, Any]:
        return {
            "evaluation_date": result["evaluation_date"],
            "overall_quality_score": result["overall_quality_score"],
            "warning": result["warning"],
            "warning_threshold": result["warning_threshold"],
            "providers": result["providers"],
            "issue_count": len(result["issues"]),
        }

