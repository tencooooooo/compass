from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class FreshnessChecker:
    """Scores how recently provider files were updated."""

    def score(self, files: list[Path], expected_frequency_days: int = 1) -> dict[str, Any]:
        if not files:
            return {"score": 0, "latest_modified": None, "age_days": None, "expected_frequency_days": expected_frequency_days}
        latest = max(path.stat().st_mtime for path in files)
        latest_dt = datetime.fromtimestamp(latest, timezone.utc)
        age_days = max((datetime.now(timezone.utc) - latest_dt).total_seconds() / 86400, 0)
        if age_days <= expected_frequency_days:
            score = 100
        elif age_days <= expected_frequency_days * 3:
            score = 80
        elif age_days <= expected_frequency_days * 7:
            score = 55
        else:
            score = 25
        return {
            "score": score,
            "latest_modified": latest_dt.isoformat(),
            "age_days": round(age_days, 2),
            "expected_frequency_days": expected_frequency_days,
        }

