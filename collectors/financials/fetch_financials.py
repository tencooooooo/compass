from datetime import datetime
import json
import math
from numbers import Integral, Real
from pathlib import Path
import sys
from typing import Any

import pandas as pd
import yfinance as yf


# このファイル(collectors/financials/fetch_financials.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]

from collectors.base import BaseCollector  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"


def normalize_value(value: Any) -> Any:
    """JSON保存しやすいように、取得値を基本的な型へ揃えます。"""
    if value in ("", "None", "N/A"):
        return None
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        return None if not math.isfinite(number) else number
    if isinstance(value, pd.Timestamp):
        return value.strftime("%Y-%m-%d")
    return str(value)


def safe_ratio(numerator: Any, denominator: Any) -> float | None:
    """割り算できない場合はNoneを返します。"""
    if numerator is None or denominator in (None, 0):
        return None
    try:
        result = float(numerator) / float(denominator)
    except (TypeError, ValueError, ZeroDivisionError):
        return None
    return None if not math.isfinite(result) else result


def get_statement(ticker_obj: yf.Ticker, attribute_names: list[str]) -> pd.DataFrame:
    """yfinanceの複数の属性名候補から、最初に取得できたDataFrameを返します。"""
    for attribute_name in attribute_names:
        try:
            statement = getattr(ticker_obj, attribute_name)
        except Exception:
            continue
        if isinstance(statement, pd.DataFrame) and not statement.empty:
            return statement
    return pd.DataFrame()


def latest_column(statement: pd.DataFrame) -> Any:
    """財務諸表の最新列を返します。列がない場合はNoneです。"""
    if statement.empty or len(statement.columns) == 0:
        return None
    return statement.columns[0]


def get_statement_value(statement: pd.DataFrame, row_names: list[str], column: Any = None) -> Any:
    """指定した複数の行名候補から、最初に見つかった値を返します。"""
    if statement.empty:
        return None

    target_column = column if column is not None else latest_column(statement)
    if target_column is None or target_column not in statement.columns:
        return None

    for row_name in row_names:
        if row_name in statement.index:
            return normalize_value(statement.loc[row_name, target_column])

    return None


def get_fiscal_year(column: Any) -> int | None:
    """財務諸表の列から会計年度を推定します。"""
    if column is None:
        return None
    try:
        return int(pd.Timestamp(column).year)
    except Exception:
        return None


def get_fiscal_quarter(column: Any) -> str | None:
    """四半期財務諸表の列から YYYY-Qn 形式を作ります。"""
    if column is None:
        return None
    try:
        timestamp = pd.Timestamp(column)
    except Exception:
        return None
    quarter = ((timestamp.month - 1) // 3) + 1
    return f"{timestamp.year}-Q{quarter}"


def build_quarterly_financials(statement: pd.DataFrame, limit: int = 5) -> list[dict[str, Any]]:
    """直近4四半期と前年同期を、成長率計算しやすい形で保存します。"""
    if statement.empty:
        return []

    rows: list[dict[str, Any]] = []
    for column in list(statement.columns)[:limit]:
        rows.append(
            {
                "period_end": normalize_value(column),
                "fiscal_quarter": get_fiscal_quarter(column),
                "total_revenue": get_statement_value(statement, ["Total Revenue"], column),
                "net_income": get_statement_value(statement, ["Net Income", "Net Income Common Stockholders"], column),
                "operating_income": get_statement_value(statement, ["Operating Income", "Operating Income Loss"], column),
                "eps": get_statement_value(
                    statement,
                    ["Basic EPS", "Diluted EPS", "Basic EPS From Continuing Operations", "Diluted EPS From Continuing Operations"],
                    column,
                ),
            }
        )
    return rows


class FinancialCollector(BaseCollector):
    """yfinanceから決算データを取得し、銘柄ごとにJSON保存するcollectorです。"""

    def __init__(self, project_root: Path, settings: dict, logger):
        super().__init__(project_root, settings, logger)
        self.config_path = project_root / "config" / "tickers.yaml"
        self.output_dir = self.output_root / "raw" / "financials"

    def fetch_financials(self, ticker: str) -> dict[str, Any]:
        """損益計算書、貸借対照表、キャッシュフローから主要指標を抽出します。"""
        ticker_obj = yf.Ticker(ticker)
        info = ticker_obj.info or {}

        income_statement = get_statement(ticker_obj, ["income_stmt", "financials"])
        quarterly_income_statement = get_statement(
            ticker_obj,
            ["quarterly_income_stmt", "quarterly_financials"],
        )
        balance_sheet = get_statement(ticker_obj, ["balance_sheet"])
        cashflow = get_statement(ticker_obj, ["cashflow"])

        if income_statement.empty and quarterly_income_statement.empty and balance_sheet.empty and cashflow.empty:
            raise ValueError("決算データの取得結果が空でした。")

        income_column = latest_column(income_statement)
        quarter_column = latest_column(quarterly_income_statement)
        balance_column = latest_column(balance_sheet)
        cashflow_column = latest_column(cashflow)

        total_revenue = get_statement_value(income_statement, ["Total Revenue"], income_column)
        gross_profit = get_statement_value(income_statement, ["Gross Profit"], income_column)
        operating_income = get_statement_value(
            income_statement,
            ["Operating Income", "Operating Income Loss"],
            income_column,
        )
        net_income = get_statement_value(
            income_statement,
            ["Net Income", "Net Income Common Stockholders"],
            income_column,
        )
        ebitda = get_statement_value(
            income_statement,
            ["EBITDA", "Normalized EBITDA"],
            income_column,
        )
        eps = get_statement_value(income_statement, ["Basic EPS"], income_column)
        diluted_eps = get_statement_value(income_statement, ["Diluted EPS"], income_column)

        operating_cash_flow = get_statement_value(
            cashflow,
            ["Operating Cash Flow", "Total Cash From Operating Activities"],
            cashflow_column,
        )
        capital_expenditure = get_statement_value(
            cashflow,
            ["Capital Expenditure", "Capital Expenditures", "Capital Expenditure Reported"],
            cashflow_column,
        )
        free_cash_flow = get_statement_value(cashflow, ["Free Cash Flow"], cashflow_column)
        if free_cash_flow is None and operating_cash_flow is not None and capital_expenditure is not None:
            free_cash_flow = float(operating_cash_flow) + float(capital_expenditure)

        current_assets = get_statement_value(balance_sheet, ["Current Assets"], balance_column)
        current_liabilities = get_statement_value(
            balance_sheet,
            ["Current Liabilities"],
            balance_column,
        )
        operating_margin = safe_ratio(operating_income, total_revenue)
        if operating_margin is None:
            operating_margin = normalize_value(info.get("operatingMargins"))

        profit_margin = safe_ratio(net_income, total_revenue)
        if profit_margin is None:
            profit_margin = normalize_value(info.get("profitMargins"))

        financials = {
            "ticker": ticker,
            "currency": normalize_value(info.get("financialCurrency") or info.get("currency")),
            "fiscal_year": get_fiscal_year(income_column),
            "fiscal_quarter": get_fiscal_quarter(quarter_column),
            "total_revenue": total_revenue,
            "gross_profit": gross_profit,
            "operating_income": operating_income,
            "net_income": net_income,
            "ebitda": ebitda,
            "eps": eps if eps is not None else normalize_value(info.get("trailingEps")),
            "diluted_eps": diluted_eps,
            "operating_margin": operating_margin,
            "profit_margin": profit_margin,
            "free_cash_flow": normalize_value(free_cash_flow),
            "capital_expenditure": capital_expenditure,
            "research_and_development": get_statement_value(
                income_statement,
                ["Research And Development", "Research Development"],
                income_column,
            ),
            "cash": get_statement_value(
                balance_sheet,
                ["Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments"],
                balance_column,
            ),
            "total_assets": get_statement_value(balance_sheet, ["Total Assets"], balance_column),
            "total_liabilities": get_statement_value(
                balance_sheet,
                ["Total Liabilities Net Minority Interest", "Total Liab"],
                balance_column,
            ),
            "shareholders_equity": get_statement_value(
                balance_sheet,
                ["Stockholders Equity", "Total Stockholder Equity"],
                balance_column,
            ),
            "long_term_debt": get_statement_value(
                balance_sheet,
                ["Long Term Debt", "Long Term Debt And Capital Lease Obligation"],
                balance_column,
            ),
            "current_ratio": safe_ratio(current_assets, current_liabilities),
            "quarterly_financials": build_quarterly_financials(quarterly_income_statement),
        }

        return {key: normalize_value(value) for key, value in financials.items()}

    def save_financials(self, ticker: str) -> tuple[bool, str]:
        """1銘柄分の決算データを取得し、JSONへ上書き保存します。"""
        output_path = self.output_dir / f"{ticker}.json"

        try:
            financials = self.fetch_financials(ticker)
            with output_path.open("w", encoding="utf-8") as file:
                json.dump(financials, file, ensure_ascii=False, indent=2)

            return True, f"{ticker}: 保存完了 -> {output_path}"
        except Exception as error:
            return False, f"{ticker}: エラー - {error}"

    def run(self) -> int:
        timezone = get_timezone(self.settings)
        started_at = datetime.now(timezone)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.logger.info("Compass v1.0-alpha - Financial data fetch")
        self.logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.logger.info("設定ファイル: %s", self.config_path)
        self.logger.info("保存先: %s", self.output_dir)

        try:
            tickers = load_tickers(self.config_path)
        except Exception as error:
            self.logger.exception("設定読み込みエラー: %s", error)
            return 1

        successful_tickers: list[str] = []
        failed_tickers: list[str] = []

        for ticker in tickers:
            ok, message = self.save_financials(ticker)
            if ok:
                successful_tickers.append(ticker)
                self.logger.info("[OK] %s", message)
            else:
                failed_tickers.append(ticker)
                self.logger.error("[NG] %s", message)

        finished_at = datetime.now(timezone)
        self.logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.logger.info("取得成功銘柄: %s", ", ".join(successful_tickers) or "なし")
        self.logger.info("失敗銘柄: %s", ", ".join(failed_tickers) or "なし")
        self.logger.info(
            "処理結果: 成功 %s / 失敗 %s / 合計 %s",
            len(successful_tickers),
            len(failed_tickers),
            len(tickers),
        )

        return 1 if failed_tickers else 0


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.financials")
    collector = FinancialCollector(PROJECT_ROOT, settings, logger)
    return collector.run()


if __name__ == "__main__":
    sys.exit(main())
