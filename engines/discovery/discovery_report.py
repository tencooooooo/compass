from __future__ import annotations

from typing import Any


def bullet_lines(items: list[str]) -> list[str]:
    return [f"- {item}" for item in items] if items else ["- N/A"]


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "対象データがありません。"
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(str(cell) if cell not in (None, "") else "N/A" for cell in row) + " |" for row in rows]
    return "\n".join([header_line, separator, *body])


def render_candidates_report(candidates: list[dict[str, Any]], market_summary: dict[str, Any]) -> str:
    rows = [
        [
            candidate["ticker"],
            candidate["company"],
            candidate["sector"],
            candidate["discovery_score"],
            candidate["status"],
            candidate["confidence"],
        ]
        for candidate in candidates
    ]
    top = candidates[0] if candidates else None
    lines = [
        "# Discovery Candidates",
        "",
        "> このレポートは投資判断ではありません。市場、セクター、企業の文脈から追加調査候補を整理するものです。",
        "",
        "## Market Context",
        "",
        f"- 対象企業数: {market_summary.get('ticker_count', 'N/A')}",
        f"- セクター数: {market_summary.get('sector_count', 'N/A')}",
        f"- 市場平均スコア: {market_summary.get('average_score', 'N/A')}",
        f"- 1M市場モメンタム平均: {market_summary.get('average_momentum_1m', 'N/A')}",
        f"- ニュース件数: {market_summary.get('news_count', 'N/A')}",
        f"- Event数: {market_summary.get('event_count', 'N/A')}",
        "",
        "## Candidate Summary",
        "",
        markdown_table(["Ticker", "Company", "Sector", "Discovery Score", "Status", "Confidence"], rows),
        "",
    ]
    if top:
        lines.extend(
            [
                "## Top Candidate",
                "",
                top["ticker"],
                "",
                "理由",
                "",
                *bullet_lines(top["discovery_reasons"][:5]),
                "",
                "Confidence",
                "",
                top["confidence"],
                "",
                "Evidence",
                "",
                *bullet_lines(top["evidence"]),
                "",
            ]
        )

    lines.extend(
        [
            "## Notes",
            "",
            "Discovery EngineはランキングAIではありません。Discovery Scoreは追加調査の優先論点を整理するための補助指標です。",
            "Growth HunterはこのDiscovery基盤の上で将来実装します。",
            "",
        ]
    )
    return "\n".join(lines)


def render_candidate_detail(candidate: dict[str, Any]) -> str:
    lines = [
        f"# {candidate['ticker']} Discovery Detail",
        "",
        "> この候補詳細は投資判断ではありません。追加調査の理由と注意点を説明するものです。",
        "",
        "## Company",
        "",
        f"- Company: {candidate['company']}",
        f"- Sector: {candidate['sector']}",
        f"- Industry: {candidate.get('industry') or 'N/A'}",
        "",
        "## Discovery Score",
        "",
        f"{candidate['discovery_score']} / 100",
        "",
        "## Discovery Reasons",
        "",
        *bullet_lines(candidate["discovery_reasons"]),
        "",
        "## Strengths",
        "",
        *bullet_lines(candidate["strengths"]),
        "",
        "## Watch Points",
        "",
        *bullet_lines(candidate["watch_points"]),
        "",
        "## Confidence",
        "",
        candidate["confidence"],
        "",
        "## Evidence",
        "",
        *bullet_lines(candidate["evidence"]),
        "",
        "## Missing Data",
        "",
        *bullet_lines(candidate["missing_data"]),
        "",
        "## Metrics",
        "",
    ]
    for key, value in candidate.get("metrics", {}).items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    return "\n".join(lines)
