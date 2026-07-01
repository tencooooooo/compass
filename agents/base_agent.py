from abc import ABC, abstractmethod
from typing import Any

from agents.context_builder import ContextBuilder
from agents.prompt_manager import PromptManager
from agents.providers.base_provider import BaseProvider
from agents.providers.dummy_provider import DummyProvider


class BaseAgent(ABC):
    """Base interface for Compass agents.

    Agents organize Compass API data for AI providers. They do not own analysis
    rules and they do not write Knowledge, Memory, or generated reports.
    """

    agent_name = "base"

    def __init__(
        self,
        provider: BaseProvider | None = None,
        context_builder: ContextBuilder | None = None,
        prompt_manager: PromptManager | None = None,
    ):
        self.provider = provider or DummyProvider()
        self.context_builder = context_builder or ContextBuilder()
        self.prompt_manager = prompt_manager or PromptManager()

    def run(self, **kwargs: Any) -> dict[str, Any]:
        data = self.load_data(**kwargs)
        context = self.prepare_context(data, **kwargs)
        prompt = self.build_prompt(context, **kwargs)
        raw_response = self.provider.generate(prompt, context)
        return self.format_response(raw_response, context, **kwargs)

    @abstractmethod
    def load_data(self, **kwargs: Any) -> dict[str, Any]:
        """Load Compass data through API-facing services."""

    def prepare_context(self, data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
        return data

    def build_prompt(self, context: dict[str, Any], **kwargs: Any) -> str:
        return self.prompt_manager.build_agent_prompt(
            agent_name=self.agent_name,
            task=str(kwargs.get("task", "Summarize Compass context for human review.")),
            context_summary=", ".join(sorted(context.keys())),
        )

    def format_response(self, raw_response: dict[str, Any], context: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
        return {
            "agent": self.agent_name,
            "provider": self.provider.name,
            "response": raw_response,
            "context": context,
        }
