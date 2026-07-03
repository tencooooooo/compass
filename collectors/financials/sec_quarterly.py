from __future__ import annotations

from datetime import date, datetime
from typing import Any


# XBRLタグは企業や年度で揺れるため、優先順の候補リストで解決します。
REVENUE_TAGS = [
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "Revenues",
    "SalesRevenueNet",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
]
NET_INCOME_TAGS = ["NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic"]
OPERATING_INCOME_TAGS = ["OperatingIncomeLoss"]
EPS_TAGS = ["EarningsPerShareDiluted", "EarningsPerShareBasic"]

# 四半期(約3ヶ月)の会計期間だけを対象にします。10-Kの通期値は除外します。
QUARTER_MIN_DAYS = 70
QUARTER_MAX_DAYS = 100

MAX_QUARTERS = 8


def _parse_date(value: Any) -> date | None:
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def _fiscal_quarter_label(period_end: date) -> str:
    quarter = ((period_end.month - 1) // 3) + 1
    return f"{period_end.year}-Q{quarter}"


def _is_quarterly_duration(entry: dict[str, Any]) -> bool:
    start = _parse_date(entry.get("start"))
    end = _parse_date(entry.get("end"))
    if start is None or end is None:
        return False
    return QUARTER_MIN_DAYS <= (end - start).days <= QUARTER_MAX_DAYS


def _quarterly_values(facts: dict[str, Any], tag_candidates: list[str], unit_keys: list[str]) -> dict[str, dict[str, Any]]:
    """タグ候補から四半期値を period_end 文字列 -> {val, filed} で返します。

    タグは年度や企業で切り替わる(例: ASC 606移行で Revenues -> RevenueFromContractWith...)ため、
    先頭一致で打ち切らず period_end 単位でマージします。同じ period_end が複数タグにある場合は
    候補リストの優先順位が高いタグの値を採用します。
    """
    merged: dict[str, dict[str, Any]] = {}
    for tag in tag_candidates:
        concept = facts.get(tag)
        if not isinstance(concept, dict):
            continue
        units = concept.get("units", {})
        entries: list[dict[str, Any]] = []
        for unit_key in unit_keys:
            unit_entries = units.get(unit_key)
            if isinstance(unit_entries, list):
                entries.extend(item for item in unit_entries if isinstance(item, dict))
        values: dict[str, dict[str, Any]] = {}
        for entry in entries:
            if not _is_quarterly_duration(entry):
                continue
            end = str(entry.get("end") or "")
            value = entry.get("val")
            if not end or not isinstance(value, (int, float)):
                continue
            filed = str(entry.get("filed") or "")
            # 同じ四半期が複数の提出書類に含まれるため、最新のfiledを採用します。
            existing = values.get(end)
            if existing is None or filed > existing["filed"]:
                values[end] = {"val": float(value), "filed": filed}
        for end, item in values.items():
            merged.setdefault(end, item)
    return merged


def extract_quarterly_financials(company_facts: dict[str, Any], max_quarters: int = MAX_QUARTERS) -> list[dict[str, Any]]:
    """SEC companyfacts(XBRL)から、scoring互換の四半期時系列を新しい順に作ります。"""
    facts = company_facts.get("facts", {}).get("us-gaap", {})
    if not isinstance(facts, dict) or not facts:
        return []

    revenue = _quarterly_values(facts, REVENUE_TAGS, ["USD"])
    net_income = _quarterly_values(facts, NET_INCOME_TAGS, ["USD"])
    operating_income = _quarterly_values(facts, OPERATING_INCOME_TAGS, ["USD"])
    eps = _quarterly_values(facts, EPS_TAGS, ["USD/shares"])

    period_ends: set[str] = set(revenue) | set(net_income) | set(operating_income) | set(eps)
    rows: list[dict[str, Any]] = []
    for period_end in period_ends:
        end_date = _parse_date(period_end)
        if end_date is None:
            continue
        rows.append(
            {
                "period_end": period_end,
                "fiscal_quarter": _fiscal_quarter_label(end_date),
                "total_revenue": revenue.get(period_end, {}).get("val"),
                "net_income": net_income.get(period_end, {}).get("val"),
                "operating_income": operating_income.get(period_end, {}).get("val"),
                "eps": eps.get(period_end, {}).get("val"),
            }
        )

    rows.sort(key=lambda row: row["period_end"], reverse=True)
    return rows[:max_quarters]
