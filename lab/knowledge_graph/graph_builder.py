from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT, list_json_files, read_json
from lab.theme_intelligence.theme_classifier import ThemeClassifier


RELATIONSHIPS = {
    "BELONGS_TO",
    "RELATED_TO",
    "SUPPLIES",
    "COMPETES_WITH",
    "PARTNERS_WITH",
    "USES",
    "INVESTS_IN",
    "ACQUIRES",
}

TECHNOLOGY_KEYWORDS = {
    "AI": ["ai", "artificial intelligence", "machine learning"],
    "GPU": ["gpu", "accelerator"],
    "Cloud": ["cloud", "data center"],
    "Cybersecurity": ["cybersecurity", "security"],
    "Robotics": ["robotics", "autonomous"],
    "EV Battery": ["battery", "electric vehicle"],
    "Quantum Computing": ["quantum"],
}

PRODUCT_KEYWORDS = {
    "NVIDIA GPU": ["nvidia gpu", "geforce", "rtx"],
    "iPhone": ["iphone"],
    "Azure": ["azure"],
    "AWS": ["aws"],
    "Google Cloud": ["google cloud"],
    "Tesla EV": ["tesla", "electric vehicle"],
}


class GraphBuilder:
    """Builds a local Compass Knowledge Graph from existing data artifacts."""

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.nodes: dict[str, dict[str, Any]] = {}
        self.edges: dict[str, dict[str, Any]] = {}

    def build(self) -> dict[str, Any]:
        companies = self._companies()
        themes = ThemeClassifier().classify()
        self._company_nodes(companies)
        self._theme_nodes(themes)
        self._theme_edges(themes)
        self._news_and_event_edges(companies)
        self._competitive_edges(companies, themes)
        self._theme_similarity_edges(themes)
        return {
            "metadata": {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "node_count": len(self.nodes),
                "edge_count": len(self.edges),
                "relationships": sorted(RELATIONSHIPS),
            },
            "nodes": sorted(self.nodes.values(), key=lambda row: (row["type"], row["id"])),
            "edges": sorted(self.edges.values(), key=lambda row: (row["source"], row["relationship"], row["target"])),
        }

    def _companies(self) -> dict[str, dict[str, Any]]:
        output = {}
        for path in list_json_files("storage/raw/companies"):
            data = read_json(f"storage/raw/companies/{path.name}", {})
            ticker = (data.get("ticker") or path.stem).upper()
            output[ticker] = data
        return output

    def _company_nodes(self, companies: dict[str, dict[str, Any]]) -> None:
        for ticker, company in companies.items():
            text = self._company_text(company, read_json(f"storage/raw/news/{ticker}.json", []))
            self._node(ticker, "Company", company.get("company_name") or ticker, sector=company.get("sector"), industry=company.get("industry"))
            sector = company.get("sector")
            if sector:
                self._node(sector, "Sector", sector)
                self._edge(ticker, sector, "BELONGS_TO", "Company profile sector")
            country = company.get("country")
            if country:
                self._node(country, "Country", country)
                self._edge(ticker, country, "BELONGS_TO", "Company profile country")
            ceo = company.get("ceo_name") or company.get("ceo") or company.get("chief_executive_officer")
            if ceo:
                self._node(str(ceo), "CEO", str(ceo))
                self._edge(ticker, str(ceo), "RELATED_TO", "Company profile CEO")
            for technology, keywords in TECHNOLOGY_KEYWORDS.items():
                if self._contains_any(text, keywords):
                    self._node(technology, "Technology", technology)
                    self._edge(ticker, technology, "USES", "Company profile or news keyword match")
            for product, keywords in PRODUCT_KEYWORDS.items():
                if self._contains_any(text, keywords):
                    self._node(product, "Product", product)
                    self._edge(ticker, product, "USES", "Product keyword match")

    def _theme_nodes(self, themes: dict[str, Any]) -> None:
        for theme in themes:
            self._node(theme, "Theme", theme)

    def _theme_edges(self, themes: dict[str, Any]) -> None:
        for theme, item in themes.items():
            for company in item.get("companies", []):
                ticker = company.get("ticker")
                if ticker:
                    self._edge(ticker, theme, "BELONGS_TO", "; ".join(company.get("evidence", [])) or "Theme classification")

    def _news_and_event_edges(self, companies: dict[str, dict[str, Any]]) -> None:
        for ticker in companies:
            for item in read_json(f"storage/raw/news/{ticker}.json", [])[:20]:
                if not isinstance(item, dict):
                    continue
                event_id = self._event_id(ticker, item)
                title = item.get("title") or event_id
                text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
                self._node(event_id, "Event", title, ticker=ticker, published_at=item.get("published_at"), publisher=item.get("publisher"))
                self._edge(ticker, event_id, "RELATED_TO", "News item")
                if "etf" in text:
                    self._node("ETF", "ETF", "ETF")
                    self._edge(event_id, "ETF", "RELATED_TO", "ETF keyword")
                self._relationship_from_text(ticker, text)
            for item in read_json(f"storage/events/{ticker}_events.json", [])[:20]:
                if not isinstance(item, dict):
                    continue
                label = item.get("event_type") or item.get("title") or "Event"
                event_id = f"event:{ticker}:{self._slug(label)}"
                self._node(event_id, "Event", label, ticker=ticker)
                self._edge(ticker, event_id, "RELATED_TO", "Event database")

    def _competitive_edges(self, companies: dict[str, dict[str, Any]], themes: dict[str, Any]) -> None:
        by_sector: dict[str, list[str]] = {}
        for ticker, company in companies.items():
            by_sector.setdefault(company.get("sector") or "Unknown", []).append(ticker)
        for tickers in by_sector.values():
            self._pair_edges(tickers[:8], "COMPETES_WITH", "Same sector")
        for item in themes.values():
            tickers = [company.get("ticker") for company in item.get("companies", []) if company.get("ticker")]
            self._pair_edges(tickers[:8], "COMPETES_WITH", "Same theme")

    def _theme_similarity_edges(self, themes: dict[str, Any]) -> None:
        theme_companies = {
            theme: {company.get("ticker") for company in item.get("companies", []) if company.get("ticker")}
            for theme, item in themes.items()
        }
        names = sorted(theme_companies)
        for index, left in enumerate(names):
            for right in names[index + 1 :]:
                union = theme_companies[left] | theme_companies[right]
                if not union:
                    continue
                score = len(theme_companies[left] & theme_companies[right]) / len(union)
                if score >= 0.3:
                    self._edge(left, right, "RELATED_TO", f"Shared company overlap {score:.2f}", weight=round(score, 3))

    def _relationship_from_text(self, ticker: str, text: str) -> None:
        if re.search(r"\b(partner|partnership|alliance)\b", text):
            self._edge(ticker, "Partnership Event", "PARTNERS_WITH", "Partnership keyword in news")
            self._node("Partnership Event", "Event", "Partnership Event")
        if re.search(r"\b(acquire|acquires|acquisition)\b", text):
            self._edge(ticker, "Acquisition Event", "ACQUIRES", "Acquisition keyword in news")
            self._node("Acquisition Event", "Event", "Acquisition Event")
        if re.search(r"\b(invests|investment|investing)\b", text):
            self._edge(ticker, "Investment Event", "INVESTS_IN", "Investment keyword in news")
            self._node("Investment Event", "Event", "Investment Event")
        if re.search(r"\b(supplier|supplies|supply)\b", text):
            self._edge(ticker, "Supply Chain Event", "SUPPLIES", "Supply keyword in news")
            self._node("Supply Chain Event", "Event", "Supply Chain Event")

    def _pair_edges(self, tickers: list[str], relationship: str, evidence: str) -> None:
        for index, left in enumerate(tickers):
            for right in tickers[index + 1 :]:
                self._edge(left, right, relationship, evidence, bidirectional=True)

    def _node(self, node_id: str, node_type: str, label: str, **properties: Any) -> None:
        if not node_id:
            return
        self.nodes.setdefault(
            node_id,
            {"id": node_id, "type": node_type, "label": label, "properties": {key: value for key, value in properties.items() if value is not None}},
        )

    def _edge(self, source: str, target: str, relationship: str, evidence: str, weight: float = 1.0, bidirectional: bool = False) -> None:
        if not source or not target or source == target or relationship not in RELATIONSHIPS:
            return
        edge_id = f"{source}|{relationship}|{target}"
        self.edges.setdefault(edge_id, {"source": source, "target": target, "relationship": relationship, "weight": weight, "evidence": evidence})
        if bidirectional:
            reverse_id = f"{target}|{relationship}|{source}"
            self.edges.setdefault(reverse_id, {"source": target, "target": source, "relationship": relationship, "weight": weight, "evidence": evidence})

    def _company_text(self, company: dict[str, Any], news: Any) -> str:
        parts = [company.get("company_name"), company.get("sector"), company.get("industry"), company.get("business_summary")]
        if isinstance(news, list):
            for item in news[:20]:
                if isinstance(item, dict):
                    parts.extend([item.get("title"), item.get("summary")])
        return " ".join(str(part) for part in parts if part).lower()

    def _contains_any(self, text: str, keywords: list[str]) -> bool:
        return any(keyword.lower() in text for keyword in keywords)

    def _event_id(self, ticker: str, item: dict[str, Any]) -> str:
        return f"news:{ticker}:{self._slug(item.get('title') or item.get('url') or 'event')}"

    def _slug(self, value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", str(value).strip().lower()).strip("-")
        return slug[:80] or "event"
