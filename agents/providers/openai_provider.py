from typing import Any

from agents.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """Placeholder for a future OpenAI-backed provider."""

    name = "openai"

    def generate(self, prompt: str, context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError("OpenAIProvider is a placeholder. Use DummyProvider for current local runs.")
