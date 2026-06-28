from datetime import datetime
import json
from pathlib import Path
import re
import sys
from textwrap import shorten
from typing import Any

import pandas as pd


# このファイル(analyzers/company_analysis/generate_company_report.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402
from utils.tickers import load_tickers  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "tickers.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
PROMPT_PATH = PROJECT_ROOT / "prompts" / "company_analysis_prompt.md"
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
REPORT_DIR = PROJECT_ROOT / "reports" / "company_analysis"


def load_json(path: Path, default: Any) -> Any:
    """JSONを読み込みます。存在しない場合はdefaultを返します。"""
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_text(path: Path) -> str:
    """テキストファイルを読み込みます。存在しない場合は空文字を返します。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_knowledge() -> dict[str, str]:
    """knowledgeディレクトリ内のMarkdownを読み込みます。"""
    if not KNOWLEDGE_DIR.exists():
        return {}
    return {
        path.name: path.read_text(encoding="utf-8")
        for path in sorted(KNOWLEDGE_DIR.glob("*.md"))
    }


def format_number(value: Any) -> str:
    if value is None or value == "":
        return "不明"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value)

    abs_number = abs(number)
    if abs_number >= 1_000_000_000_000:
        return f"{number / 1_000_000_000_000:.2f}兆"
    if abs_number >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f}十億"
    if abs_number >= 1_000_000:
        return f"{number / 1_000_000:.2f}百万"
    return f"{number:,.2f}"


def format_currency(value: Any, currency: str | None = None) -> str:
    text = format_number(value)
    if text == "不明":
        return text
    return f"{text} {currency}" if currency else text


def format_percent(value: Any) -> str:
    if value is None or value == "":
        return "不明"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value)
    return f"{number:.2f}%"


def format_ratio_as_percent(value: Any) -> str:
    if value is None or value == "":
        return "不明"
    try:
        number = float(value) * 100
    except (TypeError, ValueError):
        return str(value)
    return f"{number:.2f}%"


def sanitize_report_text(value: Any) -> str:
    """レポート本文では投資判断に見える表現を中立化します。"""
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


def load_prices(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    prices = pd.read_csv(path)
    if prices.empty or "date" not in prices.columns:
        return pd.DataFrame()
    prices = prices.copy()
    prices["date"] = pd.to_datetime(prices["date"])
    return prices.sort_values("date").reset_index(drop=True)


def price_summary(prices: pd.DataFrame) -> dict[str, Any]:
    if prices.empty:
        return {
            "first_date": None,
            "last_date": None,
            "first_close": None,
            "last_close": None,
            "change_percent": None,
            "latest_volume": None,
            "average_volume_30d": None,
        }

    first = prices.iloc[0]
    last = prices.iloc[-1]
    first_close = safe_float(first.get("close"))
    last_close = safe_float(last.get("close"))
    change_percent = None
    if first_close not in (None, 0) and last_close is not None:
        change_percent = ((last_close - first_close) / first_close) * 100

    return {
        "first_date": first["date"].strftime("%Y-%m-%d"),
        "last_date": last["date"].strftime("%Y-%m-%d"),
        "first_close": first_close,
        "last_close": last_close,
        "change_percent": change_percent,
        "latest_volume": safe_float(last.get("volume")),
        "average_volume_30d": safe_float(prices.tail(30)["volume"].mean()),
    }


def summarize_news(news_items: list[dict[str, Any]], limit: int = 5) -> list[str]:
    lines = []
    for item in news_items[:limit]:
        title = sanitize_report_text(item.get("title") or "タイトル不明")
        publisher = item.get("publisher") or "不明"
        published_at = item.get("published_at") or "日時不明"
        summary = sanitize_report_text(item.get("summary") or "要約なし")
        summary = shorten(str(summary), width=180, placeholder="...")
        lines.append(f"- {published_at} / {publisher}: {title}。要約: {summary}")
    return lines or ["- 取得済みニュースがありません。"]


def classify_event(title: str | None) -> str:
    text = (title or "").lower()
    rules = [
        ("決算", ["earnings", "revenue", "eps", "guidance", "quarter"]),
        ("新製品", ["launch", "new product", "chip", "ai", "iphone", "gpu"]),
        ("大型契約", ["contract", "deal", "partnership", "customer"]),
        ("M&A", ["acquire", "acquisition", "merger", "m&a"]),
        ("配当", ["dividend"]),
        ("自社株買い", ["buyback", "repurchase"]),
        ("規制", ["regulation", "regulatory", "antitrust", "tariff", "export"]),
        ("訴訟", ["lawsuit", "legal", "court", "sues"]),
        ("CEO交代", ["ceo", "cfo", "executive"]),
        ("設備投資", ["capex", "factory", "data center", "investment"]),
    ]
    for label, keywords in rules:
        if any(keyword in text for keyword in keywords):
            return label
    return "その他"


def summarize_events(events: list[dict[str, Any]], limit: int = 5) -> list[str]:
    if not events:
        return ["- イベントDBに保存済みイベントがありません。"]

    def sort_key(event: dict[str, Any]) -> float:
        value = safe_float(event.get("price_change_percent"))
        return abs(value) if value is not None else -1

    sorted_events = sorted(events, key=sort_key, reverse=True)
    lines = []
    for event in sorted_events[:limit]:
        category = classify_event(event.get("title"))
        change = format_percent(event.get("price_change_percent"))
        close_price = format_number(event.get("close_price"))
        volume = format_number(event.get("volume"))
        title = sanitize_report_text(event.get("title") or "タイトル不明")
        lines.append(
            "- "
            f"{event.get('published_at') or '日時不明'} / {category}: "
            f"{title} "
            f"(終値: {close_price}, 前日比: {change}, 出来高: {volume})"
        )
    return lines


def build_ai_analysis(company: dict[str, Any], financials: dict[str, Any], price: dict[str, Any]) -> dict[str, list[str]]:
    strengths: list[str] = []
    weaknesses: list[str] = []
    watch_points: list[str] = []
    risks: list[str] = []

    sector = company.get("sector")
    market_cap = safe_float(company.get("market_cap"))
    operating_margin = safe_float(financials.get("operating_margin"))
    profit_margin = safe_float(financials.get("profit_margin"))
    fcf = safe_float(financials.get("free_cash_flow"))
    rnd = safe_float(financials.get("research_and_development"))
    current_ratio = safe_float(financials.get("current_ratio"))
    beta = safe_float(company.get("beta"))
    price_change = safe_float(price.get("change_percent"))

    if market_cap and market_cap >= 100_000_000_000:
        strengths.append("時価総額が大きく、事業基盤や市場での存在感が確認できます。")
    if operating_margin and operating_margin >= 0.20:
        strengths.append("営業利益率が高く、収益性の強さが示されています。")
    if profit_margin and profit_margin >= 0.15:
        strengths.append("純利益率が高く、売上から利益を残す力があります。")
    if fcf and fcf > 0:
        strengths.append("フリーキャッシュフローがプラスで、現金創出力があります。")
    if rnd and rnd > 0:
        strengths.append("研究開発費を計上しており、将来成長への投資が続いています。")

    if beta and beta >= 1.5:
        weaknesses.append("βが高く、市場全体より株価変動が大きくなる可能性があります。")
    if current_ratio is not None and current_ratio < 1:
        weaknesses.append("流動比率が1倍を下回っており、短期的な財務余力は追加確認が必要です。")
    if price_change and price_change > 150:
        weaknesses.append("過去期間で株価が大きく上昇しており、期待先行の可能性があります。")

    watch_points.append("売上成長、営業利益率、FCFが同時に改善しているかを継続確認する必要があります。")
    watch_points.append("直近ニュース後の出来高と株価反応が継続的か、一時的かを確認する価値があります。")
    if sector:
        watch_points.append(f"{sector} セクター全体の需要変化と競争環境を確認する必要があります。")

    risks.append("yfinance由来データのため、項目欠損や仕様変更の影響を受ける可能性があります。")
    risks.append("ニュースの市場反応は短期的な需給やマクロ環境にも左右されると考えられます。")
    if beta and beta >= 1.5:
        risks.append("高いボラティリティにより、企業価値と短期株価が乖離する可能性があります。")

    return {
        "strengths": strengths or ["現時点のデータだけでは明確な強みを断定できません。追加調査が必要です。"],
        "weaknesses": weaknesses or ["現時点のデータだけでは明確な弱みを断定できません。追加調査が必要です。"],
        "watch_points": watch_points,
        "risks": risks,
    }


def research_priority(company: dict[str, Any], financials: dict[str, Any], news_items: list[dict[str, Any]]) -> str:
    score = 0
    if safe_float(company.get("market_cap")) and safe_float(company.get("market_cap")) >= 100_000_000_000:
        score += 1
    if safe_float(financials.get("operating_margin")) and safe_float(financials.get("operating_margin")) >= 0.15:
        score += 1
    if safe_float(financials.get("free_cash_flow")) and safe_float(financials.get("free_cash_flow")) > 0:
        score += 1
    if safe_float(financials.get("research_and_development")) and safe_float(financials.get("research_and_development")) > 0:
        score += 1
    if len(news_items) >= 5:
        score += 1

    stars = ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆", "★★★★☆", "★★★★★"]
    return stars[min(max(score - 1, 0), 4)]


def ai_comment(company: dict[str, Any], financials: dict[str, Any], priority: str) -> str:
    name = company.get("company_name") or company.get("ticker") or "この企業"
    sector = company.get("sector") or "不明セクター"
    revenue = format_currency(financials.get("total_revenue"), financials.get("currency"))
    op_margin = format_ratio_as_percent(financials.get("operating_margin"))
    fcf = format_currency(financials.get("free_cash_flow"), financials.get("currency"))
    return (
        f"{name}は{sector}に属し、売上規模は{revenue}、営業利益率は{op_margin}、"
        f"FCFは{fcf}です。調査優先度は{priority}で、投資判断ではなく、"
        "成長性・収益性・ニュース後の市場反応を継続確認する価値があります。"
    )


def knowledge_summary(knowledge: dict[str, str]) -> str:
    if not knowledge:
        return "knowledge/ は未読み込みです。"
    names = ", ".join(sorted(knowledge.keys()))
    return f"参照Knowledge: {names}"


def generate_report(ticker: str, prompt: str, knowledge: dict[str, str]) -> str:
    company = load_json(PROJECT_ROOT / "storage" / "raw" / "companies" / f"{ticker}.json", {})
    financials = load_json(PROJECT_ROOT / "storage" / "raw" / "financials" / f"{ticker}.json", {})
    news_items = load_json(PROJECT_ROOT / "storage" / "raw" / "news" / f"{ticker}.json", [])
    events = load_json(PROJECT_ROOT / "storage" / "events" / f"{ticker}_events.json", [])
    prices = load_prices(PROJECT_ROOT / "storage" / "raw" / "prices" / f"{ticker}.csv")
    price = price_summary(prices)

    currency = company.get("currency") or financials.get("currency")
    analysis = build_ai_analysis(company, financials, price)
    priority = research_priority(company, financials, news_items)

    report_lines = [
        f"# {ticker} 企業分析レポート",
        "",
        "> このレポートは投資判断ではありません。個別の投資判断や価格水準の提示は行いません。",
        f"> {knowledge_summary(knowledge)}",
        f"> プロンプト: {PROMPT_PATH.name} ({len(prompt)} chars)",
        "",
        "## 1. 企業概要",
        "",
        f"- 会社名: {company.get('company_name') or '不明'}",
        f"- セクター: {company.get('sector') or '不明'}",
        f"- 業種: {company.get('industry') or '不明'}",
        f"- 時価総額: {format_currency(company.get('market_cap'), currency)}",
        f"- 事業概要: {company.get('business_summary') or '不明'}",
        "",
        "## 2. 株価状況",
        "",
        f"- 対象期間: {price.get('first_date') or '不明'} から {price.get('last_date') or '不明'}",
        f"- 期間初値終値ベース: {format_number(price.get('first_close'))} から {format_number(price.get('last_close'))}",
        f"- 期間騰落率: {format_percent(price.get('change_percent'))}",
        f"- 52週高値: {format_number(company.get('52_week_high'))}",
        f"- 52週安値: {format_number(company.get('52_week_low'))}",
        f"- 最新出来高: {format_number(price.get('latest_volume'))}",
        f"- 30日平均出来高: {format_number(price.get('average_volume_30d'))}",
        "",
        "## 3. 財務状況",
        "",
        f"- 会計年度: {financials.get('fiscal_year') or '不明'}",
        f"- 直近四半期: {financials.get('fiscal_quarter') or '不明'}",
        f"- 売上: {format_currency(financials.get('total_revenue'), financials.get('currency'))}",
        f"- 粗利益: {format_currency(financials.get('gross_profit'), financials.get('currency'))}",
        f"- 営業利益: {format_currency(financials.get('operating_income'), financials.get('currency'))}",
        f"- 純利益: {format_currency(financials.get('net_income'), financials.get('currency'))}",
        f"- EPS: {format_number(financials.get('eps'))}",
        f"- 希薄化後EPS: {format_number(financials.get('diluted_eps'))}",
        f"- 営業利益率: {format_ratio_as_percent(financials.get('operating_margin'))}",
        f"- 純利益率: {format_ratio_as_percent(financials.get('profit_margin'))}",
        f"- 研究開発費: {format_currency(financials.get('research_and_development'), financials.get('currency'))}",
        f"- FCF: {format_currency(financials.get('free_cash_flow'), financials.get('currency'))}",
        f"- 現金: {format_currency(financials.get('cash'), financials.get('currency'))}",
        f"- 総資産: {format_currency(financials.get('total_assets'), financials.get('currency'))}",
        f"- 総負債: {format_currency(financials.get('total_liabilities'), financials.get('currency'))}",
        f"- 自己資本: {format_currency(financials.get('shareholders_equity'), financials.get('currency'))}",
        f"- 長期債務: {format_currency(financials.get('long_term_debt'), financials.get('currency'))}",
        f"- 流動比率: {format_number(financials.get('current_ratio'))}",
        "",
        "## 4. 最近のニュース",
        "",
        *summarize_news(news_items, limit=5),
        "",
        "## 5. イベント整理",
        "",
        *summarize_events(events, limit=5),
        "",
        "## 6. AI分析",
        "",
        "### 強み",
        "",
        *[f"- {item}" for item in analysis["strengths"]],
        "",
        "### 弱み",
        "",
        *[f"- {item}" for item in analysis["weaknesses"]],
        "",
        "### 今後の注目ポイント",
        "",
        *[f"- {item}" for item in analysis["watch_points"]],
        "",
        "### リスク要因",
        "",
        *[f"- {item}" for item in analysis["risks"]],
        "",
        "## 7. 調査優先度",
        "",
        priority,
        "",
        "この評価は投資判断ではなく、追加調査する価値を示すものです。",
        "",
        "## 8. AIコメント",
        "",
        ai_comment(company, financials, priority),
        "",
    ]
    return "\n".join(report_lines)


def main() -> int:
    try:
        settings = load_yaml(SETTINGS_PATH)
    except Exception as error:
        print(f"settings.yaml 読み込みエラー: {error}")
        return 1

    logger = setup_logger(PROJECT_ROOT, settings, "compass.company_analysis")
    timezone = get_timezone(settings)
    started_at = datetime.now(timezone)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("Compass v1.0-alpha - Company analysis report generation")
    logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("保存先: %s", REPORT_DIR)

    try:
        tickers = load_tickers(CONFIG_PATH)
    except Exception as error:
        logger.exception("設定読み込みエラー: %s", error)
        return 1

    prompt = load_text(PROMPT_PATH)
    knowledge = load_knowledge()

    successful_tickers: list[str] = []
    failed_tickers: list[str] = []

    for ticker in tickers:
        try:
            report = generate_report(ticker, prompt, knowledge)
            output_path = REPORT_DIR / f"{ticker}.md"
            output_path.write_text(report, encoding="utf-8")
            successful_tickers.append(ticker)
            logger.info("[OK] %s: レポート保存完了 -> %s", ticker, output_path)
        except Exception as error:
            failed_tickers.append(ticker)
            logger.exception("[NG] %s: エラー - %s", ticker, error)

    finished_at = datetime.now(timezone)
    logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info("生成成功銘柄: %s", ", ".join(successful_tickers) or "なし")
    logger.info("失敗銘柄: %s", ", ".join(failed_tickers) or "なし")
    logger.info(
        "処理結果: 成功 %s / 失敗 %s / 合計 %s",
        len(successful_tickers),
        len(failed_tickers),
        len(tickers),
    )

    return 1 if failed_tickers else 0


if __name__ == "__main__":
    sys.exit(main())
