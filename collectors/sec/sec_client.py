from __future__ import annotations

import json
import os
import time
import gzip
import zlib
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class SECClient:
    """Small SEC EDGAR client with User-Agent, rate limit, and retry handling."""

    SEC_ARCHIVES = "https://www.sec.gov/Archives/edgar/data"
    SEC_TICKERS = "https://www.sec.gov/files/company_tickers.json"
    SEC_SUBMISSIONS = "https://data.sec.gov/submissions/CIK{cik}.json"
    SEC_COMPANY_FACTS = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

    def __init__(
        self,
        user_agent: str | None = None,
        request_interval: float = 0.2,
        max_retries: int = 3,
        timeout: int = 30,
    ) -> None:
        self.user_agent = user_agent or os.getenv("SEC_USER_AGENT") or "Compass Research Platform contact@example.com"
        self.request_interval = request_interval
        self.max_retries = max_retries
        self.timeout = timeout
        self._last_request_at = 0.0

    def get_company_tickers(self) -> dict[str, Any]:
        return self.get_json(self.SEC_TICKERS)

    def get_submissions(self, cik: str) -> dict[str, Any]:
        return self.get_json(self.SEC_SUBMISSIONS.format(cik=str(cik).zfill(10)))

    def get_company_facts(self, cik: str) -> dict[str, Any]:
        return self.get_json(self.SEC_COMPANY_FACTS.format(cik=str(cik).zfill(10)))

    def download_document(self, cik: str, accession_number: str, document: str) -> str:
        accession_path = accession_number.replace("-", "")
        cik_path = str(int(cik))
        url = f"{self.SEC_ARCHIVES}/{cik_path}/{accession_path}/{document}"
        return self.get_text(url)

    def filing_url(self, cik: str, accession_number: str, document: str) -> str:
        accession_path = accession_number.replace("-", "")
        return f"{self.SEC_ARCHIVES}/{int(cik)}/{accession_path}/{document}"

    def get_json(self, url: str) -> dict[str, Any]:
        return json.loads(self.get_text(url))

    def get_text(self, url: str) -> str:
        headers = {
            "User-Agent": self.user_agent,
            "Accept-Encoding": "gzip, deflate",
            "Host": self._host(url),
        }
        last_error: Exception | None = None
        for attempt in range(self.max_retries):
            self._throttle()
            try:
                request = Request(url, headers=headers)
                with urlopen(request, timeout=self.timeout) as response:
                    raw = response.read()
                    encoding = response.headers.get("Content-Encoding", "").lower()
                    if encoding == "gzip":
                        raw = gzip.decompress(raw)
                    elif encoding == "deflate":
                        raw = zlib.decompress(raw)
                    return raw.decode("utf-8", errors="replace")
            except (HTTPError, URLError, TimeoutError) as error:
                last_error = error
                time.sleep(min(2**attempt, 8))
        raise RuntimeError(f"SEC request failed after {self.max_retries} attempts: {url}") from last_error

    def ticker_to_cik(self, ticker: str, cache_path: Path | None = None) -> tuple[str, str]:
        data = self._load_ticker_data(cache_path)
        target = ticker.upper()
        for row in data.values():
            if str(row.get("ticker", "")).upper() == target:
                return str(row["cik_str"]).zfill(10), str(row.get("title") or target)
        raise KeyError(f"SEC CIK not found for ticker: {ticker}")

    def _load_ticker_data(self, cache_path: Path | None) -> dict[str, Any]:
        if cache_path and cache_path.exists():
            return json.loads(cache_path.read_text(encoding="utf-8"))
        data = self.get_company_tickers()
        if cache_path:
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return data

    def _throttle(self) -> None:
        elapsed = time.monotonic() - self._last_request_at
        if elapsed < self.request_interval:
            time.sleep(self.request_interval - elapsed)
        self._last_request_at = time.monotonic()

    def _host(self, url: str) -> str:
        if url.startswith("https://data.sec.gov"):
            return "data.sec.gov"
        return "www.sec.gov"
