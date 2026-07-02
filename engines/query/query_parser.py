from dataclasses import dataclass, field
from typing import Any


SUPPORTED_QUERIES = {
    "companies": "companies",
    "scores": "scores",
    "discovery": "discovery",
    "validation": "validation",
    "market": "market",
    "sectors": "sectors",
    "memory": "memory",
    "feedback": "feedback",
    "learning": "learning",
    "notifications": "notifications",
    "top discovery": "top_discovery",
    "top score": "top_score",
    "latest validation": "latest_validation",
    "latest proposal": "latest_proposal",
    "market summary": "market_summary",
    "sector summary": "sector_summary",
    "company history": "company_history",
    "company score": "company_score",
    "company discovery": "company_discovery",
    "company validation": "company_validation",
    "knowledge graph": "knowledge_graph",
    "graph related": "graph_related",
    "graph theme": "graph_theme",
    "graph path": "graph_path",
}


@dataclass(frozen=True)
class QueryRequest:
    query: str
    intent: str
    params: dict[str, Any] = field(default_factory=dict)


class QueryParser:
    """Parses supported Compass query labels into executor intents."""

    def parse(self, query: str, **params: Any) -> QueryRequest:
        normalized = " ".join(query.lower().replace("_", " ").split())
        intent = SUPPORTED_QUERIES.get(normalized)
        if intent is None:
            supported = ", ".join(sorted(SUPPORTED_QUERIES.keys()))
            raise ValueError(f"Unsupported query: {query}. Supported queries: {supported}")
        return QueryRequest(query=query, intent=intent, params=params)
