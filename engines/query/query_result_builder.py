from datetime import datetime, timezone
from typing import Any


class QueryResultBuilder:
    """Builds the unified Query Engine response shape."""

    def success(self, query: str, data: Any) -> dict[str, Any]:
        return {
            "success": True,
            "query": query,
            "data": data,
            "timestamp": self._timestamp(),
            "result_count": self._count(data),
        }

    def failure(self, query: str, message: str) -> dict[str, Any]:
        return {
            "success": False,
            "query": query,
            "data": None,
            "timestamp": self._timestamp(),
            "result_count": 0,
            "error": message,
        }

    def _timestamp(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def _count(self, data: Any) -> int:
        if data is None:
            return 0
        if isinstance(data, list):
            return len(data)
        if isinstance(data, dict):
            for key in ("results", "candidates", "rows", "items", "history"):
                value = data.get(key)
                if isinstance(value, list):
                    return len(value)
            return 1 if data else 0
        return 1
