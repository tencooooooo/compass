from typing import Any

from agents.providers.base_provider import BaseProvider


class ClaudeProvider(BaseProvider):
    """Placeholder for a future Claude-backed provider."""

    name = "claude"

    def generate(self, prompt: str, context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError("ClaudeProvider is a placeholder. Use DummyProvider for current local runs.")
