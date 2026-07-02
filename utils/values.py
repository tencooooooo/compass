from __future__ import annotations

from typing import Any


def safe_float(value: Any) -> float | None:
    """floatに変換できない値とNaNをNoneに揃え、数値の扱いを統一します。"""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    # NaNは自分自身と等しくない性質を使い、pandasに依存せず判定します。
    return None if number != number else number
