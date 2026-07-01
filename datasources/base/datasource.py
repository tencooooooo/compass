from __future__ import annotations

import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class DataSourceResult:
    """Structured response returned by Data Source Hub providers."""

    provider: str
    success: bool
    data: Any
    message: str = ""
    cached_path: str | None = None


class BaseDataSource(ABC):
    """Common interface for every Compass data source provider."""

    name = "base"
    requires_api_key = False
    api_key_env: str | None = None

    def __init__(self, config: dict[str, Any] | None = None, repo_root: Path | None = None) -> None:
        self.config = config or {}
        self.repo_root = repo_root or REPO_ROOT
        self.enabled = bool(self.config.get("enabled", False))
        self.connected = False
        self.cache_dir = self.repo_root / "datasources" / "cache" / self.name

    @abstractmethod
    def connect(self) -> bool:
        """Prepare the provider for use."""
        raise NotImplementedError

    @abstractmethod
    def fetch(self, **kwargs: Any) -> DataSourceResult:
        """Fetch data from the provider."""
        raise NotImplementedError

    @abstractmethod
    def normalize(self, data: Any) -> Any:
        """Normalize provider data for Compass consumers."""
        raise NotImplementedError

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate normalized provider data."""
        raise NotImplementedError

    @abstractmethod
    def cache(self, key: str, data: Any) -> Path:
        """Persist data in provider cache."""
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> bool:
        """Close provider resources."""
        raise NotImplementedError

    def api_key(self) -> str | None:
        env_name = self.config.get("api_key_env") or self.api_key_env
        return os.getenv(env_name) if env_name else None

    def is_available(self) -> bool:
        if not self.enabled:
            return False
        if self.requires_api_key:
            return bool(self.api_key())
        return True


class ScaffoldDataSource(BaseDataSource):
    """Disabled-safe base class for future API-backed providers."""

    source_label = "Future provider"

    def connect(self) -> bool:
        self.connected = self.is_available()
        return self.connected

    def fetch(self, **kwargs: Any) -> DataSourceResult:
        if not self.enabled:
            return DataSourceResult(
                provider=self.name,
                success=True,
                data=self.normalize({"items": [], "status": "disabled"}),
                message="Provider scaffold is disabled.",
            )
        if self.requires_api_key and not self.api_key():
            return DataSourceResult(
                provider=self.name,
                success=False,
                data=None,
                message="Provider requires an API key from environment or GitHub Secrets.",
            )
        return DataSourceResult(
            provider=self.name,
            success=True,
            data=self.normalize({"items": [], "status": "not_connected", "params": kwargs}),
            message="Provider scaffold has no external connection yet.",
        )

    def normalize(self, data: Any) -> dict[str, Any]:
        payload = data if isinstance(data, dict) else {"items": data}
        return {
            "provider": self.name,
            "source": self.source_label,
            "status": payload.get("status", "scaffold"),
            "items": payload.get("items", []),
            "normalized_at": datetime.now(timezone.utc).isoformat(),
        }

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict) and "provider" in data and "items" in data

    def cache(self, key: str, data: Any) -> Path:
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        path = self.cache_dir / f"{key}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def disconnect(self) -> bool:
        self.connected = False
        return True
