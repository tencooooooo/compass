from __future__ import annotations

from typing import Type

from datasources.base.datasource import BaseDataSource


class DataSourceRegistry:
    """Registry for Data Source Hub provider classes."""

    def __init__(self) -> None:
        self._providers: dict[str, Type[BaseDataSource]] = {}

    def register(self, name: str, provider_class: Type[BaseDataSource]) -> None:
        self._providers[name] = provider_class

    def unregister(self, name: str) -> None:
        self._providers.pop(name, None)

    def list(self) -> list[str]:
        return sorted(self._providers)

    def exists(self, name: str) -> bool:
        return name in self._providers

    def get_class(self, name: str) -> Type[BaseDataSource] | None:
        return self._providers.get(name)
