from __future__ import annotations

from typing import Any


REQUIRED_METADATA_FIELDS = (
    "ticker",
    "company_name",
    "filing_type",
    "filing_date",
    "accession_number",
    "source_url",
    "document_title",
)


class SECNormalizer:
    """Normalizes SEC filing rows into Compass metadata."""

    def normalize(self, ticker: str, company_name: str, cik: str, row: dict[str, Any], source_url: str) -> dict[str, Any]:
        document = row.get("primaryDocument") or ""
        description = row.get("primaryDocDescription") or document or row.get("form")
        return {
            "ticker": ticker.upper(),
            "company_name": company_name,
            "cik": str(cik).zfill(10),
            "filing_type": row.get("form"),
            "filing_date": row.get("filingDate"),
            "report_date": row.get("reportDate"),
            "accession_number": row.get("accessionNumber"),
            "source_url": source_url,
            "document_title": description,
            "primary_document": document,
            "acceptance_datetime": row.get("acceptanceDateTime"),
            "items": row.get("items"),
            "size": row.get("size"),
            "is_xbrl": row.get("isXBRL"),
            "is_inline_xbrl": row.get("isInlineXBRL"),
        }

    def validate(self, metadata: dict[str, Any]) -> tuple[bool, list[str]]:
        missing = [field for field in REQUIRED_METADATA_FIELDS if not metadata.get(field)]
        return not missing, missing
