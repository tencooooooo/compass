import csv
import json
from datetime import date, datetime
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT


DATE_FIELDS = ("date", "published_at", "timestamp", "generated_at", "created_at", "validation_date", "discovery_date")


class SnapshotLoader:
    """Loads only data available on or before the snapshot date."""

    def __init__(self, snapshot_date: str, repo_root: Path | None = None):
        self.snapshot_date = self._parse_date(snapshot_date)
        self.repo_root = repo_root or REPO_ROOT

    def load(self) -> dict[str, Any]:
        return {
            "date": self.snapshot_date.isoformat(),
            "prices": self.load_prices(),
            "companies": self.load_companies(),
            "financials": self.load_financials(),
            "news": self.load_news(),
            "events": self.load_events(),
            "knowledge": self.load_knowledge(),
            "memory": self.load_memory(),
        }

    def load_prices(self) -> dict[str, list[dict[str, Any]]]:
        prices: dict[str, list[dict[str, Any]]] = {}
        for path in self._glob("storage/raw/prices", "*.csv"):
            rows = []
            with path.open("r", encoding="utf-8", newline="") as handle:
                for row in csv.DictReader(handle):
                    row_date = self._parse_optional_date(row.get("date"))
                    if row_date and row_date <= self.snapshot_date:
                        rows.append(row)
            if rows:
                prices[path.stem.upper()] = rows
        return prices

    def load_companies(self) -> dict[str, dict[str, Any]]:
        companies: dict[str, dict[str, Any]] = {}
        for path in self._glob("storage/raw/companies", "*.json"):
            data = self._read_json(path, {})
            if isinstance(data, dict):
                companies[path.stem.upper()] = self._static_company_identity(data)
        return companies

    def load_financials(self) -> dict[str, dict[str, Any]]:
        financials: dict[str, dict[str, Any]] = {}
        for path in self._glob("storage/raw/financials", "*.json"):
            data = self._read_json(path, {})
            if not isinstance(data, dict):
                continue
            fiscal_date = self._fiscal_period_end(data)
            if fiscal_date is None or fiscal_date <= self.snapshot_date:
                financials[path.stem.upper()] = data
        return financials

    def load_news(self) -> dict[str, list[dict[str, Any]]]:
        return self._load_dated_list_directory("storage/raw/news")

    def load_events(self) -> dict[str, list[dict[str, Any]]]:
        events: dict[str, list[dict[str, Any]]] = {}
        for path in self._glob("storage/events", "*_events.json"):
            ticker = path.name.replace("_events.json", "").upper()
            events[ticker] = self._filter_records(self._read_json(path, []))
        return {ticker: rows for ticker, rows in events.items() if rows}

    def load_knowledge(self) -> dict[str, Any]:
        versions = []
        for path in self._glob("knowledge/versions", "*.json"):
            data = self._read_json(path, {})
            if not isinstance(data, dict):
                continue
            effective = self._parse_optional_date(data.get("effective_from") or data.get("created_at"))
            if data.get("status") == "active" and effective is not None and effective <= self.snapshot_date:
                versions.append(data)
        baseline_files = {}
        if versions:
            for path in self._glob("knowledge", "*.md"):
                baseline_files[path.name] = path.read_text(encoding="utf-8")
        return {
            "versions": versions,
            "baseline_files": baseline_files,
            "policy": "Knowledge with effective_from/created_at after snapshot is excluded. Undated markdown is only included when at least one Knowledge version is active for the snapshot date.",
        }

    def load_memory(self) -> dict[str, Any]:
        return {
            "companies": self._load_company_memory(),
            "discoveries": self._load_dated_json_files("memory/discoveries"),
            "validations": self._load_monthly_json_files("memory/validations"),
            "market": self._load_dated_json_files("memory/market"),
            "learning": self._filter_records(self._read_repo_json("memory/learning/learning_history.json", [])),
        }

    def _load_company_memory(self) -> dict[str, dict[str, Any]]:
        output: dict[str, dict[str, Any]] = {}
        for path in self._glob("memory/companies", "*.json"):
            data = self._read_json(path, {})
            if not isinstance(data, dict):
                continue
            history = data.get("History", [])
            filtered = self._filter_records(history) if isinstance(history, list) else []
            item = dict(data)
            item["History"] = filtered
            output[path.stem.upper()] = item
        return output

    def _load_dated_json_files(self, relative_dir: str) -> dict[str, Any]:
        output: dict[str, Any] = {}
        for path in self._glob(relative_dir, "*.json"):
            file_date = self._parse_optional_date(path.stem)
            if file_date and file_date <= self.snapshot_date:
                output[path.stem] = self._read_json(path, {})
        return output

    def _load_monthly_json_files(self, relative_dir: str) -> dict[str, Any]:
        output: dict[str, Any] = {}
        for path in self._glob(relative_dir, "*.json"):
            file_date = self._parse_optional_date(f"{path.stem}-01")
            if file_date and file_date <= self.snapshot_date:
                output[path.stem] = self._read_json(path, {})
        return output

    def _load_dated_list_directory(self, relative_dir: str) -> dict[str, list[dict[str, Any]]]:
        output: dict[str, list[dict[str, Any]]] = {}
        for path in self._glob(relative_dir, "*.json"):
            rows = self._filter_records(self._read_json(path, []))
            if rows:
                output[path.stem.upper()] = rows
        return output

    def _filter_records(self, records: Any) -> list[dict[str, Any]]:
        if not isinstance(records, list):
            return []
        filtered = []
        for record in records:
            if not isinstance(record, dict):
                continue
            record_date = self._record_date(record)
            if record_date is None or record_date <= self.snapshot_date:
                filtered.append(record)
        return filtered

    def _static_company_identity(self, data: dict[str, Any]) -> dict[str, Any]:
        allowed_fields = (
            "ticker",
            "company_name",
            "sector",
            "industry",
            "country",
            "currency",
            "exchange",
            "website",
            "business_summary",
        )
        return {field: data.get(field) for field in allowed_fields if field in data}

    def _record_date(self, record: dict[str, Any]) -> date | None:
        for field in DATE_FIELDS:
            parsed = self._parse_optional_date(record.get(field))
            if parsed:
                return parsed
        return None

    def _fiscal_period_end(self, data: dict[str, Any]) -> date | None:
        quarter = str(data.get("fiscal_quarter", ""))
        year = data.get("fiscal_year")
        if quarter and "-Q" in quarter:
            try:
                fiscal_year, fiscal_quarter = quarter.split("-Q", 1)
                month = int(fiscal_quarter) * 3
                return date(int(fiscal_year), month, 28)
            except ValueError:
                return None
        if year:
            try:
                return date(int(year), 12, 31)
            except ValueError:
                return None
        return None

    def _glob(self, relative_dir: str, pattern: str) -> list[Path]:
        path = self.repo_root / relative_dir
        if not path.exists():
            return []
        return sorted(path.glob(pattern))

    def _read_repo_json(self, relative_path: str, fallback: Any) -> Any:
        return self._read_json(self.repo_root / relative_path, fallback)

    def _read_json(self, path: Path, fallback: Any) -> Any:
        if not path.exists():
            return fallback
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return fallback

    def _parse_optional_date(self, value: Any) -> date | None:
        if value in (None, ""):
            return None
        text = str(value)
        try:
            return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
        except ValueError:
            try:
                return date.fromisoformat(text[:10])
            except ValueError:
                return None

    def _parse_date(self, value: str) -> date:
        return date.fromisoformat(value)
