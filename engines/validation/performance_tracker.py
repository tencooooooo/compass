from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd


TRACKING_COLUMNS = [
    "discovery_date",
    "validation_date",
    "period",
    "ticker",
    "company",
    "sector",
    "discovery_score",
    "discovery_reasons",
    "start_date",
    "end_date",
    "start_price",
    "end_price",
    "validation_result",
    "return_percent",
    "benchmark",
    "benchmark_return_percent",
    "benchmark_diff_percent",
    "sector_average_return_percent",
    "sector_diff_percent",
    "confidence",
    "event_count",
    "evidence",
    "period_complete",
]


def normalize_history_rows(rows: list[dict[str, Any]]) -> pd.DataFrame:
    """Validation履歴をCSV/JSONで扱いやすい列構成にそろえます。"""
    normalized_rows = []
    for row in rows:
        normalized_rows.append({column: row.get(column) for column in TRACKING_COLUMNS})
    return pd.DataFrame(normalized_rows, columns=TRACKING_COLUMNS)


def merge_with_existing(
    history_path: Path,
    rows: list[dict[str, Any]],
    persistent_rows: list[dict[str, Any]] | None = None,
) -> pd.DataFrame:
    """同じDiscovery日・銘柄・期間の履歴は最新結果で上書きします。"""
    current = normalize_history_rows(persistent_rows or [])
    if history_path.exists():
        existing = pd.read_csv(history_path)
        current = pd.concat([existing, current], ignore_index=True)
    current = pd.concat([current, normalize_history_rows(rows)], ignore_index=True)

    if current.empty:
        return current

    key_columns = ["discovery_date", "ticker", "period"]
    current = current.drop_duplicates(subset=key_columns, keep="last")
    current = current.reindex(columns=TRACKING_COLUMNS)
    return current.sort_values(["discovery_date", "ticker", "period"]).reset_index(drop=True)


def merge_json_history(
    json_path: Path,
    rows: list[dict[str, Any]],
    persistent_rows: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """JSON履歴は詳細な理由やEvidenceを保ったまま蓄積します。"""
    existing_rows: list[dict[str, Any]] = []
    if json_path.exists():
        with json_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            existing_rows = [item for item in data if isinstance(item, dict)]

    merged: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in [*existing_rows, *(persistent_rows or []), *rows]:
        key = (str(row.get("discovery_date")), str(row.get("ticker")), str(row.get("period")))
        merged[key] = row

    return [merged[key] for key in sorted(merged)]


def save_history(
    report_dir: Path,
    rows: list[dict[str, Any]],
    persistent_rows: list[dict[str, Any]] | None = None,
) -> pd.DataFrame:
    """Validation履歴をCSVとJSONの両方で保存します。"""
    report_dir.mkdir(parents=True, exist_ok=True)
    csv_path = report_dir / "validation_history.csv"
    json_path = report_dir / "validation_history.json"

    history = merge_with_existing(csv_path, rows, persistent_rows)
    history.to_csv(csv_path, index=False)
    json_history = merge_json_history(json_path, rows, persistent_rows)
    json_path.write_text(json.dumps(json_history, ensure_ascii=False, indent=2), encoding="utf-8")
    return history
