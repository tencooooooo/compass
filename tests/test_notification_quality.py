from __future__ import annotations

from datetime import datetime, timezone
import json

from engines.notification.event_detector import classify_news, detect_important_news_alerts, is_recent_news


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
