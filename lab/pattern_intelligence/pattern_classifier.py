from typing import Any


class PatternClassifier:
    """Classifies success, failure, sector, market, and event pattern candidates."""

    def classify(self, features: dict[str, Any]) -> dict[str, Any]:
        companies = features.get("companies", {})
        return {
            "success_patterns": self._success_patterns(companies),
            "failure_patterns": self._failure_patterns(companies),
            "sector_patterns": self._sector_patterns(companies),
            "market_patterns": self._market_patterns(companies),
            "event_patterns": self._event_patterns(companies),
        }

    def _success_patterns(self, companies: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        patterns = []
        rd = self._tickers_where(companies, lambda item: self._value(item, "financials", "rd_ratio") and self._value(item, "financials", "rd_ratio") >= 0.08)
        if rd:
            patterns.append(self._pattern("High R&D intensity", rd, "Companies with R&D/revenue >= 8%.", "Medium"))
        eps = self._tickers_where(companies, lambda item: (self._value(item, "financials", "eps") or 0) > 0 and (self._value(item, "financials", "free_cash_flow") or 0) > 0)
        if eps:
            patterns.append(self._pattern("Positive EPS and FCF", eps, "Companies showing both positive EPS and free cash flow.", "Medium"))
        sector = self._tickers_where(companies, lambda item: (self._value(item, "market", "sector_average_momentum_1m") or 0) > 0)
        if sector:
            patterns.append(self._pattern("Sector tailwind", sector, "Companies in sectors with positive average 1M momentum.", "Low"))
        return patterns

    def _failure_patterns(self, companies: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        patterns = []
        news_dependent = self._tickers_where(companies, lambda item: (self._value(item, "activity", "news_count") or 0) >= 10 and (self._value(item, "activity", "momentum_1m") or 0) < 0)
        if news_dependent:
            patterns.append(self._pattern("News-heavy but weak momentum", news_dependent, "High news volume with negative 1M momentum may indicate temporary attention.", "Low"))
        valuation = self._tickers_where(companies, lambda item: (self._value(item, "financials", "trailing_pe") or 0) > 80)
        if valuation:
            patterns.append(self._pattern("Elevated valuation", valuation, "Trailing PER above 80 suggests valuation sensitivity.", "Low"))
        margin = self._tickers_where(companies, lambda item: self._value(item, "financials", "profit_margin") is not None and self._value(item, "financials", "profit_margin") < 0.05)
        if margin:
            patterns.append(self._pattern("Thin profit margin", margin, "Profit margin below 5% can weaken resilience.", "Medium"))
        return patterns

    def _sector_patterns(self, companies: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        sectors: dict[str, list[str]] = {}
        for ticker, item in companies.items():
            sectors.setdefault(item.get("sector") or "Unknown", []).append(ticker)
        return [self._pattern(f"{sector} cluster", tickers, f"{sector} appears in the current Compass universe.", "Medium") for sector, tickers in sorted(sectors.items())]

    def _market_patterns(self, companies: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        risk_off = self._tickers_where(companies, lambda item: self._value(item, "market", "sector_trend", "momentum") == "Risk-Off")
        weak = self._tickers_where(companies, lambda item: self._value(item, "market", "sector_trend", "momentum") == "Weak")
        patterns = []
        if risk_off:
            patterns.append(self._pattern("Risk-Off sector pressure", risk_off, "Sector trend reports Risk-Off momentum.", "Medium"))
        if weak:
            patterns.append(self._pattern("Weak sector momentum", weak, "Sector trend reports weak momentum.", "Medium"))
        return patterns

    def _event_patterns(self, companies: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        event_rich = self._tickers_where(companies, lambda item: (self._value(item, "activity", "event_count") or 0) >= 10)
        return [self._pattern("High event density", event_rich, "At least 10 event records are available for these companies.", "Low")] if event_rich else []

    def _pattern(self, name: str, tickers: list[str], evidence: str, confidence: str) -> dict[str, Any]:
        return {
            "name": name,
            "tickers": tickers,
            "evidence": evidence,
            "confidence": confidence,
            "requires_human_review": True,
        }

    def _tickers_where(self, companies: dict[str, dict[str, Any]], predicate) -> list[str]:
        return sorted(ticker for ticker, item in companies.items() if predicate(item))

    def _value(self, data: dict[str, Any], *keys: str) -> Any:
        current: Any = data
        for key in keys:
            if not isinstance(current, dict):
                return None
            current = current.get(key)
        return current
