from __future__ import annotations

from typing import Any


RELIABILITY_LEVELS = {
    "sec": ("primary", 100),
    "earnings": ("primary", 95),
    "prices": ("market_data", 90),
    "companies": ("market_data", 85),
    "financials": ("market_data", 85),
    "macro": ("official_or_provider", 85),
    "etf": ("provider", 80),
    "insider": ("provider", 80),
    "analyst": ("secondary", 70),
    "news": ("secondary", 70),
    "events": ("derived", 65),
    "trends": ("estimated", 60),
}


class ReliabilityScorer:
    """Assigns source reliability by provider category."""

    def score(self, provider: str) -> dict[str, Any]:
        source_type, score = RELIABILITY_LEVELS.get(provider, ("future_provider", 50))
        return {"score": score, "source_type": source_type}

