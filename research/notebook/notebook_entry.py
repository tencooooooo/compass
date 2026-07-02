from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any


CATEGORIES = {
    "Discovery",
    "Theme",
    "Pattern",
    "Data Source",
    "Learning",
    "Strategy",
    "Experiment",
    "Time Machine",
    "Performance",
    "Data Quality",
    "General",
}


@dataclass
class NotebookEntry:
    """One human-readable Compass research notebook entry."""

    date: str = field(default_factory=lambda: date.today().isoformat())
    author: str = "Human Researcher"
    version: str = "v1"
    category: str = "General"
    title: str = "Untitled Research Note"
    hypothesis: str = ""
    experiment: str = ""
    result: str = ""
    conclusion: str = ""
    related_knowledge: list[str] = field(default_factory=list)
    related_experiment: str = ""

    def __post_init__(self) -> None:
        if self.category not in CATEGORIES:
            self.category = "General"

    @property
    def entry_id(self) -> str:
        slug = "".join(char.lower() if char.isalnum() else "-" for char in self.title).strip("-")
        return f"{self.date}-{slug or 'research-note'}"

    def metadata(self) -> dict[str, Any]:
        return {
            "entry_id": self.entry_id,
            "date": self.date,
            "author": self.author,
            "version": self.version,
            "category": self.category,
            "title": self.title,
            "hypothesis": self.hypothesis,
            "experiment": self.experiment,
            "result": self.result,
            "conclusion": self.conclusion,
            "related_knowledge": self.related_knowledge,
            "related_experiment": self.related_experiment,
            "status": self.status(),
        }

    def markdown(self) -> str:
        knowledge = ", ".join(self.related_knowledge) if self.related_knowledge else "None"
        return "\n".join(
            [
                f"## {self.title}",
                "",
                f"- Date: {self.date}",
                f"- Author: {self.author}",
                f"- Version: {self.version}",
                f"- Category: {self.category}",
                f"- Related Knowledge: {knowledge}",
                f"- Related Experiment: {self.related_experiment or 'None'}",
                "",
                "### Hypothesis",
                "",
                self.hypothesis or "TBD",
                "",
                "### Experiment",
                "",
                self.experiment or "TBD",
                "",
                "### Result",
                "",
                self.result or "TBD",
                "",
                "### Conclusion",
                "",
                self.conclusion or "TBD",
                "",
            ]
        )

    def status(self) -> str:
        if self.conclusion:
            return "Concluded"
        if self.result:
            return "Observed"
        if self.experiment:
            return "Running"
        if self.hypothesis:
            return "Proposed"
        return "Draft"

