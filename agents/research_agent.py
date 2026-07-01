from typing import Any

from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """Prepares company and comparison research context for AI providers."""

    agent_name = "research"

    def load_data(self, **kwargs: Any) -> dict[str, Any]:
        ticker = str(kwargs.get("ticker", "AAPL")).upper()
        comparison_report = str(kwargs.get("comparison_report", "reports/comparative_analysis/market_overview.md"))
        return {
            "ticker": ticker,
            "research": self.context_builder.company_context(ticker),
            "comparison_report": self.context_builder.report(comparison_report),
        }

    def prepare_context(self, data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
        research = data.get("research", {})
        company = research.get("company") if isinstance(research, dict) else {}
        profile = company.get("profile", {}) if isinstance(company, dict) else {}
        return {
            "ticker": data.get("ticker"),
            "company_name": profile.get("company_name"),
            "sector": profile.get("sector"),
            "company_report": company.get("report_markdown") if isinstance(company, dict) else "",
            "latest_score": research.get("score") if isinstance(research, dict) else None,
            "latest_validation": research.get("validation") if isinstance(research, dict) else [],
            "comparison_report": data.get("comparison_report", ""),
            "knowledge": research.get("knowledge") if isinstance(research, dict) else {},
        }
