from __future__ import annotations

from core.memory.memory_engine import merge_item_history


def test_memory_item_history_accumulates_and_deduplicates_by_url():
    existing = [
        {
            "ticker": "AAPL",
            "title": "Older item",
            "url": "https://example.com/older",
            "published_at": "2026-07-01T00:00:00+00:00",
        }
    ]
    current = [
        {
            "ticker": "AAPL",
            "title": "Older item updated",
            "url": "https://example.com/older",
            "published_at": "2026-07-01T00:00:00+00:00",
        },
        {
            "ticker": "AAPL",
            "title": "New item",
            "url": "https://example.com/new",
            "published_at": "2026-07-11T00:00:00+00:00",
        },
    ]

    history = merge_item_history(existing, current)

    assert len(history) == 2
    assert history[0]["title"] == "New item"
    assert history[1]["title"] == "Older item updated"
