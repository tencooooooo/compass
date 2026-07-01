from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class CollectorRunResult:
    """Small structured result for disabled and future data expansion collectors."""

    collector: str
    category: str
    enabled: bool
    success: bool
    message: str
    output_path: str | None = None


class CollectorInterface(ABC):
    """Common interface for future data-source collectors."""

    category: str = "unknown"
    data_categories: tuple[str, ...] = ()
    enabled: bool = False

    def __init__(
        self,
        project_root: Path | None = None,
        settings: dict[str, Any] | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self.project_root = project_root or PROJECT_ROOT
        self.settings = settings or {}
        self.logger = logger or logging.getLogger(self.__class__.__name__)
        self.output_dir = self.project_root / "storage" / "raw" / self.category

    @abstractmethod
    def collect(self) -> dict[str, Any]:
        """Collect raw source data."""
        raise NotImplementedError

    @abstractmethod
    def validate(self, raw_data: dict[str, Any]) -> bool:
        """Validate raw source data before normalization."""
        raise NotImplementedError

    @abstractmethod
    def normalize(self, raw_data: dict[str, Any]) -> dict[str, Any]:
        """Normalize raw source data to Compass storage schema."""
        raise NotImplementedError

    @abstractmethod
    def save(self, normalized_data: dict[str, Any]) -> Path:
        """Save normalized data under storage/raw/{category}."""
        raise NotImplementedError

    def run(self) -> CollectorRunResult:
        """Run the collector only when explicitly enabled in the future."""
        if not self.enabled:
            return CollectorRunResult(
                collector=self.__class__.__name__,
                category=self.category,
                enabled=False,
                success=True,
                message="Collector scaffold is disabled. External API connection is not implemented.",
            )

        raw_data = self.collect()
        if not self.validate(raw_data):
            return CollectorRunResult(
                collector=self.__class__.__name__,
                category=self.category,
                enabled=True,
                success=False,
                message="Collected data failed validation.",
            )
        normalized_data = self.normalize(raw_data)
        output_path = self.save(normalized_data)
        return CollectorRunResult(
            collector=self.__class__.__name__,
            category=self.category,
            enabled=True,
            success=True,
            message="Collector completed.",
            output_path=str(output_path.relative_to(self.project_root)),
        )


class DisabledCollector(CollectorInterface):
    """Reusable no-network scaffold for future collectors that need API credentials."""

    source_name: str = "Future data source"
    requires_api_key: bool = True

    def collect(self) -> dict[str, Any]:
        return {
            "collector": self.__class__.__name__,
            "source": self.source_name,
            "category": self.category,
            "data_categories": list(self.data_categories),
            "status": "disabled",
            "requires_api_key": self.requires_api_key,
            "items": [],
            "collected_at": datetime.now(timezone.utc).isoformat(),
        }

    def validate(self, raw_data: dict[str, Any]) -> bool:
        return isinstance(raw_data, dict) and raw_data.get("category") == self.category

    def normalize(self, raw_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "project": "Compass",
            "schema": "data_expansion_v1",
            "collector": raw_data.get("collector", self.__class__.__name__),
            "source": raw_data.get("source", self.source_name),
            "category": self.category,
            "data_categories": list(self.data_categories),
            "status": raw_data.get("status", "disabled"),
            "requires_api_key": raw_data.get("requires_api_key", self.requires_api_key),
            "items": raw_data.get("items", []),
            "normalized_at": datetime.now(timezone.utc).isoformat(),
        }

    def save(self, normalized_data: dict[str, Any]) -> Path:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        output_path = self.output_dir / "latest.json"
        output_path.write_text(json.dumps(normalized_data, ensure_ascii=False, indent=2), encoding="utf-8")
        return output_path
