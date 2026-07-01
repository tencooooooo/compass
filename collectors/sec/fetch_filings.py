from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from collectors.sec.filing_index import FilingIndex  # noqa: E402
from collectors.sec.sec_client import SECClient  # noqa: E402
from collectors.sec.sec_normalizer import SECNormalizer  # noqa: E402
from collectors.sec.sec_parser import SUPPORTED_FORMS, SECParser  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


class SECFilingsCollector:
    """Collects SEC EDGAR filings and stores raw documents plus metadata."""

    def __init__(
        self,
        project_root: Path = PROJECT_ROOT,
        forms: list[str] | None = None,
        limit: int = 1,
        user_agent: str | None = None,
    ) -> None:
        self.project_root = project_root
        self.forms = forms or list(SUPPORTED_FORMS)
        self.limit = limit
        config = load_yaml(project_root / "config" / "datasources.yaml").get("datasources", {}).get("sec", {})
        configured_user_agent = user_agent or os.getenv(config.get("user_agent_env", "SEC_USER_AGENT"))
        self.client = SECClient(
            user_agent=configured_user_agent,
            request_interval=float(config.get("request_interval", 0.2)),
            max_retries=int(config.get("max_retries", 3)),
        )
        self.parser = SECParser()
        self.normalizer = SECNormalizer()
        self.output_root = project_root / "storage" / "raw" / "sec"
        self.cache_path = project_root / "datasources" / "cache" / "sec" / "company_tickers.json"

    def collect_ticker(self, ticker: str) -> dict[str, Any]:
        cik, company_name = self.client.ticker_to_cik(ticker, self.cache_path)
        submissions = self.client.get_submissions(cik)
        rows = self.parser.filings(submissions, self.forms, self.limit)
        company_dir = self.output_root / ticker.upper()
        filings_dir = company_dir / "filings"
        metadata_dir = company_dir / "metadata"
        filings_dir.mkdir(parents=True, exist_ok=True)
        metadata_dir.mkdir(parents=True, exist_ok=True)
        filing_index = FilingIndex(company_dir)
        saved_metadata = []
        skipped = []
        errors = []
        for row in rows:
            accession = row.get("accessionNumber")
            document = row.get("primaryDocument")
            if not accession or not document:
                errors.append({"accession_number": accession, "error": "Missing accession number or primary document."})
                continue
            source_url = self.client.filing_url(cik, accession, document)
            metadata = self.normalizer.normalize(ticker, company_name, cik, row, source_url)
            valid, missing = self.normalizer.validate(metadata)
            if not valid:
                errors.append({"accession_number": accession, "error": f"Missing required fields: {', '.join(missing)}"})
                continue
            metadata_path = metadata_dir / f"{accession}.json"
            filing_path = filings_dir / f"{accession}_{document}"
            if filing_index.exists(accession) and metadata_path.exists() and filing_path.exists():
                skipped.append(accession)
                saved_metadata.append(metadata)
                continue
            filing_text = self.client.download_document(cik, accession, document)
            filing_path.write_text(filing_text, encoding="utf-8")
            metadata["local_filing_path"] = str(filing_path.relative_to(self.project_root))
            metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
            json.loads(metadata_path.read_text(encoding="utf-8"))
            saved_metadata.append(metadata)
        index_path = filing_index.update(ticker, saved_metadata)
        return {
            "ticker": ticker.upper(),
            "company_name": company_name,
            "cik": cik,
            "saved": len(saved_metadata),
            "skipped": skipped,
            "errors": errors,
            "index_path": str(index_path.relative_to(self.project_root)),
        }

    def run(self, tickers: list[str] | None = None) -> dict[str, Any]:
        selected_tickers = tickers or load_tickers(self.project_root / "config" / "tickers.yaml")
        results = [self.collect_ticker(ticker) for ticker in selected_tickers]
        return {"success": True, "forms": self.forms, "limit": self.limit, "results": results}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch SEC EDGAR filings for Compass tickers.")
    parser.add_argument("--ticker", action="append", help="Ticker to fetch. Can be passed multiple times.")
    parser.add_argument("--forms", default="10-K,10-Q,8-K", help="Comma-separated form types.")
    parser.add_argument("--limit", type=int, default=1, help="Number of filings per form per ticker.")
    parser.add_argument("--user-agent", default=None, help="SEC User-Agent header. Defaults to SEC_USER_AGENT env var.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    forms = [form.strip() for form in args.forms.split(",") if form.strip()]
    collector = SECFilingsCollector(forms=forms, limit=args.limit, user_agent=args.user_agent)
    result = collector.run(tickers=args.ticker)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("success") else 1


if __name__ == "__main__":
    raise SystemExit(main())
