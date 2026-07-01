from __future__ import annotations

import re
from typing import Any


SECTION_NAMES = ("opening_remarks", "financial_highlights", "guidance", "qa_section", "closing_remarks")


class TranscriptParser:
    """Parses transcript text into paragraphs and coarse analysis-ready sections."""

    def parse(self, text: str) -> dict[str, Any]:
        paragraphs = self._paragraphs(text)
        sections = {name: [] for name in SECTION_NAMES}
        current = "opening_remarks"
        for paragraph in paragraphs:
            detected = self._detect_section(paragraph)
            if detected:
                current = detected
            sections[current].append(paragraph)
        if not sections["closing_remarks"] and paragraphs:
            sections["closing_remarks"] = paragraphs[-2:] if len(paragraphs) > 1 else paragraphs[-1:]
        return {"paragraphs": paragraphs, "sections": sections}

    def _paragraphs(self, text: str) -> list[str]:
        blocks = re.split(r"\n\s*\n+", text.strip())
        paragraphs = []
        for block in blocks:
            cleaned = re.sub(r"\s+", " ", block).strip()
            if cleaned:
                paragraphs.append(cleaned)
        if len(paragraphs) <= 1 and text.strip():
            paragraphs = [line.strip() for line in text.splitlines() if line.strip()]
        return paragraphs

    def _detect_section(self, paragraph: str) -> str | None:
        text = paragraph.lower()
        if any(token in text for token in ("question-and-answer", "question and answer", "q&a", "questions-and-answers")):
            return "qa_section"
        if any(token in text for token in ("guidance", "outlook", "forecast", "expects", "we expect")):
            return "guidance"
        if any(token in text for token in ("revenue", "gross margin", "operating income", "eps", "cash flow", "financial highlights")):
            return "financial_highlights"
        if any(token in text for token in ("closing remarks", "in closing", "to conclude", "thank you for joining")):
            return "closing_remarks"
        if any(token in text for token in ("prepared remarks", "opening remarks", "welcome", "good afternoon", "good morning")):
            return "opening_remarks"
        return None
