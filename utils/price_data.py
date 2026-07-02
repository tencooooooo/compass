from __future__ import annotations

from typing import Any

import pandas as pd


PRICE_COLUMNS = ["date", "open", "high", "low", "close", "adj_close", "volume"]


def normalize_price_frame(prices: pd.DataFrame) -> pd.DataFrame:
    """Normalize local OHLCV data and keep adjusted close for return calculations."""
    if prices.empty or "date" not in prices.columns:
        return pd.DataFrame()
    prices = prices.copy()
    prices["date"] = pd.to_datetime(prices["date"]).dt.tz_localize(None)
    if "adj_close" not in prices.columns:
        prices["adj_close"] = prices.get("close")
    for column in ("open", "high", "low", "close", "adj_close", "volume"):
        if column in prices.columns:
            prices[column] = pd.to_numeric(prices[column], errors="coerce")
    required = ["date", "close", "adj_close"]
    return prices.dropna(subset=required).sort_values("date").reset_index(drop=True)


def adjusted_close(row: Any) -> float | None:
    """Return adjusted close when available, otherwise raw close for backward compatibility."""
    value = row.get("adj_close") if hasattr(row, "get") else None
    if value is None or pd.isna(value):
        value = row.get("close") if hasattr(row, "get") else None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return None if pd.isna(number) else number

