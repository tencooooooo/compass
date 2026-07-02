from __future__ import annotations

from typing import Any

import pandas as pd


PRICE_COLUMNS = ["date", "open", "high", "low", "close", "adj_close", "volume"]
TRADING_DAY_WINDOWS = {
    30: 21,
    90: 63,
    180: 126,
    365: 252,
}


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


def trading_day_momentum(prices: pd.DataFrame, days: int) -> float | None:
    """Calculate momentum using trading-row counts instead of calendar-day offsets."""
    prices = normalize_price_frame(prices)
    window = TRADING_DAY_WINDOWS.get(days, days)
    if prices.empty or len(prices) <= window:
        return None
    latest = adjusted_close(prices.iloc[-1])
    base = adjusted_close(prices.iloc[-window - 1])
    if base in (None, 0) or latest is None:
        return None
    return ((latest - base) / base) * 100


# 1日で±50%を超える調整済み終値の変動は、分割未調整やデータ不良の疑いとして警告します。
EXTREME_DAILY_MOVE_PERCENT = 50.0


def validate_price_frame(prices: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    """OHLCVの不正行を除外し、疑わしい点の警告一覧を返します。

    除外(データとして矛盾): 終値・調整済み終値が0以下、high < low、出来高が負。
    警告のみ(正しい可能性もある): 前日比±50%超の変動。
    """
    prices = normalize_price_frame(prices)
    issues: list[str] = []
    if prices.empty:
        return prices, issues

    invalid = prices["close"] <= 0
    invalid |= prices["adj_close"] <= 0
    if "high" in prices.columns and "low" in prices.columns:
        both_present = prices["high"].notna() & prices["low"].notna()
        invalid |= both_present & (prices["high"] < prices["low"])
    if "volume" in prices.columns:
        invalid |= prices["volume"].notna() & (prices["volume"] < 0)

    dropped = int(invalid.sum())
    if dropped:
        dropped_dates = prices.loc[invalid, "date"].dt.strftime("%Y-%m-%d").tolist()
        issues.append(f"不正なOHLCV行を{dropped}件除外しました: {', '.join(dropped_dates[:5])}")
        prices = prices[~invalid].reset_index(drop=True)

    if len(prices) >= 2:
        daily_change = prices["adj_close"].pct_change().abs() * 100
        extreme = daily_change > EXTREME_DAILY_MOVE_PERCENT
        for index in prices.index[extreme]:
            issues.append(
                f"要確認: {prices.loc[index, 'date'].strftime('%Y-%m-%d')} の前日比変動が "
                f"{daily_change[index]:.1f}% です(分割未調整またはデータ不良の可能性)"
            )

    return prices, issues
