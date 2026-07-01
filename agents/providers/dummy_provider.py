from typing import Any

from agents.providers.base_provider import BaseProvider


class DummyProvider(BaseProvider):
    """Deterministic provider for local tests and model-independent development."""

    name = "dummy"

    def generate(self, prompt: str, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "provider": self.name,
            "summary": "Dummy provider returned normalized Compass context without model inference.",
            "prompt_preview": prompt[:500],
            "context_keys": sorted(context.keys()),
            "context": context,
        }
