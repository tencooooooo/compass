from abc import ABC, abstractmethod
from typing import Any


class BaseProvider(ABC):
    """Interface for AI model providers used by Compass agents."""

    name = "base"

    @abstractmethod
    def generate(self, prompt: str, context: dict[str, Any]) -> dict[str, Any]:
        """Generate a response from a prompt and normalized Compass context."""
