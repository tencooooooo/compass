from __future__ import annotations

from typing import Any


SUPPORTED_FORMS = ("10-K", "10-Q", "8-K")
FUTURE_FORMS = ("DEF 14A", "S-1", "Form 4")


class SECParser:
    """Parses SEC submissions JSON into filing candidate rows."""

    def filings(self, submissions: dict[str, Any], forms: list[str], limit: int) -> list[dict[str, Any]]:
        recent = submissions.get("filings", {}).get("recent", {})
        rows = self._zip_recent(recent)
        filtered = [row for row in rows if row.get("form") in forms]
        filtered.sort(key=lambda row: row.get("filingDate") or "", reverse=True)
        counts = {form: 0 for form in forms}
        output = []
        for row in filtered:
            form = row["form"]
            if counts[form] >= limit:
                continue
            output.append(row)
            counts[form] += 1
        return output

    def _zip_recent(self, recent: dict[str, Any]) -> list[dict[str, Any]]:
        keys = [
            "accessionNumber",
            "filingDate",
            "reportDate",
            "acceptanceDateTime",
            "act",
            "form",
            "fileNumber",
            "filmNumber",
            "items",
            "size",
            "isXBRL",
            "isInlineXBRL",
            "primaryDocument",
            "primaryDocDescription",
        ]
        length = len(recent.get("accessionNumber", []))
        rows = []
        for index in range(length):
            rows.append({key: self._value(recent.get(key, []), index) for key in keys})
        return rows

    def _value(self, values: Any, index: int) -> Any:
        if isinstance(values, list) and index < len(values):
            return values[index]
        return None
