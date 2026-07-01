from __future__ import annotations

import json
from pathlib import Path
from typing import Any


APPROVED_STATUS = "Approved"


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_proposal_index(index_path: Path) -> list[dict[str, Any]]:
    data = load_json(index_path, [])
    return data if isinstance(data, list) else []


def approved_proposals(index_path: Path) -> list[dict[str, Any]]:
    return [proposal for proposal in load_proposal_index(index_path) if proposal.get("status") == APPROVED_STATUS]


def proposal_status_counts(index_path: Path) -> dict[str, int]:
    proposals = load_proposal_index(index_path)
    counts = {"Approved": 0, "Rejected": 0, "Deferred": 0, "Pending": 0}
    for proposal in proposals:
        status = proposal.get("status")
        if status in counts:
            counts[status] += 1
    return counts


def proposal_markdown_by_id(proposal_dir: Path, proposal_id: str) -> str:
    if not proposal_dir.exists():
        return ""
    for path in sorted(proposal_dir.glob("proposal_*.md"), reverse=True):
        text = path.read_text(encoding="utf-8")
        if proposal_id in text:
            return text
    return ""


def related_knowledge_candidate(knowledge_update_dir: Path, proposal_id: str) -> str:
    if not knowledge_update_dir.exists():
        return ""
    for path in sorted(knowledge_update_dir.glob("candidate_*.md"), reverse=True):
        text = path.read_text(encoding="utf-8")
        if proposal_id in text:
            return text
    return ""
