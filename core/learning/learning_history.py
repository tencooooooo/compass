from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_history(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data if isinstance(data, list) else []


def save_history(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")


def append_learning_rows(path: Path, proposals: list[dict[str, Any]], applied_date: str, knowledge_version: str) -> list[dict[str, Any]]:
    history = load_history(path)
    seen = {row.get("proposal_id") for row in history}
    for proposal in proposals:
        proposal_id = proposal.get("proposal_id")
        if proposal_id in seen:
            continue
        history.append(
            {
                "proposal_id": proposal_id,
                "applied_date": applied_date,
                "target": proposal.get("target"),
                "reviewer": proposal.get("reviewer", ""),
                "reason": proposal.get("title", ""),
                "knowledge_version": knowledge_version,
            }
        )
    save_history(path, history)
    return history
