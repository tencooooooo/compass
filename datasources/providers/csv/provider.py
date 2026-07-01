from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from datasources.base.datasource import BaseDataSource, DataSourceResult


class CSVProvider(BaseDataSource):
    """Local CSV reader provider."""

    name = "csv"
    requires_api_key = False

    def connect(self) -> bool:
        self.connected = self.enabled
        return self.connected

    def fetch(self, **kwargs: Any) -> DataSourceResult:
        if not self.enabled:
            return DataSourceResult(self.name, True, self.normalize([]), "Provider is disabled.")
        path = self._resolve(kwargs.get("path"))
        if path is None or not path.exists():
            return DataSourceResult(self.name, False, None, "CSV path does not exist.")
        with path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        normalized = self.normalize({"path": str(path), "rows": rows})
        return DataSourceResult(self.name, self.validate(normalized), normalized, "Loaded local CSV.")

    def normalize(self, data: Any) -> dict[str, Any]:
        payload = data if isinstance(data, dict) else {"rows": data}
        return {"provider": self.name, "source": "local_csv", "path": payload.get("path"), "rows": payload.get("rows", [])}

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict) and isinstance(data.get("rows"), list)

    def cache(self, key: str, data: Any) -> Path:
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        path = self.cache_dir / f"{key}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def disconnect(self) -> bool:
        self.connected = False
        return True

    def _resolve(self, value: Any) -> Path | None:
        if not value:
            return None
        path = Path(str(value))
        return path if path.is_absolute() else self.repo_root / path
