from __future__ import annotations

from typing import Any

from collectors.earnings.fetch_transcripts import EarningsTranscriptCollector
from datasources.base.datasource import BaseDataSource, DataSourceResult


class EarningsProvider(BaseDataSource):
    """Data Source Hub provider for earnings call transcript collection."""

    name = "earnings"
    requires_api_key = False

    def connect(self) -> bool:
        self.connected = self.enabled
        return self.connected

    def fetch(self, **kwargs: Any) -> DataSourceResult:
        if not self.enabled:
            return DataSourceResult(self.name, True, self.normalize({}), "Earnings provider is disabled.")
        ticker = kwargs.get("ticker")
        if not ticker:
            return DataSourceResult(self.name, False, None, "ticker is required.")
        metadata = {
            key: kwargs.get(key)
            for key in (
                "company_name",
                "fiscal_quarter",
                "earnings_date",
                "transcript_date",
                "source",
                "language",
                "ceo_name",
                "cfo_name",
            )
            if kwargs.get(key)
        }
        result = EarningsTranscriptCollector(project_root=self.repo_root).run(
            ticker=str(ticker),
            source_path=kwargs.get("source_path"),
            source_url=kwargs.get("source_url"),
            metadata=metadata,
        )
        normalized = self.normalize(result)
        return DataSourceResult(self.name, self.validate(normalized), normalized, "Fetched earnings transcript.")

    def normalize(self, data: Any) -> dict[str, Any]:
        payload = data if isinstance(data, dict) else {"results": data}
        return {
            "provider": self.name,
            "source": "Earnings call transcript",
            "results": payload.get("results", []),
            "success": payload.get("success", False),
        }

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict) and data.get("provider") == self.name and isinstance(data.get("results"), list)

    def cache(self, key: str, data: Any):
        import json

        self.cache_dir.mkdir(parents=True, exist_ok=True)
        path = self.cache_dir / f"{key}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def disconnect(self) -> bool:
        self.connected = False
        return True
