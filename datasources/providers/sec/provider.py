from __future__ import annotations

from typing import Any

from collectors.sec.fetch_filings import SECFilingsCollector
from datasources.base.datasource import BaseDataSource, DataSourceResult


class SECProvider(BaseDataSource):
    """SEC EDGAR provider backed by the Compass SEC filings collector."""

    name = "sec"
    requires_api_key = False

    def connect(self) -> bool:
        self.connected = self.enabled
        return self.connected

    def fetch(self, **kwargs: Any) -> DataSourceResult:
        if not self.enabled:
            return DataSourceResult(self.name, True, self.normalize({}), "SEC provider is disabled.")
        ticker = kwargs.get("ticker")
        tickers = kwargs.get("tickers")
        selected = [ticker] if ticker else tickers
        forms = kwargs.get("forms") or self.config.get("forms") or ["10-K", "10-Q", "8-K"]
        limit = int(kwargs.get("limit") or self.config.get("limit", 1))
        collector = SECFilingsCollector(project_root=self.repo_root, forms=list(forms), limit=limit)
        result = collector.run(tickers=selected)
        normalized = self.normalize(result)
        return DataSourceResult(self.name, self.validate(normalized), normalized, "Fetched SEC EDGAR filings.")

    def normalize(self, data: Any) -> dict[str, Any]:
        payload = data if isinstance(data, dict) else {"results": data}
        return {
            "provider": self.name,
            "source": "SEC EDGAR",
            "forms": payload.get("forms", []),
            "limit": payload.get("limit"),
            "results": payload.get("results", []),
            "success": payload.get("success", False),
        }

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict) and data.get("provider") == self.name and isinstance(data.get("results"), list)

    def cache(self, key: str, data: Any):
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        path = self.cache_dir / f"{key}.json"
        import json

        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def disconnect(self) -> bool:
        self.connected = False
        return True
