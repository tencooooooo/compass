from __future__ import annotations

import json

from lab.performance.evaluator import Evaluator


def write_json(path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def test_performance_uses_all_durable_discovery_dates(tmp_path):
    write_json(
        tmp_path / "storage" / "raw" / "companies" / "AAPL.json",
        {"ticker": "AAPL", "company_name": "Apple", "sector": "Technology"},
    )
    for date_key, score in (("2026-07-01", 70), ("2026-07-02", 75)):
        write_json(
            tmp_path / "memory" / "discoveries" / f"{date_key}.json",
            {
                "date": date_key,
                "generated_at": "2026-06-30T18:00:00-04:00",
                "candidates": [{"ticker": "AAPL", "company": "Apple", "score": score, "confidence": "High"}],
            },
        )

    signals = Evaluator(repo_root=tmp_path)._signals()

    assert [(row["discovery_date"], row["discovery_score"]) for row in signals] == [
        ("2026-07-01", 70),
        ("2026-07-02", 75),
    ]
    assert all(row["sector"] == "Technology" for row in signals)
