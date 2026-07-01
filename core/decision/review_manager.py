from __future__ import annotations

import json
from pathlib import Path
from typing import Any


VALID_STATUSES = {"Pending", "Approved", "Rejected", "Deferred"}


class ReviewManager:
    """Proposal indexをJSONで管理するReview管理層です。"""

    def __init__(self, index_path: Path):
        self.index_path = index_path

    def load_index(self) -> list[dict[str, Any]]:
        if not self.index_path.exists():
            return []
        with self.index_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []

    def save_index(self, proposals: list[dict[str, Any]]) -> None:
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        self.index_path.write_text(json.dumps(proposals, ensure_ascii=False, indent=2), encoding="utf-8")

    def upsert_pending(self, proposal: dict[str, Any]) -> None:
        proposals = self.load_index()
        proposal_id = proposal["proposal_id"]
        existing = next((item for item in proposals if item.get("proposal_id") == proposal_id), None)
        if existing:
            existing.update(
                {
                    "title": proposal["title"],
                    "target": proposal["target"],
                    "updated": proposal["updated"],
                    "source_feedback": proposal.get("source_feedback"),
                }
            )
        else:
            proposals.append(
                {
                    "proposal_id": proposal_id,
                    "title": proposal["title"],
                    "target": proposal["target"],
                    "status": "Pending",
                    "created": proposal["created"],
                    "updated": proposal["updated"],
                    "reviewer": "",
                    "source_feedback": proposal.get("source_feedback"),
                }
            )
        self.save_index(sorted(proposals, key=lambda item: item.get("created", "")))

    def update_status(self, proposal_id: str, status: str, reviewer: str = "", updated: str = "") -> dict[str, Any]:
        if status not in VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}")
        proposals = self.load_index()
        for proposal in proposals:
            if proposal.get("proposal_id") != proposal_id:
                continue
            proposal["status"] = status
            proposal["reviewer"] = reviewer
            if updated:
                proposal["updated"] = updated
            self.save_index(proposals)
            return proposal
        raise KeyError(f"Proposal not found: {proposal_id}")
