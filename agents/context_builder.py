from pathlib import Path
from typing import Any

from api.services.compass_data import (
    get_company,
    get_discovery,
    get_learning,
    get_market,
    get_market_sectors,
    get_notifications,
    get_proposals,
    get_score,
    get_top_discovery,
    get_validation_for_ticker,
)


class ContextBuilder:
    """Builds normalized context for model-independent Compass agents."""

    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or Path(__file__).resolve().parents[1]

    def knowledge(self, names: list[str] | None = None) -> dict[str, str]:
        knowledge_root = self.repo_root / "knowledge"
        if names is None:
            names = ["api_design.md", "agent_architecture.md", "context_design.md", "provider_design.md"]
        items: dict[str, str] = {}
        for name in names:
            path = knowledge_root / name
            if path.exists():
                items[name] = path.read_text(encoding="utf-8")
        return items

    def report(self, relative_path: str) -> str:
        path = self.repo_root / relative_path
        if not path.exists():
            return ""
        return path.read_text(encoding="utf-8")

    def company_context(self, ticker: str) -> dict[str, Any]:
        return {
            "company": get_company(ticker),
            "score": get_score(ticker),
            "validation": get_validation_for_ticker(ticker),
            "knowledge": self.knowledge(),
        }

    def discovery_context(self, limit: int = 10) -> dict[str, Any]:
        return {
            "discovery": get_discovery(),
            "top_discovery": get_top_discovery(limit),
            "proposals": get_proposals(),
            "knowledge": self.knowledge(),
        }

    def market_context(self) -> dict[str, Any]:
        return {
            "market": get_market(),
            "sectors": get_market_sectors(),
            "notifications": get_notifications(),
            "knowledge": self.knowledge(),
        }

    def learning_context(self) -> dict[str, Any]:
        return {
            "learning": get_learning(),
            "proposals": get_proposals(),
            "knowledge": self.knowledge(),
        }
