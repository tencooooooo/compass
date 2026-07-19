from __future__ import annotations

from datetime import timezone
import json

from core.memory import memory_engine
from core.memory.local_provider import LocalProvider
from engines.validation import backtest_engine
from engines.validation.performance_tracker import save_history


def write_json(path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def validation_row(discovery_date: str, result: str, complete: bool) -> dict:
    return {
        "discovery_date": discovery_date,
        "validation_date": "2026-07-11",
        "period": "1w",
        "ticker": "AAPL",
        "validation_result": result,
        "return_percent": 4.0 if complete else 0.0,
        "period_complete": complete,
    }


def test_save_history_merges_durable_rows_and_refreshes_matching_signal(tmp_path):
    old_pending = validation_row("2026-07-01", "Neutral", False)
    old_completed = validation_row("2026-07-01", "Excellent", True)
    current = validation_row("2026-07-11", "Neutral", False)

    save_history(tmp_path, [old_completed, current], persistent_rows=[old_pending])

    rows = json.loads((tmp_path / "validation_history.json").read_text(encoding="utf-8"))
    assert len(rows) == 2
    assert rows[0]["discovery_date"] == "2026-07-01"
    assert rows[0]["period_complete"] is True
    assert rows[0]["validation_result"] == "Excellent"


def test_discovery_snapshots_include_memory_and_live_report(tmp_path, monkeypatch):
    memory_dir = tmp_path / "memory" / "discoveries"
    live_path = tmp_path / "reports" / "discovery" / "discovery_candidates.json"
    write_json(
        memory_dir / "2026-07-01.json",
        {
            "date": "2026-07-01",
            "generated_at": "2026-06-30T18:00:00-04:00",
            "candidates": [{"ticker": "AAPL", "score": 70, "reasons": ["old"]}],
        },
    )
    write_json(
        live_path,
        {
            "generated_at": "2026-07-11T18:00:00-04:00",
            "candidates": [{"ticker": "MSFT", "discovery_score": 80}],
        },
    )
    monkeypatch.setattr(backtest_engine, "DISCOVERY_MEMORY_DIR", memory_dir)
    monkeypatch.setattr(backtest_engine, "DISCOVERY_PATH", live_path)

    snapshots = backtest_engine.discovery_snapshots(timezone.utc)

    assert [item[0].date().isoformat() for item in snapshots] == ["2026-07-01", "2026-07-11"]
    assert snapshots[0][1][0]["discovery_score"] == 70
    assert snapshots[0][1][0]["discovery_reasons"] == ["old"]


def test_validation_memory_is_partitioned_by_discovery_month(tmp_path, monkeypatch):
    write_json(
        tmp_path / "reports" / "validation" / "validation_history.json",
        [validation_row("2026-06-30", "Good", True), validation_row("2026-07-01", "Neutral", False)],
    )
    monkeypatch.setattr(memory_engine, "PROJECT_ROOT", tmp_path)
    memory_engine.Memory.configure(LocalProvider(tmp_path / "memory"))

    count = memory_engine.build_validation_memory("2026-07-11T00:00:00+00:00")

    assert count == 2
    june = json.loads((tmp_path / "memory" / "validations" / "2026-06.json").read_text(encoding="utf-8"))
    july = json.loads((tmp_path / "memory" / "validations" / "2026-07.json").read_text(encoding="utf-8"))
    assert june["Good"] == 1
    assert june["Pending"] == 0
    assert june["average_return"] == 4.0
    assert july["Neutral"] == 0
    assert july["Pending"] == 1
    assert july["average_return"] is None
