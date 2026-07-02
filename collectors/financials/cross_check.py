from __future__ import annotations

from typing import Any

from utils.values import safe_float


# 相対乖離がこの割合を超えた四半期を、データ品質の警告として記録します。
REVENUE_TOLERANCE_PERCENT = 10.0


def _rows_by_quarter(rows: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(rows, list):
        return {}
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        if isinstance(row, dict) and isinstance(row.get("fiscal_quarter"), str):
            result.setdefault(row["fiscal_quarter"], row)
    return result


def revenue_cross_check(
    sec_rows: Any,
    yfinance_rows: Any,
    tolerance_percent: float = REVENUE_TOLERANCE_PERCENT,
) -> dict[str, Any]:
    """SECとyfinanceの四半期売上を突き合わせ、乖離が大きい四半期を報告します。

    どちらか一方のデータ不良・通貨違い・会計基準差の検出に使います。
    判定はせず事実のみ記録し、解釈は人間のレビューに委ねます。
    """
    sec_by_quarter = _rows_by_quarter(sec_rows)
    yfinance_by_quarter = _rows_by_quarter(yfinance_rows)

    checked = 0
    mismatches: list[dict[str, Any]] = []
    for quarter, sec_row in sec_by_quarter.items():
        yfinance_row = yfinance_by_quarter.get(quarter)
        if yfinance_row is None:
            continue
        sec_revenue = safe_float(sec_row.get("total_revenue"))
        yfinance_revenue = safe_float(yfinance_row.get("total_revenue"))
        if sec_revenue in (None, 0) or yfinance_revenue is None:
            continue
        checked += 1
        diff_percent = abs(yfinance_revenue - sec_revenue) / abs(sec_revenue) * 100
        if diff_percent > tolerance_percent:
            mismatches.append(
                {
                    "fiscal_quarter": quarter,
                    "sec_revenue": sec_revenue,
                    "yfinance_revenue": yfinance_revenue,
                    "diff_percent": round(diff_percent, 2),
                }
            )

    mismatches.sort(key=lambda item: item["fiscal_quarter"], reverse=True)
    return {
        "checked_quarters": checked,
        "tolerance_percent": tolerance_percent,
        "mismatches": mismatches,
    }
