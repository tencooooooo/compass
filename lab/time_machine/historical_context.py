from typing import Any


class HistoricalContext:
    """Builds replay context from a future-safe snapshot."""

    def __init__(self, snapshot: dict[str, Any]):
        self.snapshot = snapshot

    def build(self) -> dict[str, Any]:
        tickers = sorted(set(self.snapshot.get("prices", {}).keys()) | set(self.snapshot.get("companies", {}).keys()))
        company_context = {ticker: self._company_context(ticker) for ticker in tickers}
        return {
            "date": self.snapshot.get("date"),
            "tickers": tickers,
            "companies": company_context,
            "market": self._market_context(company_context),
            "data_range": self._data_range(),
            "future_data_policy": "Only records dated on or before the snapshot date are included.",
        }

    def _company_context(self, ticker: str) -> dict[str, Any]:
        prices = self.snapshot.get("prices", {}).get(ticker, [])
        news = self.snapshot.get("news", {}).get(ticker, [])
        events = self.snapshot.get("events", {}).get(ticker, [])
        company = self.snapshot.get("companies", {}).get(ticker, {})
        financials = self.snapshot.get("financials", {}).get(ticker, {})
        memory = self.snapshot.get("memory", {}).get("companies", {}).get(ticker, {})
        score = self._score_company(prices, news, events, financials)
        return {
            "company": company,
            "financials": financials,
            "price_count": len(prices),
            "news_count": len(news),
            "event_count": len(events),
            "latest_price": prices[-1] if prices else None,
            "historical_score": score,
            "memory_history": memory.get("History", []) if isinstance(memory, dict) else [],
            "confidence": self._confidence(prices, news, financials),
        }

    def _market_context(self, company_context: dict[str, dict[str, Any]]) -> dict[str, Any]:
        sectors: dict[str, dict[str, Any]] = {}
        for ticker, context in company_context.items():
            company = context.get("company", {})
            sector = company.get("sector") or "Unknown"
            sector_data = sectors.setdefault(sector, {"sector": sector, "tickers": [], "scores": [], "news_count": 0, "event_count": 0})
            sector_data["tickers"].append(ticker)
            sector_data["scores"].append(context.get("historical_score", {}).get("total_score", 0))
            sector_data["news_count"] += context.get("news_count", 0)
            sector_data["event_count"] += context.get("event_count", 0)
        sector_rows = []
        for sector_data in sectors.values():
            scores = sector_data.pop("scores")
            sector_data["ticker_count"] = len(sector_data["tickers"])
            sector_data["average_score"] = round(sum(scores) / len(scores), 2) if scores else 0
            sector_rows.append(sector_data)
        return {
            "ticker_count": len(company_context),
            "sector_count": len(sector_rows),
            "sectors": sorted(sector_rows, key=lambda row: row["average_score"], reverse=True),
        }

    def _score_company(self, prices: list[dict[str, Any]], news: list[dict[str, Any]], events: list[dict[str, Any]], financials: dict[str, Any]) -> dict[str, Any]:
        growth = 20 if financials.get("total_revenue") else 8
        financial_health = 20 if financials.get("cash") and financials.get("shareholders_equity") else 8
        momentum = self._momentum_score(prices)
        news_score = min(20, 8 + len(news) + len(events) // 2)
        valuation = 12 if financials.get("eps") else 8
        total = min(100, growth + financial_health + momentum + news_score + valuation)
        return {
            "total_score": total,
            "components": {
                "Growth": growth,
                "Financial Health": financial_health,
                "Valuation": valuation,
                "Momentum": momentum,
                "News": news_score,
            },
            "method": "historical_replay_rule_based",
        }

    def _momentum_score(self, prices: list[dict[str, Any]]) -> int:
        if len(prices) < 22:
            return 8
        try:
            latest = float(prices[-1]["close"])
            previous = float(prices[-22]["close"])
        except (KeyError, TypeError, ValueError):
            return 8
        if previous == 0:
            return 8
        change = (latest - previous) / previous
        if change >= 0.10:
            return 20
        if change >= 0.03:
            return 16
        if change >= 0:
            return 12
        return 8

    def _confidence(self, prices: list[dict[str, Any]], news: list[dict[str, Any]], financials: dict[str, Any]) -> str:
        available = sum([bool(prices), bool(news), bool(financials)])
        if available == 3:
            return "High"
        if available == 2:
            return "Medium"
        return "Low"

    def _data_range(self) -> dict[str, Any]:
        price_dates = [row.get("date") for rows in self.snapshot.get("prices", {}).values() for row in rows if row.get("date")]
        return {
            "price_start": min(price_dates) if price_dates else None,
            "price_end": max(price_dates) if price_dates else None,
            "snapshot_date": self.snapshot.get("date"),
        }
