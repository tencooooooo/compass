from __future__ import annotations

import json

from utils.operational_inputs import validate_operational_inputs


def write(path, content: str = "data") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_performance_requires_durable_discovery_and_prices(tmp_path):
    errors = validate_operational_inputs("performance", tmp_path)
    assert "memory/discoveries contains no candidate snapshots" in errors
    assert "storage/raw/prices/SPY.csv is missing" in errors

    write(
        tmp_path / "memory" / "discoveries" / "2026-07-10.json",
        json.dumps({"candidates": [{"ticker": "AAPL"}]}),
    )
    write(tmp_path / "storage" / "raw" / "prices" / "SPY.csv")
    write(tmp_path / "storage" / "raw" / "companies" / "AAPL.json", "{}")
    assert validate_operational_inputs("performance", tmp_path) == []


def test_strategy_rejects_empty_discovery_candidates(tmp_path):
    write(tmp_path / "storage" / "raw" / "prices" / "SPY.csv")
    write(tmp_path / "storage" / "raw" / "companies" / "AAPL.json", "{}")
    write(
        tmp_path / "reports" / "discovery" / "discovery_candidates.json",
        json.dumps({"candidates": []}),
    )
    assert "reports/discovery/discovery_candidates.json contains no candidates" in validate_operational_inputs(
        "strategy", tmp_path
    )

    write(
        tmp_path / "reports" / "discovery" / "discovery_candidates.json",
        json.dumps({"candidates": [{"ticker": "AAPL"}]}),
    )
    assert validate_operational_inputs("strategy", tmp_path) == []


def test_experiment_and_graph_require_upstream_outputs(tmp_path):
    assert len(validate_operational_inputs("experiment", tmp_path)) == 2
    write(
        tmp_path / "reports" / "performance" / "dashboard_metrics.json",
        json.dumps({"overall": {"evaluated_count": 4}}),
    )
    write(
        tmp_path / "reports" / "strategy" / "dashboard.json",
        json.dumps({"strategies": [{"selected_count": 1}]}),
    )
    assert validate_operational_inputs("experiment", tmp_path) == []

    assert validate_operational_inputs("graph", tmp_path)
    write(tmp_path / "storage" / "raw" / "companies" / "AAPL.json", "{}")
    assert validate_operational_inputs("graph", tmp_path) == []
