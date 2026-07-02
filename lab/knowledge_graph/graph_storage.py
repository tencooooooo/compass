from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT


class GraphStorage:
    """Persists Compass Knowledge Graph files."""

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.storage_dir = repo_root / "storage" / "knowledge_graph"

    def save(self, graph: dict[str, Any]) -> dict[str, str]:
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "graph": self.storage_dir / "graph.json",
            "nodes": self.storage_dir / "nodes.json",
            "edges": self.storage_dir / "edges.json",
        }
        files["graph"].write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
        files["nodes"].write_text(json.dumps(graph.get("nodes", []), ensure_ascii=False, indent=2), encoding="utf-8")
        files["edges"].write_text(json.dumps(graph.get("edges", []), ensure_ascii=False, indent=2), encoding="utf-8")
        return {name: str(path.relative_to(self.repo_root)) for name, path in files.items()}

    def load(self) -> dict[str, Any]:
        path = self.storage_dir / "graph.json"
        if not path.exists():
            return {"nodes": [], "edges": [], "metadata": {}}
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {"nodes": [], "edges": [], "metadata": {}}
        return data if isinstance(data, dict) else {"nodes": [], "edges": [], "metadata": {}}

