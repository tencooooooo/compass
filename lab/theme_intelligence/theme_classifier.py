from pathlib import Path
import re
from typing import Any

import yaml

from api.services.data_loader import REPO_ROOT, list_json_files, read_json


class ThemeClassifier:
    """Classifies companies into one or more investment themes."""

    def __init__(self, config_path: Path | None = None) -> None:
        self.config_path = config_path or REPO_ROOT / "config" / "themes.yaml"
        self.themes = self._load_themes()

    def classify(self) -> dict[str, Any]:
        companies = self._companies()
        classified = {theme: {"definition": definition, "companies": []} for theme, definition in self.themes.items()}
        for ticker in sorted(companies):
            company = companies[ticker]
            news = read_json(f"storage/raw/news/{ticker}.json", [])
            text = self._company_text(company, news)
            sector = company.get("sector") or "Unknown"
            for theme, definition in self.themes.items():
                match = self._match_theme(text, sector, definition)
                if match["score"] <= 0:
                    continue
                classified[theme]["companies"].append(
                    {
                        "ticker": ticker,
                        "company_name": company.get("company_name") or ticker,
                        "sector": sector,
                        "industry": company.get("industry") or "Unknown",
                        "confidence": self._confidence(match["score"]),
                        "evidence": match["evidence"],
                    }
                )
        return classified

    def _load_themes(self) -> dict[str, dict[str, Any]]:
        if not self.config_path.exists():
            return {}
        data = yaml.safe_load(self.config_path.read_text(encoding="utf-8")) or {}
        themes = data.get("themes", {})
        return themes if isinstance(themes, dict) else {}

    def _companies(self) -> dict[str, dict[str, Any]]:
        output = {}
        for path in list_json_files("storage/raw/companies"):
            ticker = path.stem.upper()
            output[ticker] = read_json(f"storage/raw/companies/{path.name}", {})
        return output

    def _company_text(self, company: dict[str, Any], news: Any) -> str:
        parts = [
            company.get("ticker"),
            company.get("company_name"),
            company.get("sector"),
            company.get("industry"),
            company.get("business_summary"),
        ]
        if isinstance(news, list):
            for item in news[:20]:
                if isinstance(item, dict):
                    parts.extend([item.get("title"), item.get("summary")])
        return " ".join(str(part) for part in parts if part).lower()

    def _match_theme(self, text: str, sector: str, definition: dict[str, Any]) -> dict[str, Any]:
        evidence = []
        score = 0
        for keyword in definition.get("keywords", []):
            token = str(keyword).lower()
            if token and self._contains_keyword(text, token):
                evidence.append(f"Keyword: {keyword}")
                score += 2
        if not evidence:
            return {"score": 0, "evidence": []}
        if sector in definition.get("sectors", []):
            evidence.append(f"Sector alignment: {sector}")
            score += 1
        return {"score": score, "evidence": evidence[:6]}

    def _contains_keyword(self, text: str, keyword: str) -> bool:
        if len(keyword) <= 3 or keyword.replace(" ", "").isalnum():
            return re.search(rf"\b{re.escape(keyword)}\b", text, flags=re.IGNORECASE) is not None
        return keyword in text

    def _confidence(self, score: int) -> str:
        if score >= 7:
            return "High"
        if score >= 3:
            return "Medium"
        return "Low"
