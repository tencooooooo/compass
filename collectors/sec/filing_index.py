from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class FilingIndex:
    """Maintains per-company SEC filing index files."""

    def __init__(self, company_dir: Path) -> None:
        self.company_dir = company_dir
        self.path = company_dir / "index.json"

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"ticker": self.company_dir.name.upper(), "filings": []}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {"ticker": self.company_dir.name.upper(), "filings": []}

    def exists(self, accession_number: str) -> bool:
        return any(row.get("accession_number") == accession_number for row in self.load().get("filings", []))

    def update(self, ticker: str, metadata_rows: list[dict[str, Any]]) -> Path:
        existing = self.load()
        filings = existing.get("filings", [])
        by_accession = {row.get("accession_number"): row for row in filings if row.get("accession_number")}
        for metadata in metadata_rows:
            by_accession[metadata["accession_number"]] = {
                "type": metadata["filing_type"],
                "date": metadata["filing_date"],
                "accession_number": metadata["accession_number"],
                "source_url": metadata["source_url"],
                "document_title": metadata["document_title"],
            }
        sorted_rows = sorted(by_accession.values(), key=lambda row: row.get("date") or "", reverse=True)
        payload = {"ticker": ticker.upper(), "filings": sorted_rows}
        self.company_dir.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        json.loads(self.path.read_text(encoding="utf-8"))
        return self.path
