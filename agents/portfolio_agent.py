from typing import Any

from agents.base_agent import BaseAgent


class PortfolioAgent(BaseAgent):
    """Placeholder for future portfolio context.

    Portfolio decisions are not implemented. This agent only exposes the
    current learning and proposal context for future design work.
    """

    agent_name = "portfolio"

    def load_data(self, **kwargs: Any) -> dict[str, Any]:
        return self.context_builder.learning_context()

    def prepare_context(self, data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
        return {
            "status": "placeholder",
            "message": "Portfolio Agent is reserved for future implementation.",
            "learning": data.get("learning", {}),
            "proposals": data.get("proposals", []),
            "knowledge": data.get("knowledge", {}),
        }
