import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from collectors.financials.fetch_sec_financials import SECFinancialsCollector


class StubSECClient:
    def __init__(self, company_facts: dict):
        self._company_facts = company_facts

    def ticker_to_cik(self, ticker: str, cache_path=None):
        return "0000320193", "Stub Company"

    def get_company_facts(self, cik: str) -> dict:
        return self._company_facts


def quarterly_facts(quarters: list[tuple[str, str, float]]) -> dict:
    entries = [
        {"start": start, "end": end, "val": value, "filed": end, "form": "10-Q"}
        for start, end, value in quarters
    ]
    return {"facts": {"us-gaap": {"Revenues": {"units": {"USD": entries}}}}}


def collector_with(tmp_dir: str, company_facts: dict) -> SECFinancialsCollector:
    collector = SECFinancialsCollector()
    collector.client = StubSECClient(company_facts)
    collector.financials_dir = Path(tmp_dir)
    return collector


FIVE_QUARTERS = [
    ("2026-01-01", "2026-03-31", 130.0),
    ("2025-10-01", "2025-12-31", 125.0),
    ("2025-07-01", "2025-09-30", 120.0),
    ("2025-04-01", "2025-06-30", 110.0),
    ("2025-01-01", "2025-03-31", 100.0),
]


class SecFinancialsEnrichmentTest(unittest.TestCase):
    def test_adopts_sec_series_and_keeps_yfinance_backup(self):
        with TemporaryDirectory() as tmp_dir:
            collector = collector_with(tmp_dir, quarterly_facts(FIVE_QUARTERS))
            path = Path(tmp_dir) / "AAPL.json"
            path.write_text(
                json.dumps({"ticker": "AAPL", "eps": 2.0, "quarterly_financials": [{"fiscal_quarter": "2026-Q1"}]}),
                encoding="utf-8",
            )

            adopted, _message = collector.enrich_ticker("AAPL", "2026-07-02T00:00:00")

            self.assertTrue(adopted)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["quarterly_source"], "sec_edgar")
            self.assertEqual(len(saved["quarterly_financials"]), 5)
            self.assertEqual(saved["quarterly_financials"][0]["fiscal_quarter"], "2026-Q1")
            self.assertEqual(saved["quarterly_financials_yfinance"], [{"fiscal_quarter": "2026-Q1"}])
            self.assertEqual(saved["eps"], 2.0)

    def test_skips_when_sec_series_is_too_short(self):
        with TemporaryDirectory() as tmp_dir:
            collector = collector_with(tmp_dir, quarterly_facts(FIVE_QUARTERS[:2]))
            path = Path(tmp_dir) / "AAPL.json"
            original = {"ticker": "AAPL", "quarterly_financials": [{"fiscal_quarter": "2026-Q1"}]}
            path.write_text(json.dumps(original), encoding="utf-8")

            adopted, message = collector.enrich_ticker("AAPL", "2026-07-02T00:00:00")

            self.assertFalse(adopted)
            self.assertIn("見送り", message)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), original)

    def test_creates_file_when_yfinance_data_is_missing(self):
        with TemporaryDirectory() as tmp_dir:
            collector = collector_with(tmp_dir, quarterly_facts(FIVE_QUARTERS))

            adopted, _message = collector.enrich_ticker("NEWCO", "2026-07-02T00:00:00")

            self.assertTrue(adopted)
            saved = json.loads((Path(tmp_dir) / "NEWCO.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["ticker"], "NEWCO")
            self.assertEqual(saved["quarterly_source"], "sec_edgar")
            self.assertNotIn("quarterly_financials_yfinance", saved)


if __name__ == "__main__":
    unittest.main()
