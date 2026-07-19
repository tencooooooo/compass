from __future__ import annotations

import csv
from datetime import datetime, timezone

from engines.scoring_engine.scoring_engine import sector_companies_for
from engines.validation import backtest_engine
from utils.tickers import load_peer_tickers, load_sector_benchmarks


def write_config(tmp_path, text: str):
    path = tmp_path / "tickers.yaml"
    path.write_text(text, encoding="utf-8")
    return path


def test_load_peer_tickers_dedupes_watch_and_normalizes(tmp_path):
    config = write_config(
        tmp_path,
        """
tickers:
  - AAPL
  - MSFT
peer_tickers:
  - aapl
  - avgo
  - AVGO
  - orcl
""",
    )
    assert load_peer_tickers(config) == ["AVGO", "ORCL"]


def test_load_sector_benchmarks_returns_mapping(tmp_path):
    config = write_config(
        tmp_path,
        """
tickers:
  - AAPL
sector_benchmarks:
  Technology: xlk
  Consumer Cyclical: XLY
""",
    )
    assert load_sector_benchmarks(config) == {"Technology": "XLK", "Consumer Cyclical": "XLY"}


def test_sector_companies_include_peer_profiles_from_pool():
    inputs = {"AAPL": {"company": {"ticker": "AAPL", "sector": "Technology"}}}
    pool = [
        {"ticker": "AAPL", "sector": "Technology"},
        {"ticker": "AVGO", "sector": "Technology"},
        {"ticker": "HD", "sector": "Consumer Cyclical"},
    ]

    peers = sector_companies_for("AAPL", inputs, pool)

    assert [peer["ticker"] for peer in peers] == ["AAPL", "AVGO"]


def write_prices(price_dir, ticker: str, rows: list[tuple[str, float]]) -> None:
    price_dir.mkdir(parents=True, exist_ok=True)
    with (price_dir / f"{ticker}.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["date", "close", "adj_close"])
        for date_text, price in rows:
            writer.writerow([date_text, price, price])


def test_validation_row_includes_sector_etf_diff(tmp_path, monkeypatch):
    price_dir = tmp_path / "prices"
    # 銘柄は+10%、セクターETFは+2% -> ETF差は+8ptになる。
    write_prices(price_dir, "TESTX", [("2026-06-01", 100.0), ("2026-06-08", 110.0), ("2026-06-15", 111.0)])
    write_prices(price_dir, "XLK", [("2026-06-01", 50.0), ("2026-06-08", 51.0), ("2026-06-15", 51.5)])
    monkeypatch.setattr(backtest_engine, "PRICE_DIR", price_dir)
    backtest_engine.load_prices.cache_clear()
    backtest_engine.ticker_period_return.cache_clear()

    row = backtest_engine.validation_row(
        candidate={"ticker": "TESTX", "sector": "Technology"},
        period_label="1w",
        period_days=7,
        discovery_date=datetime(2026, 6, 1, tzinfo=timezone.utc),
        validation_date=datetime(2026, 6, 15, tzinfo=timezone.utc),
        benchmark_name=None,
        companies={},
        sector_benchmarks={"Technology": "XLK"},
    )

    assert row["sector_benchmark"] == "XLK"
    assert round(row["sector_benchmark_return_percent"], 2) == 2.0
    assert round(row["sector_benchmark_diff_percent"], 2) == 8.0
    assert row["period_complete"] is True

    backtest_engine.load_prices.cache_clear()
    backtest_engine.ticker_period_return.cache_clear()
