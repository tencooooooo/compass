from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def validate_operational_inputs(engine: str, repo_root: Path = REPO_ROOT) -> list[str]:
    errors: list[str] = []
    prices = list((repo_root / "storage" / "raw" / "prices").glob("*.csv"))
    companies = list((repo_root / "storage" / "raw" / "companies").glob("*.json"))
    discoveries = list((repo_root / "memory" / "discoveries").glob("*.json"))
    discovery_snapshots = [load_json(path, {}) for path in discoveries]

    if engine in {"performance", "strategy"}:
        if not prices:
            errors.append("storage/raw/prices contains no CSV files")
        if not (repo_root / "storage" / "raw" / "prices" / "SPY.csv").exists():
            errors.append("storage/raw/prices/SPY.csv is missing")
        if not companies:
            errors.append("storage/raw/companies contains no company profiles")

    if engine == "performance" and not any(
        isinstance(snapshot, dict) and snapshot.get("candidates") for snapshot in discovery_snapshots
    ):
        errors.append("memory/discoveries contains no candidate snapshots")

    if engine == "strategy":
        discovery = load_json(repo_root / "reports" / "discovery" / "discovery_candidates.json", {})
        if not isinstance(discovery, dict) or not discovery.get("candidates"):
            errors.append("reports/discovery/discovery_candidates.json contains no candidates")

    if engine == "experiment":
        performance_path = repo_root / "reports" / "performance" / "dashboard_metrics.json"
        strategy_path = repo_root / "reports" / "strategy" / "dashboard.json"
        performance = load_json(performance_path, {})
        strategy = load_json(strategy_path, {})
        if not performance_path.exists():
            errors.append("reports/performance/dashboard_metrics.json is missing")
        elif int((performance.get("overall") or {}).get("evaluated_count") or 0) == 0:
            errors.append("performance dashboard contains no evaluated rows")
        if not strategy_path.exists():
            errors.append("reports/strategy/dashboard.json is missing")
        elif not any(int(item.get("selected_count") or 0) > 0 for item in strategy.get("strategies", [])):
            errors.append("strategy dashboard contains no selected positions")

    if engine == "graph" and not companies:
        errors.append("storage/raw/companies contains no company profiles")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate restored Compass inputs before a scheduled engine run.")
    parser.add_argument("engine", choices=("performance", "strategy", "experiment", "graph"))
    args = parser.parse_args()
    errors = validate_operational_inputs(args.engine)
    if errors:
        for error in errors:
            print(f"::error::{args.engine}: {error}")
        return 1
    print(f"Operational inputs ready: {args.engine}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
