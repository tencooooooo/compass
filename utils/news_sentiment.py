from __future__ import annotations

import re
from typing import Any


POSITIVE_PATTERNS = [
    r"beat(?:s|ing)?",
    r"record",
    r"strong",
    r"demand",
    r"growth",
    r"partnership",
    r"contract",
    r"launch(?:es|ed|ing)?",
    r"upgrade(?:s|d)?",
    r"profit(?:s|able|ability)?",
    r"\bai\b",
    r"buyback",
    r"cost cuts?",
    r"cuts? costs?",
    r"margin expansion",
    r"raises? guidance",
]

NEGATIVE_PATTERNS = [
    r"miss(?:es|ed|ing)?",
    r"lawsuit",
    r"probe",
    r"regulation",
    r"downgrade(?:s|d)?",
    r"weak(?:ness)?",
    r"falls?",
    r"risk(?:s)?",
    r"tariff(?:s)?",
    r"loss(?:es)?",
    r"guidance cuts?",
    r"cuts? guidance",
    r"profit warning",
    r"delay(?:s|ed)?",
]

NEGATIONS = {"no", "not", "without", "never"}


def _compile(pattern: str) -> re.Pattern[str]:
    return re.compile(rf"(?<![A-Za-z0-9])(?:{pattern})(?![A-Za-z0-9])", re.IGNORECASE)


COMPILED_POSITIVE = [_compile(pattern) for pattern in POSITIVE_PATTERNS]
COMPILED_NEGATIVE = [_compile(pattern) for pattern in NEGATIVE_PATTERNS]
TOKEN_PATTERN = re.compile(r"\b[\w']+\b", re.IGNORECASE)


def _has_negation_before(text: str, start: int, window: int = 3) -> bool:
    tokens = list(TOKEN_PATTERN.finditer(text[:start]))
    previous = [token.group(0).lower() for token in tokens[-window:]]
    return any(token in NEGATIONS for token in previous)


def _score_matches(text: str, patterns: list[re.Pattern[str]], direction: int) -> int:
    score = 0
    for pattern in patterns:
        for match in pattern.finditer(text):
            score += -direction if _has_negation_before(text, match.start()) else direction
    return score


def classify_text(text: str) -> str:
    normalized = " ".join(str(text or "").lower().split())
    if not normalized:
        return "neutral"
    score = _score_matches(normalized, COMPILED_POSITIVE, 1)
    score += _score_matches(normalized, COMPILED_NEGATIVE, -1)
    if score > 0:
        return "positive"
    if score < 0:
        return "negative"
    return "neutral"


def classify_news_item(item: dict[str, Any]) -> str:
    return classify_text(f"{item.get('title') or ''} {item.get('summary') or ''}")


def sentiment_counts(news_items: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"positive": 0, "negative": 0, "neutral": 0}
    for item in news_items:
        counts[classify_news_item(item)] += 1
    return counts
