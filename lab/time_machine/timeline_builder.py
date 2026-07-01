from typing import Any


class TimelineBuilder:
    """Builds a compact timeline from snapshot context."""

    def build(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        timeline = []
        for ticker, company_context in context.get("companies", {}).items():
            latest_price = company_context.get("latest_price") or {}
            timeline.append(
                {
                    "ticker": ticker,
                    "date": latest_price.get("date") or context.get("date"),
                    "score": company_context.get("historical_score", {}).get("total_score"),
                    "confidence": company_context.get("confidence"),
                    "news_count": company_context.get("news_count"),
                    "event_count": company_context.get("event_count"),
                }
            )
        return sorted(timeline, key=lambda item: (item.get("score") or 0), reverse=True)
