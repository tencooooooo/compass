from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from api.services.data_loader import REPO_ROOT


class ExperimentRegistry:
    """Stores experiment definitions and registry results."""

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.config_path = repo_root / "config" / "experiments.yaml"
        self.registry_path = repo_root / "memory" / "experiments" / "registry.json"

    def definitions(self) -> list[dict[str, Any]]:
        if not self.config_path.exists():
            return []
        data = yaml.safe_load(self.config_path.read_text(encoding="utf-8")) or {}
        return data.get("experiments", [])

    def save_results(self, results: list[dict[str, Any]]) -> Path:
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)
        registry = self.load()
        by_id = {row.get("experiment_id"): row for row in registry if row.get("experiment_id")}
        for result in results:
            by_id[result["experiment_id"]] = {
                "experiment_id": result["experiment_id"],
                "version": result.get("candidate_version"),
                "status": result.get("status"),
                "metrics": result.get("candidate_metrics", {}),
                "winner": result.get("winner"),
                "updated_at": date.today().isoformat(),
            }
        rows = sorted(by_id.values(), key=lambda row: row.get("experiment_id", ""))
        self.registry_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
        return self.registry_path

    def load(self) -> list[dict[str, Any]]:
        if not self.registry_path.exists():
            return []
        try:
            data = json.loads(self.registry_path.read_text(encoding="utf-8"))
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []
