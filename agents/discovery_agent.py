from typing import Any

from agents.base_agent import BaseAgent


class DiscoveryAgent(BaseAgent):
    """Prepares Discovery candidates, evidence, and confidence context."""

    agent_name = "discovery"

    def load_data(self, **kwargs: Any) -> dict[str, Any]:
        limit = int(kwargs.get("limit", 10))
        return self.context_builder.discovery_context(limit=limit)

    def prepare_context(self, data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
        top = data.get("top_discovery", [])
        candidates = []
        for candidate in top if isinstance(top, list) else []:
            candidates.append(
                {
                    "ticker": candidate.get("ticker"),
                    "company": candidate.get("company"),
                    "sector": candidate.get("sector"),
                    "discovery_score": candidate.get("discovery_score"),
                    "confidence": candidate.get("confidence"),
                    "reasons": candidate.get("discovery_reasons", []),
                    "evidence": candidate.get("evidence", []),
                }
            )
        return {
            "candidates": candidates,
            "proposals": data.get("proposals", []),
            "knowledge": data.get("knowledge", {}),
        }
