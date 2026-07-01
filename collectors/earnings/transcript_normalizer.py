from __future__ import annotations

from datetime import date
from typing import Any


REQUIRED_METADATA_FIELDS = (
    "ticker",
    "company_name",
    "fiscal_quarter",
    "earnings_date",
    "transcript_date",
    "source",
    "language",
    "participants",
    "ceo_name",
    "cfo_name",
)


class TranscriptNormalizer:
    """Normalizes transcript metadata and parsed body into Compass schema."""

    def normalize(
        self,
        ticker: str,
        parsed: dict[str, Any],
        metadata: dict[str, Any],
        source: str,
    ) -> dict[str, Any]:
        normalized_metadata = {
            "ticker": ticker.upper(),
            "company_name": metadata.get("company_name") or ticker.upper(),
            "fiscal_quarter": metadata.get("fiscal_quarter") or "Unknown",
            "earnings_date": metadata.get("earnings_date") or metadata.get("date") or date.today().isoformat(),
            "transcript_date": metadata.get("transcript_date") or date.today().isoformat(),
            "source": metadata.get("source") or source,
            "language": metadata.get("language") or "en",
            "participants": metadata.get("participants") or self._participants(parsed.get("paragraphs", [])),
            "ceo_name": metadata.get("ceo_name") or self._role_name(parsed.get("paragraphs", []), "ceo"),
            "cfo_name": metadata.get("cfo_name") or self._role_name(parsed.get("paragraphs", []), "cfo"),
        }
        return {
            "metadata": normalized_metadata,
            "transcript": {
                "paragraphs": parsed.get("paragraphs", []),
                "sections": parsed.get("sections", {}),
            },
        }

    def validate(self, payload: dict[str, Any]) -> tuple[bool, list[str]]:
        metadata = payload.get("metadata", {})
        transcript = payload.get("transcript", {})
        missing = [field for field in REQUIRED_METADATA_FIELDS if field not in metadata or metadata.get(field) in (None, "")]
        if not transcript.get("paragraphs"):
            missing.append("transcript.paragraphs")
        return not missing, missing

    def _participants(self, paragraphs: list[str]) -> list[str]:
        participants = []
        for paragraph in paragraphs[:20]:
            if " - " in paragraph and any(role in paragraph.lower() for role in ("ceo", "cfo", "operator", "analyst")):
                participant = paragraph.split(" - ", 1)[0].strip()
                if participant and participant not in participants:
                    participants.append(participant)
        return participants

    def _role_name(self, paragraphs: list[str], role: str) -> str:
        role_text = role.lower()
        for paragraph in paragraphs[:30]:
            lower = paragraph.lower()
            if role_text in lower and " - " in paragraph:
                return paragraph.split(" - ", 1)[0].strip()
        return "Unknown"
