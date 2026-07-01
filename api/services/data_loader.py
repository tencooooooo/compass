import csv
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]


def resolve_path(relative_path: str) -> Path:
    return REPO_ROOT / relative_path


def read_json(relative_path: str, fallback: Any) -> Any:
    path = resolve_path(relative_path)
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return fallback


def read_text(relative_path: str, fallback: str = "") -> str:
    path = resolve_path(relative_path)
    if not path.exists():
        return fallback
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return fallback


def read_csv_records(relative_path: str) -> list[dict[str, str]]:
    path = resolve_path(relative_path)
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except OSError:
        return []


def list_json_files(relative_path: str) -> list[Path]:
    path = resolve_path(relative_path)
    if not path.exists() or not path.is_dir():
        return []
    return sorted(item for item in path.glob("*.json") if item.is_file())
