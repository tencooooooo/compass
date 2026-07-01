from typing import Any

from agents.base_agent import BaseAgent


class MarketAgent(BaseAgent):
    """Prepares market intelligence and sector analysis context."""

    agent_name = "market"

    def load_data(self, **kwargs: Any) -> dict[str, Any]:
        return self.context_builder.market_context()

    def prepare_context(self, data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
        market = data.get("market", {})
        return {
            "market": market.get("market", {}) if isinstance(market, dict) else {},
            "sectors": data.get("sectors", []),
            "top_events": market.get("top_events", []) if isinstance(market, dict) else [],
            "notifications": data.get("notifications", [])[-10:],
            "knowledge": data.get("knowledge", {}),
        }
