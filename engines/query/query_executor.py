from typing import Any

from api.services.compass_data import (
    get_companies,
    get_company,
    get_discovery,
    get_learning,
    get_market,
    get_market_sectors,
    get_notifications,
    get_proposals,
    get_score,
    get_scores,
    get_top_discovery,
    get_validation,
    get_validation_for_ticker,
)
from api.services.data_loader import list_json_files, read_json, read_text
from engines.query.query_parser import QueryRequest


class QueryExecutor:
    """Executes normalized Compass queries across API-facing data sources."""

    def execute(self, request: QueryRequest) -> Any:
        handler = getattr(self, f"_execute_{request.intent}", None)
        if handler is None:
            raise ValueError(f"No executor for query intent: {request.intent}")
        return handler(**request.params)

    def _execute_companies(self, **kwargs: Any) -> list[dict[str, Any]]:
        return get_companies()

    def _execute_scores(self, **kwargs: Any) -> dict[str, Any]:
        return get_scores()

    def _execute_discovery(self, **kwargs: Any) -> dict[str, Any]:
        return get_discovery()

    def _execute_validation(self, **kwargs: Any) -> list[dict[str, Any]]:
        return get_validation()

    def _execute_market(self, **kwargs: Any) -> dict[str, Any]:
        return get_market()

    def _execute_sectors(self, **kwargs: Any) -> list[dict[str, Any]]:
        return get_market_sectors()

    def _execute_memory(self, **kwargs: Any) -> dict[str, Any]:
        return {
            "companies": [path.stem for path in list_json_files("memory/companies")],
            "sectors": [path.stem for path in list_json_files("memory/sectors")],
            "discoveries": [path.stem for path in list_json_files("memory/discoveries")],
            "validations": [path.stem for path in list_json_files("memory/validations")],
            "market": [path.stem for path in list_json_files("memory/market")],
            "learning": read_json("memory/learning/learning_history.json", []),
        }

    def _execute_feedback(self, **kwargs: Any) -> dict[str, Any]:
        return {
            "summary_markdown": read_text("reports/feedback/feedback_summary.md"),
            "improvement_candidates_markdown": read_text("reports/feedback/improvement_candidates.md"),
            "history": read_json("reports/feedback/feedback_history.json", []),
        }

    def _execute_learning(self, **kwargs: Any) -> dict[str, Any]:
        return get_learning()

    def _execute_notifications(self, limit: int = 50, **kwargs: Any) -> list[dict[str, Any]]:
        return get_notifications()[-max(1, int(limit)):]

    def _execute_top_discovery(self, limit: int = 3, **kwargs: Any) -> list[dict[str, Any]]:
        return get_top_discovery(limit=max(1, int(limit)))

    def _execute_top_score(self, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        scores = get_scores()
        results = scores.get("results", []) if isinstance(scores, dict) else []
        if not isinstance(results, list):
            return []
        return sorted(results, key=lambda item: item.get("total_score", 0), reverse=True)[: max(1, int(limit))]

    def _execute_latest_validation(self, ticker: str | None = None, limit: int = 20, **kwargs: Any) -> list[dict[str, Any]]:
        rows = get_validation_for_ticker(ticker) if ticker else get_validation()
        return sorted(rows, key=lambda row: str(row.get("validation_date", "")), reverse=True)[: max(1, int(limit))]

    def _execute_latest_proposal(self, **kwargs: Any) -> dict[str, Any]:
        proposals = get_proposals()
        if not proposals:
            return {}
        latest = sorted(proposals, key=lambda row: str(row.get("updated") or row.get("created") or ""), reverse=True)[0]
        created = str(latest.get("created", ""))[:10]
        return {
            "proposal": latest,
            "proposal_markdown": read_text(f"reports/proposals/proposal_{created}.md") if created else "",
        }

    def _execute_market_summary(self, **kwargs: Any) -> dict[str, Any]:
        return {
            "market": get_market(),
            "summary_markdown": read_text("reports/market/market_summary.md"),
            "notifications": get_notifications()[-10:],
        }

    def _execute_sector_summary(self, **kwargs: Any) -> dict[str, Any]:
        return {
            "sectors": get_market_sectors(),
            "summary_markdown": read_text("reports/market/sector_summary.md"),
        }

    def _execute_company_history(self, ticker: str, **kwargs: Any) -> dict[str, Any]:
        target = ticker.upper().strip()
        return {
            "ticker": target,
            "company": get_company(target),
            "memory": read_json(f"memory/companies/{target}.json", {}),
            "feedback": read_json("reports/feedback/feedback_history.json", []),
            "learning": get_learning(),
        }

    def _execute_company_score(self, ticker: str, **kwargs: Any) -> dict[str, Any] | None:
        return get_score(ticker)

    def _execute_company_discovery(self, ticker: str, **kwargs: Any) -> dict[str, Any]:
        target = ticker.upper().strip()
        discovery = get_discovery()
        candidates = discovery.get("candidates", []) if isinstance(discovery, dict) else []
        match = None
        if isinstance(candidates, list):
            match = next((item for item in candidates if str(item.get("ticker", "")).upper() == target), None)
        return {
            "ticker": target,
            "discovery": match,
            "discovery_memory": read_json(f"memory/discoveries/{discovery.get('generated_at', '')[:10]}.json", {}) if isinstance(discovery, dict) else {},
        }

    def _execute_company_validation(self, ticker: str, **kwargs: Any) -> list[dict[str, Any]]:
        return get_validation_for_ticker(ticker)
