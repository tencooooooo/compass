from __future__ import annotations

from typing import Any


def format_value(value: Any) -> str:
    if value is None or value == "":
        return "N/A"
    if isinstance(value, float):
        return f"{value:,.4f}"
    return str(value)


def bullet_lines(items: list[str]) -> list[str]:
    return [f"- {item}" for item in items] if items else ["- N/A"]


def metric_lines(metrics: dict[str, Any]) -> list[str]:
    if not metrics:
        return ["- N/A"]
    return [f"- {key}: {format_value(value)}" for key, value in metrics.items()]


def render_explanation(score_result: dict[str, Any]) -> str:
    ticker = score_result["ticker"]
    company_name = score_result.get("company_name") or ticker
    lines = [
        f"# {ticker} Scoring Explanation",
        "",
        "> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。",
        "",
        "## Summary",
        "",
        f"- Company: {company_name}",
        f"- Total Score: {score_result['total_score']} / {score_result['max_score']}",
        f"- Confidence: {score_result['confidence']['level']}",
        f"- Evidence: {', '.join(score_result['evidence_sources'])}",
        "",
        "## Confidence",
        "",
        score_result["confidence"]["level"],
        "",
        "理由",
        "",
        *bullet_lines(score_result["confidence"]["reasons"]),
        "",
    ]

    for category, part in score_result["scores"].items():
        lines.extend([
            f"## {category}",
            "",
            f"{part['score']}点",
            "",
            "理由",
            "",
            *bullet_lines(part.get("reasons", [])),
            "",
            "Evidence",
            "",
            *bullet_lines(part.get("evidence", [])),
            "",
            "使用データ",
            "",
            *metric_lines(part.get("metrics", {})),
            "",
        ])
        missing = part.get("missing_data", [])
        if missing:
            lines.extend([
                "欠損・計算不可",
                "",
                *bullet_lines(missing),
                "",
            ])

    lines.extend([
        "## Note",
        "",
        "CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。",
        "",
    ])
    return "\n".join(lines)
