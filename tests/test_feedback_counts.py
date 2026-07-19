from __future__ import annotations

import json

from core.feedback import feedback_engine
from core.feedback.improvement_detector import result_counts


def test_result_counts_exclude_pending_rows():
    rows = [
        {"validation_result": "Good", "period_complete": True},
        {"validation_result": "Neutral", "period_complete": True},
        {"validation_result": "Neutral", "period_complete": False},
    ]

    counts = result_counts(rows)

    assert counts["Good"] == 1
    assert counts["Neutral"] == 1
    assert counts["Pending"] == 1


def make_analysis(generated_at: str) -> dict:
    return {
        "generated_at": generated_at,
        "overview": {"validation_count": 0, "completed_count": 0, "pending_count": 0},
        "improvement_candidates": [],
    }


def test_save_outputs_replaces_same_day_history_entry(tmp_path, monkeypatch):
    monkeypatch.setattr(feedback_engine, "REPORT_DIR", tmp_path / "reports")
    monkeypatch.setattr(feedback_engine, "REPORT_HISTORY_PATH", tmp_path / "reports" / "feedback_history.json")
    monkeypatch.setattr(feedback_engine, "MEMORY_HISTORY_PATH", tmp_path / "memory" / "feedback_history.json")

    feedback_engine.save_outputs(make_analysis("2026-07-18T08:00:00+09:00"))
    feedback_engine.save_outputs(make_analysis("2026-07-19T08:00:00+09:00"))
    feedback_engine.save_outputs(make_analysis("2026-07-19T12:00:00+09:00"))

    history = json.loads((tmp_path / "memory" / "feedback_history.json").read_text(encoding="utf-8"))
    assert [item["generated_at"] for item in history] == [
        "2026-07-18T08:00:00+09:00",
        "2026-07-19T12:00:00+09:00",
    ]
