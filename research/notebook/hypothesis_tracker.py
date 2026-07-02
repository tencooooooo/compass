from __future__ import annotations

from typing import Any


class HypothesisTracker:
    """Summarizes hypothesis status from Notebook metadata."""

    def status_report(self, entries: list[dict[str, Any]]) -> str:
        lines = ["# Hypothesis Status", "", "Hypotheses are tracked from Research Notebook metadata.", ""]
        if not entries:
            lines.append("- No hypotheses recorded yet.")
            return "\n".join(lines) + "\n"
        grouped: dict[str, list[dict[str, Any]]] = {}
        for entry in entries:
            grouped.setdefault(entry.get("status", "Draft"), []).append(entry)
        for status, rows in sorted(grouped.items()):
            lines.extend([f"## {status}", ""])
            for row in rows:
                hypothesis = row.get("hypothesis") or "No hypothesis text"
                lines.append(f"- {row.get('date')} / {row.get('category')}: {row.get('title')} - {hypothesis}")
            lines.append("")
        return "\n".join(lines)

