from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class MemoryProvider(ABC):
    """Memory保存先を差し替えるためのProvider Interfaceです。"""

    @abstractmethod
    def save(self, collection: str, key: str, data: dict[str, Any]) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self, collection: str, key: str, default: Any = None) -> Any:
        raise NotImplementedError

    @abstractmethod
    def update(self, collection: str, key: str, updates: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, collection: str, key: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def exists(self, collection: str, key: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self, collection: str) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def search(self, collection: str, query: str, limit: int = 20) -> list[dict[str, Any]]:
        raise NotImplementedError
