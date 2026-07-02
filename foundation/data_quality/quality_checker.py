from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from foundation.data_quality.duplicate_detector import DuplicateDetector
from foundation.data_quality.freshness_checker import FreshnessChecker
from foundation.data_quality.reliability_scorer import ReliabilityScorer


REQUIRED_FIELDS = {
    "prices": ("date", "close"),
    "companies": ("ticker",),
    "financials": ("ticker",),
    "news": ("ticker",),
    "events": ("ticker",),
    "sec": ("ticker", "filings"),
    "earnings": ("ticker", "transcripts"),
}


class QualityChecker:
    """Evaluates provider-level data quality for local Compass storage."""

    def __init__(self) -> None:
        self.freshness = FreshnessChecker()
        self.duplicates = DuplicateDetector()
        self.reliability = ReliabilityScorer()

    def evaluate_provider(self, provider: str, root: Path) -> dict[str, Any]:
        files = self._data_files(root)
        freshness = self.freshness.score(files, self._expected_frequency(provider))
        completeness = self._completeness(provider, files)
        reliability = self.reliability.score(provider)
        duplicates = self.duplicates.detect(files)
        consistency = self._consistency(provider, files)
        quality_score = round(
            freshness["score"] * 0.25
            + completeness["score"] * 0.3
            + reliability["score"] * 0.25
            + duplicates["score"] * 0.1
            + consistency["score"] * 0.1
        )
        issues = []
        for label, item in (
            ("freshness", freshness),
            ("completeness", completeness),
            ("duplicates", duplicates),
            ("consistency", consistency),
        ):
            if item["score"] < 70:
                issues.append({"provider": provider, "category": label, "severity": "warning", "detail": item})
        return {
            "provider": provider,
            "quality_score": quality_score,
            "freshness": freshness["score"],
            "completeness": completeness["score"],
            "reliability": reliability["score"],
            "duplicates": duplicates["duplicate_count"],
            "consistency": consistency["score"],
            "source_type": reliability["source_type"],
            "file_count": len(files),
            "latest_modified": freshness["latest_modified"],
            "issues": issues,
        }

    def _data_files(self, root: Path) -> list[Path]:
        if not root.exists():
            return []
        return sorted(path for path in root.rglob("*") if path.is_file() and path.name != ".gitkeep")

    def _expected_frequency(self, provider: str) -> int:
        if provider in {"prices", "news", "events", "trends"}:
            return 1
        if provider in {"financials", "companies", "analyst", "insider", "etf"}:
            return 7
        return 30

    def _completeness(self, provider: str, files: list[Path]) -> dict[str, Any]:
        if not files:
            return {"score": 0, "records": 0, "missing_required": 0, "null_rate": 1.0}
        required = REQUIRED_FIELDS.get(provider, ())
        checked = 0
        missing = 0
        nulls = 0
        values = 0
        for path in files[:100]:
            records = self._read_records(path)
            for record in records[:50]:
                if not isinstance(record, dict):
                    continue
                checked += 1
                for field in required:
                    if field not in record or record.get(field) in (None, "", []):
                        missing += 1
                for value in record.values():
                    values += 1
                    if value in (None, "", []):
                        nulls += 1
        if checked == 0:
            return {"score": 50, "records": 0, "missing_required": 0, "null_rate": 0}
        required_total = max(checked * len(required), 1)
        missing_rate = missing / required_total
        null_rate = nulls / max(values, 1)
        score = round(max(0, 100 - missing_rate * 60 - null_rate * 40))
        return {"score": score, "records": checked, "missing_required": missing, "null_rate": round(null_rate, 4)}

    def _consistency(self, provider: str, files: list[Path]) -> dict[str, Any]:
        if not files:
            return {"score": 0, "conflicts": 0, "checked": 0}
        conflicts = 0
        checked = 0
        for path in files[:100]:
            records = self._read_records(path)
            for record in records[:20]:
                if not isinstance(record, dict):
                    continue
                checked += 1
                ticker = record.get("ticker")
                if ticker and str(ticker).upper() != str(ticker):
                    conflicts += 1
        score = max(0, 100 - conflicts * 5)
        return {"score": score, "conflicts": conflicts, "checked": checked}

    def _read_records(self, path: Path) -> list[Any]:
        try:
            if path.suffix.lower() == ".json":
                data = json.loads(path.read_text(encoding="utf-8"))
                if isinstance(data, list):
                    return data
                if isinstance(data, dict):
                    return [data]
            if path.suffix.lower() == ".csv":
                with path.open("r", encoding="utf-8", newline="") as handle:
                    return list(csv.DictReader(handle))
        except (OSError, json.JSONDecodeError, UnicodeDecodeError):
            return []
        return []

