from pathlib import Path
from typing import Any

from engines.query.query_engine import Query


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
        company_history = Query.run("Company History", ticker=ticker).get("data", {})
        return {
            "company": company_history.get("company") if isinstance(company_history, dict) else None,
            "score": Query.run("Company Score", ticker=ticker).get("data"),
            "validation": Query.run("Company Validation", ticker=ticker).get("data"),
            "knowledge": self.knowledge(),
        }

    def discovery_context(self, limit: int = 10) -> dict[str, Any]:
        return {
            "discovery": Query.run("Discovery").get("data"),
            "top_discovery": Query.run("Top Discovery", limit=limit).get("data"),
            "proposals": Query.run("Latest Proposal").get("data"),
            "knowledge": self.knowledge(),
        }

    def market_context(self) -> dict[str, Any]:
        market_summary = Query.run("Market Summary").get("data", {})
        sector_summary = Query.run("Sector Summary").get("data", {})
        return {
            "market": market_summary.get("market") if isinstance(market_summary, dict) else {},
            "sectors": sector_summary.get("sectors", []) if isinstance(sector_summary, dict) else [],
            "notifications": Query.run("Notifications").get("data"),
            "knowledge": self.knowledge(),
        }

    def learning_context(self) -> dict[str, Any]:
        return {
            "learning": Query.run("Learning").get("data"),
            "proposals": Query.run("Latest Proposal").get("data"),
            "knowledge": self.knowledge(),
        }
