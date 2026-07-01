from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class TranscriptIndex:
    """Maintains per-company earnings transcript index files."""

    def __init__(self, company_dir: Path) -> None:
        self.company_dir = company_dir
        self.path = company_dir / "index.json"

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"ticker": self.company_dir.name.upper(), "transcripts": []}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {"ticker": self.company_dir.name.upper(), "transcripts": []}

    def exists(self, transcript_id: str) -> bool:
        return any(row.get("transcript_id") == transcript_id for row in self.load().get("transcripts", []))

    def update(self, ticker: str, metadata_rows: list[dict[str, Any]]) -> Path:
        existing = self.load()
        by_id = {row.get("transcript_id"): row for row in existing.get("transcripts", []) if row.get("transcript_id")}
        for metadata in metadata_rows:
            transcript_id = metadata["transcript_id"]
            by_id[transcript_id] = {
                "transcript_id": transcript_id,
                "fiscal_quarter": metadata["fiscal_quarter"],
                "earnings_date": metadata["earnings_date"],
                "transcript_date": metadata["transcript_date"],
                "source": metadata["source"],
                "language": metadata["language"],
            }
        rows = sorted(by_id.values(), key=lambda row: row.get("earnings_date") or "", reverse=True)
        payload = {"ticker": ticker.upper(), "transcripts": rows}
        self.company_dir.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        json.loads(self.path.read_text(encoding="utf-8"))
        return self.path
