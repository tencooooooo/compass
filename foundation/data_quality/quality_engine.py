from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from api.services.data_loader import REPO_ROOT
from foundation.data_quality.quality_checker import QualityChecker
from foundation.data_quality.quality_report import QualityReport


PROVIDER_PATHS = {
    "prices": "storage/raw/prices",
    "companies": "storage/raw/companies",
    "financials": "storage/raw/financials",
    "news": "storage/raw/news",
    "events": "storage/events",
    "sec": "storage/raw/sec",
    "earnings": "storage/raw/earnings",
    "macro": "storage/raw/macro",
    "etf": "storage/raw/etf",
    "insider": "storage/raw/insider",
    "analyst": "storage/raw/analyst",
    "trends": "storage/raw/trends",
    "future_providers": "storage/raw/future_providers",
}


class DataQualityEngine:
    """Scores quality, freshness, completeness, duplicates, and reliability for Compass data."""

    @classmethod
    def run(cls, warning_threshold: int | None = None) -> dict[str, Any]:
        threshold = warning_threshold or int(os.getenv("COMPASS_DATA_QUALITY_THRESHOLD", "70"))
        checker = QualityChecker()
        providers = [
            checker.evaluate_provider(provider, REPO_ROOT / relative_path)
            for provider, relative_path in PROVIDER_PATHS.items()
        ]
        scored = [row["quality_score"] for row in providers if row["file_count"] > 0]
        overall = round(sum(scored) / len(scored)) if scored else 0
        issues = [issue for row in providers for issue in row["issues"]]
        result = {
            "success": True,
            "evaluation_date": datetime.now(timezone.utc).isoformat(),
            "overall_quality_score": overall,
            "warning_threshold": threshold,
            "warning": overall < threshold,
            "providers": providers,
            "issues": issues,
        }
        outputs = QualityReport().write(result)
        result["outputs"] = outputs
        if result["warning"]:
            print(f"::warning::Compass Data Quality Score {overall} is below threshold {threshold}.")
        return result


if __name__ == "__main__":
    print(DataQualityEngine.run())
