from __future__ import annotations

from typing import Any


def format_number(value: Any) -> str:
    if value is None:
        return "N/A"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value)
    if abs(number) >= 1_000_000_000_000:
        return f"{number / 1_000_000_000_000:.2f}T"
    if abs(number) >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f}B"
    if abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.2f}M"
    return f"{number:,.2f}"


def format_percent(value: Any) -> str:
    if value is None:
        return "N/A"
    try:
        return f"{float(value):.2f}%"
    except (TypeError, ValueError):
        return str(value)


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "対象データがありません。"
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(str(cell) if cell not in (None, "") else "N/A" for cell in row) + " |" for row in rows]
    return "\n".join([header_line, separator, *body])


def sector_composition_table(sector_summaries: list[dict[str, Any]]) -> str:
    rows = [
        [
            sector["sector"],
            sector["ticker_count"],
            ", ".join(sector["tickers"]),
        ]
        for sector in sector_summaries
    ]
    return markdown_table(["セクター", "銘柄数", "銘柄"], rows)


def sector_metric_table(sector_summaries: list[dict[str, Any]]) -> str:
    rows = [
        [
            sector["sector"],
            sector["ticker_count"],
            format_number(sector.get("average_score")),
            format_number(sector.get("average_per")),
            format_number(sector.get("average_eps")),
            format_percent(sector.get("average_momentum_1m")),
            sector.get("news_count", 0),
        ]
        for sector in sector_summaries
    ]
    return markdown_table(["セクター", "銘柄数", "平均スコア", "平均PER", "平均EPS", "平均1Mモメンタム", "ニュース件数"], rows)


def trend_table(sector_summaries: list[dict[str, Any]]) -> str:
    rows = [
        [
            sector["sector"],
            sector["trend"]["momentum"],
            sector["trend"]["news"],
            sector["trend"]["financial_health"],
        ]
        for sector in sector_summaries
    ]
    return markdown_table(["セクター", "Momentum", "News", "Financial Health"], rows)


def top_news_lines(top_news: list[dict[str, Any]]) -> list[str]:
    if not top_news:
        return ["- 注目ニュースは取得できていません。"]
    lines = []
    for item in top_news:
        title = item.get("title") or "タイトル不明"
        ticker = item.get("ticker") or "N/A"
        publisher = item.get("publisher") or "N/A"
        published_at = item.get("published_at") or "N/A"
        lines.append(f"- {published_at} / {ticker} / {publisher}: {title}")
    return lines


def top_event_lines(top_events: list[dict[str, Any]]) -> list[str]:
    if not top_events:
        return ["- Event Databaseに表示可能なイベントがありません。"]
    lines = []
    for event in top_events:
        change = format_percent(event.get("price_change_percent"))
        volume = format_number(event.get("volume"))
        lines.append(
            f"- {event.get('published_at') or 'N/A'} / {event.get('ticker') or 'N/A'}: "
            f"{event.get('title') or 'タイトル不明'} "
            f"(株価反応: {change}, 出来高: {volume})"
        )
    return lines


def render_market_psychology(market: dict[str, Any], sector_summaries: list[dict[str, Any]], knowledge_excerpt: str) -> str:
    avg_momentum = market.get("average_momentum_1m")
    positive_sectors = sum(1 for sector in sector_summaries if (sector.get("average_momentum_1m") or 0) >= 0)
    total_sectors = len(sector_summaries)
    news_count = market.get("news_count", 0)

    if avg_momentum is None:
        tone = "市場心理はデータ不足のため判断を控える必要があります。"
    elif avg_momentum >= 5 and positive_sectors >= max(1, total_sectors / 2):
        tone = "市場はややリスクオン傾向と考えられます。"
    elif avg_momentum <= -5:
        tone = "市場はややリスクオフ寄りと考えられます。"
    else:
        tone = "市場は中立から方向感を探る局面と考えられます。"

    return (
        f"{tone} ただし、これは対象銘柄群の価格・ニュース・イベントから見たルールベースの整理であり、"
        f"市場全体を断定するものではありません。ニュース件数は {news_count} 件で、"
        f"ポジティブなモメンタムのセクターは {positive_sectors}/{total_sectors} です。\n\n"
        f"参照Knowledge: market_psychology.md\n\n{knowledge_excerpt}"
    )


def render_market_summary(
    market: dict[str, Any],
    sector_summaries: list[dict[str, Any]],
    top_news: list[dict[str, Any]],
    top_events: list[dict[str, Any]],
    psychology: str,
    comparative_reports: list[str],
) -> str:
    lines = [
        "# Market Intelligence Summary",
        "",
        "> このレポートは投資判断ではありません。市場、セクター、企業を理解するための調査補助です。",
        "",
        "## 市場全体",
        "",
        f"- 取得対象企業数: {market.get('ticker_count', 0)}",
        f"- セクター数: {market.get('sector_count', 0)}",
        f"- 市場全体の1Mモメンタム平均: {format_percent(market.get('average_momentum_1m'))}",
        f"- ニュース件数: {market.get('news_count', 0)}",
        f"- Event数: {market.get('event_count', 0)}",
        f"- 比較分析レポート: {', '.join(comparative_reports) if comparative_reports else 'N/A'}",
        "",
        "### セクター構成",
        "",
        sector_composition_table(sector_summaries),
        "",
        "### 注目ニュース",
        "",
        *top_news_lines(top_news),
        "",
        "### 注目イベント",
        "",
        *top_event_lines(top_events),
        "",
        "## セクター分析",
        "",
        sector_metric_table(sector_summaries),
        "",
        "## 市場トレンド",
        "",
        trend_table(sector_summaries),
        "",
        "## 市場心理",
        "",
        psychology,
        "",
        "## Notes",
        "",
        "Market Intelligence Engineは企業ランキングを生成しません。市場構造、セクター状態、市場心理を整理するための基盤です。",
        "",
    ]
    return "\n".join(lines)


def render_sector_summary(sector_summaries: list[dict[str, Any]], ticker_rows: list[dict[str, Any]]) -> str:
    lines = [
        "# Sector Summary",
        "",
        "> 存在するセクターのみを対象にした集計です。平均値は対象銘柄数が少ない場合、偏りが大きくなる可能性があります。",
        "",
    ]
    rows_by_sector = {sector["sector"]: [row for row in ticker_rows if row.get("sector") == sector["sector"]] for sector in sector_summaries}

    for sector in sector_summaries:
        lines.extend(
            [
                f"## {sector['sector']}",
                "",
                f"- 銘柄数: {sector['ticker_count']}",
                f"- 銘柄: {', '.join(sector['tickers'])}",
                f"- 平均スコア: {format_number(sector.get('average_score'))}",
                f"- 平均PER: {format_number(sector.get('average_per'))}",
                f"- 平均EPS: {format_number(sector.get('average_eps'))}",
                f"- 平均1Mモメンタム: {format_percent(sector.get('average_momentum_1m'))}",
                f"- ニュース件数: {sector.get('news_count', 0)}",
                "",
                "### Trend",
                "",
                f"- Momentum: {sector['trend']['momentum']}",
                f"- News: {sector['trend']['news']}",
                f"- Financial Health: {sector['trend']['financial_health']}",
                "",
                "### Companies",
                "",
                markdown_table(
                    ["Ticker", "会社名", "Score", "PER", "EPS", "1M Momentum", "News"],
                    [
                        [
                            row["ticker"],
                            row.get("company_name") or "N/A",
                            format_number(row.get("total_score")),
                            format_number(row.get("trailing_pe")),
                            format_number(row.get("eps")),
                            format_percent(row.get("momentum_1m")),
                            row.get("news_count", 0),
                        ]
                        for row in rows_by_sector.get(sector["sector"], [])
                    ],
                ),
                "",
            ]
        )
    return "\n".join(lines)
