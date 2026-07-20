import unittest

import pandas as pd

from engines.discovery.candidate_selector import build_candidate
from engines.scoring_engine.score_calculator import calculate_company_score, signal_strength_level


def price_frame(closes: list[float]) -> pd.DataFrame:
    dates = pd.bdate_range("2025-01-01", periods=len(closes))
    return pd.DataFrame(
        {
            "date": dates,
            "close": closes,
            "adj_close": closes,
            "volume": [1_000_000] * len(closes),
        }
    )


def full_financials(sign: float) -> dict:
    """sign=+1で全項目プラス、sign=-1で全項目マイナス(データは完全に存在する)。"""
    quarters = []
    for year in (2025, 2024):
        for quarter in (2, 1):
            base = 100_000_000 * (1.2 if year == 2025 else 1.0)
            quarters.append(
                {
                    "fiscal_quarter": f"{year}-Q{quarter}",
                    "total_revenue": base,
                    "eps": sign * (2.0 if year == 2025 else 1.5),
                }
            )
    return {
        "total_revenue": 120_000_000,
        "eps": sign * 2.0,
        "net_income": sign * 10_000_000,
        "operating_income": sign * 12_000_000,
        "research_and_development": 5_000_000 if sign > 0 else 0,
        "free_cash_flow": sign * 8_000_000,
        "cash": 50_000_000,
        "total_liabilities": 40_000_000,
        "shareholders_equity": sign * 60_000_000,
        "long_term_debt": 10_000_000,
        "current_ratio": 2.0 if sign > 0 else 0.5,
        "quarterly_financials": quarters,
    }


def full_company() -> dict:
    return {
        "company_name": "Test Corp",
        "sector": "Technology",
        "trailing_pe": 20.0,
        "forward_pe": 18.0,
        "peg_ratio": 1.5,
        "price_to_book": 5.0,
        "eps": 2.0,
    }


def news_items(count: int = 10) -> list[dict]:
    return [{"title": f"Company update {index}", "summary": "quarterly report"} for index in range(count)]


class ConfidenceDataOnlyTest(unittest.TestCase):
    def test_weak_signals_do_not_lower_confidence(self):
        """データが同一なら、シグナルが強くても弱くてもConfidence(データ充足度)は一致する。"""
        prices = price_frame([100.0] * 300)
        strong = calculate_company_score(
            ticker="STRONG",
            company=full_company(),
            financials=full_financials(1),
            news_items=news_items(),
            events=[],
            prices=prices,
        )
        weak = calculate_company_score(
            ticker="WEAK",
            company=full_company(),
            financials=full_financials(-1),
            news_items=news_items(),
            events=[],
            prices=prices,
        )
        self.assertEqual(strong["confidence"]["level"], weak["confidence"]["level"])
        self.assertEqual(strong["confidence"]["completeness_score"], weak["confidence"]["completeness_score"])

    def test_signal_strength_reflects_signal_quality(self):
        prices_up = price_frame([100 * (1.01**i) for i in range(300)])
        prices_down = price_frame([100 * (0.99**i) for i in range(300)])
        strong = calculate_company_score(
            ticker="STRONG",
            company=full_company(),
            financials=full_financials(1),
            news_items=news_items(),
            events=[],
            prices=prices_up,
        )
        weak = calculate_company_score(
            ticker="WEAK",
            company=full_company(),
            financials=full_financials(-1),
            news_items=news_items(),
            events=[],
            prices=prices_down,
        )
        self.assertGreater(strong["signal_strength"]["signal_rate"], weak["signal_strength"]["signal_rate"])

    def test_signal_strength_ignores_unavailable_sections(self):
        """データが無い領域はシグナル評価の分母に入らない。"""
        result = calculate_company_score(
            ticker="NODATA",
            company={},
            financials={},
            news_items=[],
            events=[],
            prices=pd.DataFrame(),
        )
        self.assertEqual(result["signal_strength"]["evaluated_max_score"], 0)
        self.assertIsNone(result["signal_strength"]["signal_rate"])
        self.assertEqual(result["signal_strength"]["level"], "Weak")

    def test_signal_strength_level_thresholds(self):
        self.assertEqual(signal_strength_level(70.0), "Strong")
        self.assertEqual(signal_strength_level(50.0), "Moderate")
        self.assertEqual(signal_strength_level(30.0), "Weak")
        self.assertEqual(signal_strength_level(None), "Weak")


class DiscoveryWeakSignalTest(unittest.TestCase):
    def build(self, financials: dict) -> dict:
        return build_candidate(
            ticker="TEST",
            company=full_company(),
            financials=financials,
            news_items=news_items(),
            events=[],
            prices=price_frame([100.0] * 300),
            score_result={},
            company_report="",
            market_dashboard={},
        )

    def test_negative_fundamentals_are_weak_signals_not_missing(self):
        candidate = self.build(full_financials(-1))
        for label in ("eps", "free_cash_flow", "total_revenue"):
            self.assertNotIn(label, candidate["missing_data"])
        self.assertIn("eps", candidate["metrics"]["weak_signals"])
        self.assertIn("free_cash_flow", candidate["metrics"]["weak_signals"])

    def test_absent_fundamentals_stay_missing(self):
        # companyのepsフォールバックも効かないよう、企業プロファイルも空にする。
        candidate = build_candidate(
            ticker="TEST",
            company={},
            financials={},
            news_items=[],
            events=[],
            prices=price_frame([100.0] * 300),
            score_result={},
            company_report="",
            market_dashboard={},
        )
        for label in ("total_revenue", "eps", "research_and_development", "free_cash_flow"):
            self.assertIn(label, candidate["missing_data"])
        self.assertEqual(candidate["metrics"]["weak_signals"], [])

    def test_candidate_reports_signal_strength(self):
        candidate = self.build(full_financials(1))
        self.assertIn(candidate["signal_strength"], {"Strong", "Moderate", "Weak"})
        self.assertIsNotNone(candidate["signal_rate"])
        self.assertGreater(candidate["metrics"]["signal_max_points"], 0)

    def test_weak_fundamentals_lower_signal_rate_but_not_confidence(self):
        strong = self.build(full_financials(1))
        weak = self.build(full_financials(-1))
        self.assertEqual(strong["confidence"], weak["confidence"])
        self.assertGreater(strong["signal_rate"], weak["signal_rate"])


if __name__ == "__main__":
    unittest.main()
