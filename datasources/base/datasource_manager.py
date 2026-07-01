from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from datasources.base.datasource import REPO_ROOT, BaseDataSource
from datasources.base.datasource_registry import DataSourceRegistry
from datasources.providers.alpha_vantage import AlphaVantageProvider
from datasources.providers.csv import CSVProvider
from datasources.providers.earnings import EarningsProvider
from datasources.providers.finnhub import FinnhubProvider
from datasources.providers.fred import FREDProvider
from datasources.providers.json import JSONProvider
from datasources.providers.pdf import PDFProvider
from datasources.providers.sec import SECProvider
from datasources.providers.yahoo_finance import YahooFinanceProvider


class DataSourceManager:
    """Creates and manages configured Data Source Hub providers."""

    def __init__(self, config_path: Path | None = None, repo_root: Path | None = None) -> None:
        self.repo_root = repo_root or REPO_ROOT
        self.config_path = config_path or self.repo_root / "config" / "datasources.yaml"
        self.config = self._load_config()
        self.registry = DataSourceRegistry()
        self._register_defaults()

    def get(self, name: str) -> BaseDataSource:
        provider_class = self.registry.get_class(name)
        if provider_class is None:
            raise KeyError(f"Data source provider is not registered: {name}")
        provider_config = self.config.get("datasources", {}).get(name, {})
        return provider_class(config=provider_config, repo_root=self.repo_root)

    def list(self) -> list[str]:
        return self.registry.list()

    def enabled(self) -> list[str]:
        configured = self.config.get("datasources", {})
        return sorted(name for name in self.list() if configured.get(name, {}).get("enabled", False))

    def _load_config(self) -> dict[str, Any]:
        if not self.config_path.exists():
            return {"datasources": {}}
        return yaml.safe_load(self.config_path.read_text(encoding="utf-8")) or {"datasources": {}}

    def _register_defaults(self) -> None:
        self.registry.register("yahoo_finance", YahooFinanceProvider)
        self.registry.register("sec", SECProvider)
        self.registry.register("earnings", EarningsProvider)
        self.registry.register("fred", FREDProvider)
        self.registry.register("finnhub", FinnhubProvider)
        self.registry.register("alpha_vantage", AlphaVantageProvider)
        self.registry.register("csv", CSVProvider)
        self.registry.register("pdf", PDFProvider)
        self.registry.register("json", JSONProvider)
