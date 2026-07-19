from __future__ import annotations

from datetime import datetime, timedelta, timezone
import json

from engines.notification.event_detector import classify_news, detect_important_news_alerts, is_recent_news, workflow_failure_event
from engines.notification.notification_engine import prune_history, sent_event_ids


def test_broad_financial_words_are_not_automatically_important():
    assert classify_news({"title": "Revenue rises in the quarter as cloud service demand improves"}) == []
    assert "決算" in classify_news({"title": "Company raises earnings guidance after quarterly results"})


def test_news_recency_requires_parseable_timestamp_within_window():
    now = datetime(2026, 7, 11, 12, tzinfo=timezone.utc)
    assert is_recent_news({"published_at": "2026-07-10T12:00:00+00:00"}, 36, now)
    assert not is_recent_news({"published_at": "2026-07-09T00:00:00+00:00"}, 36, now)
    assert not is_recent_news({"published_at": "invalid"}, 36, now)


def test_important_news_alerts_exclude_old_and_low_signal_items(tmp_path):
    news_dir = tmp_path / "storage" / "raw" / "news"
    news_dir.mkdir(parents=True)
    news_dir.joinpath("AAPL.json").write_text(
        json.dumps(
            [
                {
                    "ticker": "AAPL",
                    "title": "Apple announces $50 billion share buyback",
                    "published_at": "2026-07-11T10:00:00+00:00",
                },
                {
                    "ticker": "AAPL",
                    "title": "Apple announces a new factory",
                    "published_at": "2026-07-01T10:00:00+00:00",
                },
                {
                    "ticker": "AAPL",
                    "title": "Revenue rises in the quarter",
                    "published_at": "2026-07-11T11:00:00+00:00",
                },
            ]
        ),
        encoding="utf-8",
    )

    events = detect_important_news_alerts(
        tmp_path,
        {"important_news": True},
        max_news=5,
        max_age_hours=36,
        now=datetime(2026, 7, 11, 12, tzinfo=timezone.utc),
    )

    assert len(events) == 1
    assert events[0]["ticker"] == "AAPL"
    assert "buyback" in events[0]["summary"].lower()


def history_record(event_id: str, status: str, recorded_at: str) -> dict:
    return {"event_id": event_id, "status": status, "recorded_at": recorded_at}


def test_recent_skipped_events_are_resendable_but_stale_ones_are_not():
    now = datetime(2026, 7, 19, 12, tzinfo=timezone.utc)
    history = [
        history_record("sent-1", "sent", "2026-07-19T08:00:00+00:00"),
        history_record("skipped-fresh", "skipped_no_webhook", "2026-07-18T08:00:00+00:00"),
        history_record("skipped-stale", "skipped_no_webhook", "2026-07-10T08:00:00+00:00"),
        history_record("skipped-unparseable", "skipped_no_webhook", "invalid"),
    ]

    ids = sent_event_ids(history, now=now)

    assert "sent-1" in ids
    assert "skipped-fresh" not in ids
    assert "skipped-stale" in ids
    assert "skipped-unparseable" in ids


def test_prune_history_keeps_only_recent_records():
    now = datetime(2026, 7, 19, 12, tzinfo=timezone.utc)
    history = [
        history_record("recent", "sent", (now - timedelta(days=10)).isoformat()),
        history_record("old", "sent", (now - timedelta(days=120)).isoformat()),
        history_record("broken", "sent", "invalid"),
    ]

    pruned = prune_history(history, now=now)

    assert [record["event_id"] for record in pruned] == ["recent"]


def test_workflow_failure_event_includes_run_url_when_available():
    event = workflow_failure_event("failure", "42", "", "", run_url="https://github.com/example/repo/actions/runs/123")
    assert any("actions/runs/123" in detail for detail in event["details"])

    event = workflow_failure_event("failure", "42", "", "")
    assert not any(detail.startswith("Run:") for detail in event["details"])
