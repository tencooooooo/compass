from __future__ import annotations

import csv
from datetime import date, timedelta

from lab.performance.evaluator import Evaluator
from lab.performance.performance_engine import PerformanceEngine


def write_weekday_prices(repo_root, ticker: str, start: date, end: date) -> None:
    path = repo_root / "storage" / "raw" / "prices" / f"{ticker}.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["date", "close", "adj_close"])
        current = start
        price = 100.0
        while current <= end:
            if current.weekday() < 5:
                writer.writerow([current.isoformat(), price, price])
                price += 1.0
            current += timedelta(days=1)


def make_signal(discovery_date: str) -> dict:
    return {"ticker": "TEST", "discovery_date": discovery_date, "discovery_score": 80}


def test_weekend_target_date_completes_once_prices_pass_it(tmp_path):
    # Discovery 2026-06-28は日曜: 7日後の期限2026-07-05も日曜で、休場日に期限が当たるケース。
    write_weekday_prices(tmp_path, "TEST", date(2026, 6, 1), date(2026, 7, 17))
    row = Evaluator(repo_root=tmp_path)._evaluate_signal(make_signal("2026-06-28"), 7)

    assert row["status"] == "completed"
    assert row["actual_start_date"] == "2026-06-26"
    assert row["actual_end_date"] == "2026-07-03"


def test_pending_when_prices_have_not_reached_target_date(tmp_path):
    write_weekday_prices(tmp_path, "TEST", date(2026, 6, 1), date(2026, 7, 2))
    row = Evaluator(repo_root=tmp_path)._evaluate_signal(make_signal("2026-06-28"), 7)

    assert row["status"] == "pending"


def test_start_price_uses_last_close_on_or_before_discovery(tmp_path):
    # Validation Engine(backtest_engine)と同じ規約: Discoveryスコアが参照した直前終値を開始点にする。
    write_weekday_prices(tmp_path, "TEST", date(2026, 6, 1), date(2026, 7, 17))
    row = Evaluator(repo_root=tmp_path)._evaluate_signal(make_signal("2026-07-01"), 7)

    assert row["actual_start_date"] == "2026-07-01"
    row = Evaluator(repo_root=tmp_path)._evaluate_signal(make_signal("2026-07-04"), 7)
    assert row["actual_start_date"] == "2026-07-03"


def test_write_history_overwrites_same_evaluation_date_and_period(tmp_path, monkeypatch):
    import lab.performance.performance_engine as engine_module

    monkeypatch.setattr(engine_module, "REPO_ROOT", tmp_path)
    evaluation = {"evaluation_date": "2026-07-19"}
    metrics = {"periods": {"7": {"discovery_success_rate": 50.0, "average_return": 1.0, "alpha_vs_benchmark": 0.5}}}

    PerformanceEngine._write_history(evaluation, metrics)
    PerformanceEngine._write_history(evaluation, metrics)

    import json

    history = json.loads((tmp_path / "memory" / "performance" / "history.json").read_text(encoding="utf-8"))
    assert len(history) == 1
    assert history[0]["evaluation_date"] == "2026-07-19"
    assert history[0]["period"] == 7
