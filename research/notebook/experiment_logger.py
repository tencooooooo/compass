from __future__ import annotations

from typing import Any

from research.notebook.notebook_engine import Notebook
from research.notebook.notebook_entry import NotebookEntry


class ExperimentLogger:
    """Creates Notebook entries from experiment review context."""

    def log(self, experiment: dict[str, Any], author: str = "Human Researcher") -> dict[str, Any]:
        entry = NotebookEntry(
            author=author,
            version=str(experiment.get("candidate_version") or experiment.get("version") or "v1"),
            category="Experiment",
            title=f"Experiment Review: {experiment.get('experiment_id', 'Unknown')}",
            hypothesis=str(experiment.get("description") or experiment.get("hypothesis") or ""),
            experiment=str(experiment.get("name") or experiment.get("target") or ""),
            result=str(experiment.get("winner_reason") or experiment.get("result") or ""),
            conclusion=str(experiment.get("winner") or experiment.get("conclusion") or ""),
            related_experiment=str(experiment.get("experiment_id") or ""),
        )
        return Notebook.save(entry)

