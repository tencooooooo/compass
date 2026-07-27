"""Discovery Scoreのスケールと、config側の閾値が到達可能であることを保証します。

以前は配点合計が88点しか積み上がらないのに config で「90点以上」を判定していたため、
Discovery Alert と Discovery Score 90+ 戦略が構造的に一度も成立しませんでした。
"""

import unittest
from pathlib import Path

import numpy as np
import pandas as pd

from engines.discovery.candidate_selector import (
    DISCOVERY_MAX_SCORE,
    DISCOVERY_POINTS,
    build_candidate,
)
from utils.config import load_yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def ideal_prices(rows: int = 400) -> pd.DataFrame:
    """全ウィンドウで強く上昇し、直近だけ出来高が急増する理想的な価格系列。"""
    dates = pd.bdate_range("2024-01-01", periods=rows)
    closes = 10 * np.exp(np.linspace(0, 4, rows))
    return pd.DataFrame(
        {
            "date": dates,
            "close": closes,
            "adj_close": closes,
            "volume": [1_000] * (rows - 1) + [100_000],
        }
    )


def flat_prices(rows: int = 400) -> pd.DataFrame:
    dates = pd.bdate_range("2024-01-01", periods=rows)
    return pd.DataFrame(
        {
            "date": dates,
            "close": [100.0] * rows,
            "adj_close": [100.0] * rows,
            "volume": [1_000] * rows,
        }
    )


def best_case_candidate() -> dict:
    score_result = {
        "total_score": 100,
        "confidence": {"level": "High"},
        "signal_strength": {"level": "Strong"},
        "scores": {
            name: {"score": 20, "max_score": 20}
            for name in ("Growth", "Financial Health", "Valuation", "Momentum", "News")
        },
    }
    news = [
        {"title": "record growth strong demand partnership launch profit buyback", "summary": ""}
        for _ in range(20)
    ]
    market_dashboard = {
        "sectors": [
            {
                "sector": "Technology",
                "average_score": 10,
                "trend": {"news": "High", "financial_health": "Good", "momentum": "Strong"},
            }
        ]
    }
    return build_candidate(
        ticker="TEST",
        company={"company_name": "Test", "sector": "Technology"},
        financials={
            "research_and_development": 1e9,
            "free_cash_flow": 1e9,
            "eps": 5,
            "total_revenue": 2e11,
        },
        news_items=news,
        events=[{"price_change_percent": 9.0} for _ in range(5)],
        prices=ideal_prices(),
        score_result=score_result,
        company_report="",
        market_dashboard=market_dashboard,
        benchmark_prices=flat_prices(),
        benchmark_name="SPY",
    )


class DiscoveryScoreScaleTest(unittest.TestCase):
    def test_point_budget_sums_to_declared_max(self):
        self.assertEqual(sum(DISCOVERY_POINTS.values()), DISCOVERY_MAX_SCORE)
        self.assertEqual(DISCOVERY_MAX_SCORE, 100)

    def test_best_case_actually_reaches_max_score(self):
        candidate = best_case_candidate()

        self.assertEqual(candidate["discovery_score"], DISCOVERY_MAX_SCORE)
        self.assertEqual(candidate["max_score"], DISCOVERY_MAX_SCORE)
        self.assertEqual(candidate["status"], "Primary Candidate")

    def test_signal_rate_shares_the_same_denominator_as_the_score(self):
        """discovery_scoreに加点される項目は、必ずsignal_rateの分母にも入ることを確認します。"""
        candidate = best_case_candidate()

        self.assertEqual(candidate["signal_rate"], 100.0)
        self.assertEqual(candidate["metrics"]["signal_max_points"], float(DISCOVERY_MAX_SCORE))
        self.assertEqual(candidate["metrics"]["signal_earned_points"], float(DISCOVERY_MAX_SCORE))

    def test_configured_thresholds_are_reachable(self):
        notification = load_yaml(PROJECT_ROOT / "config" / "notification.yaml")
        strategy = load_yaml(PROJECT_ROOT / "config" / "strategy.yaml")

        alert_threshold = notification["notification"]["discovery_score"]
        self.assertLessEqual(alert_threshold, DISCOVERY_MAX_SCORE)

        self.assertLessEqual(strategy["buy"]["score"], DISCOVERY_MAX_SCORE)
        for name, definition in strategy["strategies"].items():
            score = definition.get("score")
            if score is not None:
                self.assertLessEqual(score, DISCOVERY_MAX_SCORE, f"strategy {name} の閾値が到達不能です")


if __name__ == "__main__":
    unittest.main()
