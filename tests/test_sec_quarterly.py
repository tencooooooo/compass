import unittest

from collectors.financials.sec_quarterly import extract_quarterly_financials


def usd_entry(start: str, end: str, val: float, filed: str, form: str = "10-Q") -> dict:
    return {"start": start, "end": end, "val": val, "filed": filed, "form": form}


def company_facts(revenues: list[dict], eps: list[dict] | None = None) -> dict:
    facts = {
        "Revenues": {"units": {"USD": revenues}},
    }
    if eps is not None:
        facts["EarningsPerShareDiluted"] = {"units": {"USD/shares": eps}}
    return {"facts": {"us-gaap": facts}}


class SecQuarterlyTest(unittest.TestCase):
    def test_extracts_quarterly_rows_newest_first(self):
        facts = company_facts(
            [
                usd_entry("2026-01-01", "2026-03-31", 120.0, "2026-04-25"),
                usd_entry("2025-01-01", "2025-03-31", 100.0, "2025-04-25"),
            ],
            eps=[
                usd_entry("2026-01-01", "2026-03-31", 1.2, "2026-04-25"),
                usd_entry("2025-01-01", "2025-03-31", 1.0, "2025-04-25"),
            ],
        )

        rows = extract_quarterly_financials(facts)

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["fiscal_quarter"], "2026-Q1")
        self.assertEqual(rows[0]["total_revenue"], 120.0)
        self.assertEqual(rows[0]["eps"], 1.2)
        self.assertEqual(rows[1]["fiscal_quarter"], "2025-Q1")

    def test_excludes_annual_duration_entries(self):
        facts = company_facts(
            [
                usd_entry("2025-01-01", "2025-12-31", 500.0, "2026-02-01", form="10-K"),
                usd_entry("2025-10-01", "2025-12-31", 130.0, "2026-02-01"),
            ]
        )

        rows = extract_quarterly_financials(facts)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["total_revenue"], 130.0)

    def test_duplicate_period_prefers_latest_filed(self):
        facts = company_facts(
            [
                usd_entry("2025-01-01", "2025-03-31", 100.0, "2025-04-25"),
                usd_entry("2025-01-01", "2025-03-31", 101.0, "2026-04-25"),
            ]
        )

        rows = extract_quarterly_financials(facts)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["total_revenue"], 101.0)

    def test_empty_or_missing_facts_return_empty(self):
        self.assertEqual(extract_quarterly_financials({}), [])
        self.assertEqual(extract_quarterly_financials({"facts": {"us-gaap": {}}}), [])

    def test_merges_quarters_across_revenue_tags(self):
        # ASC 606移行などでタグが切り替わった企業を想定します。
        # 優先タグが直近2四半期しか持たなくても、旧タグの四半期を捨てないことを確認します。
        facts = {
            "facts": {
                "us-gaap": {
                    "RevenueFromContractWithCustomerExcludingAssessedTax": {
                        "units": {
                            "USD": [
                                usd_entry("2026-01-01", "2026-03-31", 120.0, "2026-04-25"),
                                usd_entry("2025-10-01", "2025-12-31", 115.0, "2026-01-25"),
                            ]
                        }
                    },
                    "Revenues": {
                        "units": {
                            "USD": [
                                usd_entry("2025-07-01", "2025-09-30", 110.0, "2025-10-25"),
                                usd_entry("2025-04-01", "2025-06-30", 105.0, "2025-07-25"),
                                usd_entry("2025-01-01", "2025-03-31", 100.0, "2025-04-25"),
                            ]
                        }
                    },
                }
            }
        }

        rows = extract_quarterly_financials(facts)

        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0]["total_revenue"], 120.0)
        self.assertEqual(rows[4]["total_revenue"], 100.0)

    def test_same_period_prefers_higher_priority_tag(self):
        facts = {
            "facts": {
                "us-gaap": {
                    "RevenueFromContractWithCustomerExcludingAssessedTax": {
                        "units": {"USD": [usd_entry("2026-01-01", "2026-03-31", 120.0, "2026-04-25")]}
                    },
                    "Revenues": {
                        "units": {"USD": [usd_entry("2026-01-01", "2026-03-31", 999.0, "2026-04-25")]}
                    },
                }
            }
        }

        rows = extract_quarterly_financials(facts)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["total_revenue"], 120.0)

    def test_limits_to_max_quarters(self):
        entries = [
            usd_entry(f"{year}-01-01", f"{year}-03-31", float(year), f"{year}-04-25")
            for year in range(2016, 2027)
        ]
        rows = extract_quarterly_financials(company_facts(entries))

        self.assertEqual(len(rows), 8)
        self.assertEqual(rows[0]["fiscal_quarter"], "2026-Q1")


if __name__ == "__main__":
    unittest.main()
