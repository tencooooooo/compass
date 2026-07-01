from __future__ import annotations

import csv
import json
from typing import Any

from datasources.base.datasource import BaseDataSource, DataSourceResult


class YahooFinanceProvider(BaseDataSource):
    """Provider facade for existing Yahoo Finance-backed Compass collectors."""

    name = "yahoo_finance"
    requires_api_key = False

    def connect(self) -> bool:
        self.connected = self.enabled
        return self.connected

    def fetch(self, **kwargs: Any) -> DataSourceResult:
        ticker = str(kwargs.get("ticker", "")).upper()
        dataset = str(kwargs.get("dataset", "company"))
        if not self.enabled:
            return DataSourceResult(self.name, True, self.normalize({}), "Provider is disabled.")
        if not ticker:
            return DataSourceResult(self.name, False, None, "ticker is required.")
        path = self._path(dataset, ticker)
        if not path.exists():
            return DataSourceResult(self.name, False, None, f"No local Yahoo Finance data found for {ticker}.")
        try:
            if path.suffix == ".csv":
                with path.open("r", encoding="utf-8", newline="") as handle:
                    data = list(csv.DictReader(handle))
            else:
                data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            return DataSourceResult(self.name, False, None, f"Failed to read local Yahoo Finance data: {error}")
        normalized = self.normalize({"ticker": ticker, "dataset": dataset, "data": data})
        return DataSourceResult(self.name, self.validate(normalized), normalized, "Loaded local Yahoo Finance data.")

    def normalize(self, data: Any) -> dict[str, Any]:
        payload = data if isinstance(data, dict) else {"data": data}
        return {
            "provider": self.name,
            "source": "Existing Compass Yahoo Finance collectors",
            "ticker": payload.get("ticker"),
            "dataset": payload.get("dataset"),
            "data": payload.get("data", {}),
        }

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict) and data.get("provider") == self.name and "data" in data

    def cache(self, key: str, data: Any):
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        path = self.cache_dir / f"{key}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def disconnect(self) -> bool:
        self.connected = False
        return True

    def _path(self, dataset: str, ticker: str):
        if dataset == "prices":
            return self.repo_root / "storage" / "raw" / "prices" / f"{ticker}.csv"
        if dataset == "financials":
            return self.repo_root / "storage" / "raw" / "financials" / f"{ticker}.json"
        if dataset == "news":
            return self.repo_root / "storage" / "raw" / "news" / f"{ticker}.json"
        return self.repo_root / "storage" / "raw" / "companies" / f"{ticker}.json"
