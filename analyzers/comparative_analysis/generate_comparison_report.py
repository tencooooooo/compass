from datetime import datetime
import json
from pathlib import Path
import re
import sys
from textwrap import shorten
from typing import Any

import pandas as pd


# このファイル(analyzers/comparative_analysis/generate_comparison_report.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
PROMPT_PATH = PROJECT_ROOT / "prompts" / "comparative_analysis_prompt.md"
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
REPORT_DIR = PROJECT_ROOT / "reports" / "comparative_analysis"
COMPANY_REPORT_DIR = PROJECT_ROOT / "reports" / "company_analysis"

MEGA_TECH = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
SEMICONDUCTOR = ["NVDA", "AMD"]
STAR_VALUES = ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆", "★★★★☆", "★★★★★"]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_knowledge_names() -> str:
    if not KNOWLEDGE_DIR.exists():
        return "knowledge/ は未読み込みです。"
    names = ", ".join(path.name for path in sorted(KNOWLEDGE_DIR.glob("*.md")))
    return f"参照Knowledge: {names}"


def sanitize_report_text(value: Any) -> str:
    text = "" if value is None else str(value)
    replacements = [
        (r"\bBuy(?:ing)?\b", "投資判断表現"),
        (r"\bSell(?:ing)?\b", "投資判断表現"),
        (r"\bHold(?:ing)?\b", "投資判断表現"),
        (r"買い", "投資判断表現"),
        (r"売り", "投資判断表現"),
        (r"目標株価", "価格水準"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def safe_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return None if pd.isna(number) else number


def format_number(value: Any) -> str:
    number = safe_float(value)
    if number is None:
        return "N/A"

    abs_number = abs(number)
    if abs_number >= 1_000_000_000_000:
        return f"{number / 1_000_000_000_000:.2f}T"
    if abs_number >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f}B"
    if abs_number >= 1_000_000:
        return f"{number / 1_000_000:.2f}M"
    return f"{number:,.2f}"


def format_currency(value: Any, currency: str | None = None) -> str:
    text = format_number(value)
    if text == "N/A":
        return text
    return f"{text} {currency}" if currency else text


def format_percent(value: Any) -> str:
    number = safe_float(value)
    if number is None:
        return "N/A"
    return f"{number:.2f}%"


def format_ratio_as_percent(value: Any) -> str:
    number = safe_float(value)
    if number is None:
        return "N/A"
    return f"{number * 100:.2f}%"


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "対象データがありません。"
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(str(cell) if cell not in (None, "") else "N/A" for cell in row) + " |" for row in rows]
    return "\n".join([header_line, separator, *body])


def load_prices(ticker: str) -> pd.DataFrame:
    path = PROJECT_ROOT / "storage" / "raw" / "prices" / f"{ticker}.csv"
    if not path.exists():
        return pd.DataFrame()
    prices = pd.read_csv(path)
    if prices.empty or "date" not in prices.columns:
        return pd.DataFrame()
    prices = prices.copy()
    prices["date"] = pd.to_datetime(prices["date"])
    return prices.sort_values("date").reset_index(drop=True)


def momentum_for_days(prices: pd.DataFrame, days: int) -> float | None:
    if prices.empty or len(prices) < 2:
        return None
    latest = prices.iloc[-1]
    target_date = latest["date"] - pd.Timedelta(days=days)
    candidates = prices[prices["date"] <= target_date]
    if candidates.empty:
        return None
    base = safe_float(candidates.iloc[-1]["close"])
    latest_close = safe_float(latest["close"])
    if base in (None, 0) or latest_close is None:
        return None
    return ((latest_close - base) / base) * 100


def momentum_summary(ticker: str) -> dict[str, Any]:
    prices = load_prices(ticker)
    if prices.empty:
        return {
            "1w": None,
            "1m": None,
            "3m": None,
            "6m": None,
            "1y": None,
            "5y": None,
            "latest_volume": None,
            "average_volume": None,
        }
    latest = prices.iloc[-1]
    first = prices.iloc[0]
    latest_close = safe_float(latest["close"])
    first_close = safe_float(first["close"])
    five_year = None
    if first_close not in (None, 0) and latest_close is not None:
        five_year = ((latest_close - first_close) / first_close) * 100
    return {
        "1w": momentum_for_days(prices, 7),
        "1m": momentum_for_days(prices, 30),
        "3m": momentum_for_days(prices, 90),
        "6m": momentum_for_days(prices, 180),
        "1y": momentum_for_days(prices, 365),
        "5y": five_year,
        "latest_volume": safe_float(latest.get("volume")),
        "average_volume": safe_float(prices.tail(30)["volume"].mean()),
    }


def load_ticker_data(ticker: str) -> dict[str, Any]:
    return {
        "ticker": ticker,
        "company": load_json(PROJECT_ROOT / "storage" / "raw" / "companies" / f"{ticker}.json", {}),
        "financials": load_json(PROJECT_ROOT / "storage" / "raw" / "financials" / f"{ticker}.json", {}),
        "news": load_json(PROJECT_ROOT / "storage" / "raw" / "news" / f"{ticker}.json", []),
        "events": load_json(PROJECT_ROOT / "storage" / "events" / f"{ticker}_events.json", []),
        "company_report": load_text(COMPANY_REPORT_DIR / f"{ticker}.md"),
        "momentum": momentum_summary(ticker),
    }


def extract_section(markdown: str, start_heading: str, stop_headings: list[str]) -> str:
    start = markdown.find(start_heading)
    if start < 0:
        return ""
    content_start = start + len(start_heading)
    stop_positions = [markdown.find(stop, content_start) for stop in stop_headings]
    stop_positions = [pos for pos in stop_positions if pos >= 0]
    end = min(stop_positions) if stop_positions else len(markdown)
    return markdown[content_start:end].strip()


def first_bullets(section: str, limit: int = 2) -> list[str]:
    bullets = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(sanitize_report_text(stripped[2:]))
        if len(bullets) >= limit:
            break
    return bullets


def extract_company_report_summary(markdown: str) -> dict[str, str]:
    strengths_section = extract_section(markdown, "### 強み", ["### 弱み", "### 今後の注目ポイント", "### リスク要因", "## 7."])
    watch_section = extract_section(markdown, "### 今後の注目ポイント", ["### リスク要因", "## 7."])
    priority_section = extract_section(markdown, "## 7. 調査優先度", ["## 8. AIコメント"])

    priority = "N/A"
    for star in STAR_VALUES:
        if star in priority_section:
            priority = star
            break

    return {
        "strengths": "<br>".join(first_bullets(strengths_section)) or "N/A",
        "watch_points": "<br>".join(first_bullets(watch_section)) or "N/A",
        "priority": priority,
    }


def target_table(data: list[dict[str, Any]]) -> str:
    rows = []
    for item in data:
        company = item["company"]
        rows.append([
            item["ticker"],
            company.get("company_name") or "N/A",
            company.get("sector") or "N/A",
            company.get("industry") or "N/A",
        ])
    return markdown_table(["Ticker", "会社名", "セクター", "業種"], rows)


def basic_table(data: list[dict[str, Any]]) -> str:
    rows = []
    for item in data:
        c = item["company"]
        rows.append([
            item["ticker"],
            format_currency(c.get("market_cap"), c.get("currency")),
            format_number(c.get("trailing_pe")),
            format_number(c.get("forward_pe")),
            format_number(c.get("peg_ratio")),
            format_number(c.get("price_to_book")),
            format_number(c.get("eps")),
            format_percent(c.get("dividend_yield")),
            format_number(c.get("52_week_high")),
            format_number(c.get("52_week_low")),
        ])
    return markdown_table(
        ["Ticker", "時価総額", "PER", "Forward PER", "PEG", "PBR", "EPS", "配当利回り", "52週高値", "52週安値"],
        rows,
    )


def financial_table(data: list[dict[str, Any]]) -> str:
    rows = []
    for item in data:
        f = item["financials"]
        currency = f.get("currency")
        rows.append([
            item["ticker"],
            format_currency(f.get("total_revenue"), currency),
            format_currency(f.get("operating_income"), currency),
            format_currency(f.get("net_income"), currency),
            format_currency(f.get("ebitda"), currency),
            format_number(f.get("eps")),
            format_ratio_as_percent(f.get("operating_margin")),
            format_ratio_as_percent(f.get("profit_margin")),
            format_currency(f.get("free_cash_flow"), currency),
            format_currency(f.get("research_and_development"), currency),
            format_currency(f.get("cash"), currency),
            format_currency(f.get("total_liabilities"), currency),
            format_currency(f.get("shareholders_equity"), currency),
        ])
    return markdown_table(
        ["Ticker", "売上", "営業利益", "純利益", "EBITDA", "EPS", "営業利益率", "利益率", "FCF", "研究開発費", "現金", "負債", "自己資本"],
        rows,
    )


def momentum_table(data: list[dict[str, Any]]) -> str:
    rows = []
    for item in data:
        m = item["momentum"]
        rows.append([
            item["ticker"],
            format_percent(m.get("1w")),
            format_percent(m.get("1m")),
            format_percent(m.get("3m")),
            format_percent(m.get("6m")),
            format_percent(m.get("1y")),
            format_percent(m.get("5y")),
            format_number(m.get("latest_volume")),
            format_number(m.get("average_volume")),
        ])
    return markdown_table(
        ["Ticker", "1週間", "1か月", "3か月", "6か月", "1年", "5年", "直近出来高", "平均出来高"],
        rows,
    )


def news_event_section(data: list[dict[str, Any]]) -> str:
    sections = []
    for item in data:
        ticker = item["ticker"]
        sections.append(f"### {ticker}")
        sections.append("")
        news_items = item["news"][:3] if isinstance(item["news"], list) else []
        if news_items:
            sections.append("直近ニュース:")
            for news in news_items:
                title = sanitize_report_text(news.get("title") or "タイトル不明")
                publisher = news.get("publisher") or "N/A"
                published_at = news.get("published_at") or "N/A"
                sections.append(f"- {published_at} / {publisher}: {title}")
        else:
            sections.append("- 取得済みニュースがありません。")

        events = item["events"][:3] if isinstance(item["events"], list) else []
        if events:
            sections.append("")
            sections.append("イベントDB:")
            for event in events:
                title = sanitize_report_text(event.get("title") or "タイトル不明")
                change = format_percent(event.get("price_change_percent"))
                volume = format_number(event.get("volume"))
                sections.append(f"- {event.get('published_at') or 'N/A'}: {title} / 株価反応: {change}, 出来高: {volume}")
        sections.append("")
    return "\n".join(sections).strip()


def strengths_watch_table(data: list[dict[str, Any]]) -> str:
    rows = []
    for item in data:
        summary = extract_company_report_summary(item["company_report"])
        rows.append([item["ticker"], summary["strengths"], summary["watch_points"]])
    return markdown_table(["Ticker", "強み", "注意点"], rows)


def priority_table(data: list[dict[str, Any]]) -> str:
    rows = []
    for item in data:
        summary = extract_company_report_summary(item["company_report"])
        rows.append([item["ticker"], summary["priority"]])
    return markdown_table(["Ticker", "調査優先度"], rows)


def report_summary(report_name: str, data: list[dict[str, Any]]) -> str:
    if not data:
        return (
            "比較対象銘柄がないため、現時点では特徴を整理できません。今後対象銘柄が追加された際に、"
            "基本情報、財務、株価モメンタム、ニュース、イベントDBを横断して比較します。"
            "このレポートは投資判断ではなく、追加調査の入口を作るためのものです。"
        )

    sectors = sorted({item["company"].get("sector") or "N/A" for item in data})
    top_market_cap = max(
        data,
        key=lambda item: safe_float(item["company"].get("market_cap")) or 0,
    )
    high_margin = max(
        data,
        key=lambda item: safe_float(item["financials"].get("operating_margin")) or -999,
    )
    strong_momentum = max(
        data,
        key=lambda item: safe_float(item["momentum"].get("1y")) or -999,
    )

    return (
        f"{report_name}では、{len(data)}銘柄を対象に比較しています。対象セクターは{', '.join(sectors)}です。"
        f"時価総額では{top_market_cap['ticker']}の存在感が大きく、営業利益率では{high_margin['ticker']}が相対的に高い水準です。"
        f"1年モメンタムでは{strong_momentum['ticker']}が目立ちます。"
        "一方で、株価上昇率だけでは企業価値や将来性を判断できないため、売上規模、利益率、FCF、研究開発費、"
        "バリュエーション、ニュース材料、イベント後の出来高を分けて確認する必要があります。"
        "この比較は投資判断ではなく、追加調査する候補と論点を整理するための補助資料です。"
        "今後はスコアリングやランキングへ拡張し、相対的な特徴をより継続的に追える形へ育てていきます。"
    )


def generate_report(report_title: str, tickers: list[str], prompt: str) -> str:
    data = [load_ticker_data(ticker) for ticker in tickers]
    if not tickers:
        data = []

    lines = [
        f"# {report_title}",
        "",
        "> この比較レポートは投資判断ではありません。個別の投資判断や価格水準の提示は行いません。",
        f"> {load_knowledge_names()}",
        f"> プロンプト: {PROMPT_PATH.name} ({len(prompt)} chars)",
        "",
        "## 1. 比較対象",
        "",
        target_table(data),
        "",
        "## 2. 基本情報比較",
        "",
        basic_table(data),
        "",
        "## 3. 財務比較",
        "",
        financial_table(data),
        "",
        "## 4. 株価モメンタム比較",
        "",
        momentum_table(data),
        "",
        "## 5. ニュース・イベント比較",
        "",
        news_event_section(data) if data else "対象銘柄がありません。",
        "",
        "## 6. 強み・注意点の比較",
        "",
        strengths_watch_table(data),
        "",
        "## 7. 調査優先度比較",
        "",
        priority_table(data),
        "",
        "この調査優先度は投資判断ではなく、追加調査する価値の目安です。",
        "",
        "## 8. まとめ",
        "",
        report_summary(report_title, data),
        "",
    ]
    return "\n".join(lines)


def filter_existing_tickers(tickers: list[str], allowed: list[str]) -> list[str]:
    allowed_set = set(allowed)
    return [ticker for ticker in tickers if ticker in allowed_set]


def technology_tickers(tickers: list[str]) -> list[str]:
    selected = []
    for ticker in tickers:
        company = load_json(PROJECT_ROOT / "storage" / "raw" / "companies" / f"{ticker}.json", {})
        if company.get("sector") == "Technology":
            selected.append(ticker)
    return selected


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.comparative_analysis")
    timezone = get_timezone(settings)
    started_at = datetime.now(timezone)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("Compass v1.0-alpha - Comparative analysis report generation")
    logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("保存先: %s", REPORT_DIR)

    try:
        tickers = load_tickers(CONFIG_PATH)
    except Exception as error:
        logger.exception("設定読み込みエラー: %s", error)
        return 1

    prompt = load_text(PROMPT_PATH)
    report_specs = [
        ("market_overview.md", "Market Overview 比較分析レポート", tickers),
        ("mega_tech_comparison.md", "Mega Tech 比較分析レポート", filter_existing_tickers(tickers, MEGA_TECH)),
        ("semiconductor_comparison.md", "Semiconductor 比較分析レポート", filter_existing_tickers(tickers, SEMICONDUCTOR)),
        ("sector_technology.md", "Technology Sector 比較分析レポート", technology_tickers(tickers)),
    ]

    success_count = 0
    failure_count = 0
    for filename, title, target_tickers in report_specs:
        try:
            report = generate_report(title, target_tickers, prompt)
            output_path = REPORT_DIR / filename
            output_path.write_text(report, encoding="utf-8")
            success_count += 1
            logger.info("[OK] %s: レポート保存完了 -> %s", filename, output_path)
        except Exception as error:
            failure_count += 1
            logger.exception("[NG] %s: エラー - %s", filename, error)

    finished_at = datetime.now(timezone)
    logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("処理結果: 成功 %s / 失敗 %s / 合計 %s", success_count, failure_count, len(report_specs))

    return 1 if failure_count else 0


if __name__ == "__main__":
    sys.exit(main())
