from __future__ import annotations

import json

from core.decision.review_manager import ReviewManager


def proposal(proposal_id: str = "PROP-1") -> dict:
    return {
        "proposal_id": proposal_id,
        "title": "Test proposal",
        "target": "Scoring",
        "created": "2026-07-10T00:00:00+00:00",
        "updated": "2026-07-10T00:00:00+00:00",
        "source_feedback": "2026-07-10T00:00:00+00:00",
    }


def test_review_manager_mirrors_report_and_durable_state(tmp_path):
    report_path = tmp_path / "reports" / "proposals" / "proposal_index.json"
    state_path = tmp_path / "memory" / "decision" / "proposal_index.json"
    manager = ReviewManager(report_path, state_path)

    manager.upsert_pending(proposal())
    manager.update_status("PROP-1", "Approved", reviewer="human")

    report = json.loads(report_path.read_text(encoding="utf-8"))
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert report == state
    assert state[0]["status"] == "Approved"
    assert state[0]["reviewer"] == "human"


def test_durable_state_wins_and_upsert_does_not_reset_approval(tmp_path):
    report_path = tmp_path / "reports" / "proposals" / "proposal_index.json"
    state_path = tmp_path / "memory" / "decision" / "proposal_index.json"
    state_path.parent.mkdir(parents=True)
    approved = {**proposal(), "status": "Approved", "reviewer": "human"}
    state_path.write_text(json.dumps([approved]), encoding="utf-8")

    manager = ReviewManager(report_path, state_path)
    manager.upsert_pending({**proposal(), "title": "Refreshed title"})

    rows = manager.load_index()
    assert rows[0]["status"] == "Approved"
    assert rows[0]["reviewer"] == "human"
    assert rows[0]["title"] == "Refreshed title"
