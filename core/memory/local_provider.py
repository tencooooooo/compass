from __future__ import annotations

import json
from pathlib import Path
import re
from typing import Any

from core.memory.memory_provider import MemoryProvider


class LocalProvider(MemoryProvider):
    """ローカルJSONファイルへMemoryを保存するProviderです。"""

    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def _safe_name(self, value: str) -> str:
        safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(value).strip())
        return safe.strip("_") or "unknown"

    def _path(self, collection: str, key: str) -> Path:
        collection_path = self.root / self._safe_name(collection)
        return collection_path / f"{self._safe_name(key)}.json"

    def save(self, collection: str, key: str, data: dict[str, Any]) -> None:
        path = self._path(collection, key)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def load(self, collection: str, key: str, default: Any = None) -> Any:
        path = self._path(collection, key)
        if not path.exists():
            return default
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def update(self, collection: str, key: str, updates: dict[str, Any]) -> dict[str, Any]:
        current = self.load(collection, key, default={})
        if not isinstance(current, dict):
            current = {}
        current.update(updates)
        self.save(collection, key, current)
        return current

    def delete(self, collection: str, key: str) -> bool:
        path = self._path(collection, key)
        if not path.exists():
            return False
        path.unlink()
        return True

    def exists(self, collection: str, key: str) -> bool:
        return self._path(collection, key).exists()

    def list(self, collection: str) -> list[str]:
        collection_path = self.root / self._safe_name(collection)
        if not collection_path.exists():
            return []
        return sorted(path.stem for path in collection_path.glob("*.json"))

    def search(self, collection: str, query: str, limit: int = 20) -> list[dict[str, Any]]:
        collection_path = self.root / self._safe_name(collection)
        if not collection_path.exists():
            return []
        normalized_query = query.lower()
        results: list[dict[str, Any]] = []
        for path in sorted(collection_path.glob("*.json")):
            text = path.read_text(encoding="utf-8")
            if normalized_query not in text.lower():
                continue
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                data = {"raw": text}
            results.append({"key": path.stem, "data": data})
            if len(results) >= limit:
                break
        return results
