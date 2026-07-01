import json
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT
from engines.query.query_executor import QueryExecutor
from engines.query.query_parser import QueryParser
from engines.query.query_result_builder import QueryResultBuilder


class Query:
    """Internal Query API for Compass clients."""

    parser = QueryParser()
    executor = QueryExecutor()
    result_builder = QueryResultBuilder()
    history_path = REPO_ROOT / "memory" / "query" / "history.json"

    @classmethod
    def run(cls, query: str, **params: Any) -> dict[str, Any]:
        try:
            request = cls.parser.parse(query, **params)
            data = cls.executor.execute(request)
            result = cls.result_builder.success(query, data)
        except Exception as exc:
            result = cls.result_builder.failure(query, str(exc))
        cls._save_history(result)
        return result

    @classmethod
    def _save_history(cls, result: dict[str, Any]) -> None:
        cls.history_path.parent.mkdir(parents=True, exist_ok=True)
        history = cls._load_history(cls.history_path)
        history.append(
            {
                "query": result.get("query"),
                "timestamp": result.get("timestamp"),
                "result_count": result.get("result_count", 0),
                "success": result.get("success", False),
            }
        )
        cls.history_path.write_text(json.dumps(history[-500:], indent=2, ensure_ascii=False), encoding="utf-8")

    @staticmethod
    def _load_history(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []
        return data if isinstance(data, list) else []


if __name__ == "__main__":
    print(json.dumps(Query.run("Top Discovery"), indent=2, ensure_ascii=False))
