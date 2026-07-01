from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from datasources.base.datasource import BaseDataSource, DataSourceResult


class JSONProvider(BaseDataSource):
    """Local JSON reader provider for Memory and generated Compass artifacts."""

    name = "json"
    requires_api_key = False

    def connect(self) -> bool:
        self.connected = self.enabled
        return self.connected

    def fetch(self, **kwargs: Any) -> DataSourceResult:
        if not self.enabled:
            return DataSourceResult(self.name, True, self.normalize({}), "Provider is disabled.")
        path = self._resolve(kwargs.get("path"))
        if path is None or not path.exists():
            return DataSourceResult(self.name, False, None, "JSON path does not exist.")
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            return DataSourceResult(self.name, False, None, f"Failed to read JSON: {error}")
        normalized = self.normalize({"path": str(path), "data": data})
        return DataSourceResult(self.name, self.validate(normalized), normalized, "Loaded local JSON.")

    def normalize(self, data: Any) -> dict[str, Any]:
        payload = data if isinstance(data, dict) else {"data": data}
        return {"provider": self.name, "source": "local_json", "path": payload.get("path"), "data": payload.get("data")}

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict) and "data" in data

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
