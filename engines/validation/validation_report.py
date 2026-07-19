from __future__ import annotations

from collections import Counter
from typing import Any

import pandas as pd

from engines.validation.thresholds import VALIDATION_THRESHOLDS


RESULT_ORDER = ["Excellent", "Good", "Neutral", "Poor"]


def validation_rule_lines(periods: dict[str, int]) -> list[str]:
    """実際の分類に使う期間別閾値(VALIDATION_THRESHOLDS)からルール説明を生成します。"""
    lines = []
    for label in periods:
        threshold = VALIDATION_THRESHOLDS.get(label)
        if not threshold:
            continue
        lines.append(
            f"- {label}: Excellent 騰落率 {threshold['excellent']}%以上 または ベンチマーク超過 {threshold['benchmark_excellent']}%以上 / "
            f"Good {threshold['good']}%以上 または {threshold['benchmark_good']}%以上 / "
            f"Poor {threshold['poor']}%以下 または ベンチマーク差 {threshold['benchmark_poor']}%以下。"
        )
    lines.append("- Neutral: 上記のいずれにも該当しない、または検証期間が未完了で判断材料が不足している状態。")
    return lines


def fmt_percent(value: Any) -> str:
    if value is None or pd.isna(value):
        return "N/A"
    return f"{float(value):.2f}%"


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "対象データがありません。"
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(str(cell) if cell not in (None, "") else "N/A" for cell in row) + " |" for row in rows]
    return "\n".join([header_line, separator, *body])


def collect_repeated_points(rows: list[dict[str, Any]], result_filter: set[str], key: str, limit: int = 5) -> list[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        if row.get("validation_result") not in result_filter:
            continue
        for point in row.get(key, []) or []:
            counter[str(point)] += 1
    return [point for point, _ in counter.most_common(limit)]


def render_validation_summary(
    rows: list[dict[str, Any]],
    generated_at: str,
    periods: dict[str, int],
    benchmark_name: str | None,
) -> str:
    complete_rows = [row for row in rows if row.get("period_complete")]
    incomplete_count = len(rows) - len(complete_rows)
    # 未完了期間はNeutral扱いで保存されるため、集計は完了分のみで行い未完了は別掲する。
    result_counts = Counter(row.get("validation_result") for row in complete_rows)
    returns = [row.get("return_percent") for row in complete_rows if row.get("return_percent") is not None]
    average_return = sum(returns) / len(returns) if returns else None

    ticker_rows = [
        [
            row.get("ticker"),
            row.get("period"),
            row.get("discovery_score"),
            fmt_percent(row.get("return_percent")),
            fmt_percent(row.get("benchmark_diff_percent")),
            fmt_percent(row.get("sector_diff_percent")),
            fmt_percent(row.get("sector_benchmark_diff_percent")),
            row.get("validation_result"),
            "Yes" if row.get("period_complete") else "No",
            row.get("confidence"),
        ]
        for row in rows
    ]

    good_features = collect_repeated_points(complete_rows, {"Excellent", "Good"}, "discovery_reasons")
    improvement_features = collect_repeated_points(complete_rows, {"Neutral", "Poor"}, "watch_points")
    if incomplete_count:
        improvement_features.insert(0, "検証期間が未完了の候補があり、十分な株価推移をまだ確認できません。")

    lines = [
        "# Validation Summary",
        "",
        "> このレポートは投資判断ではありません。Discovery結果を事後検証し、将来のLearning Engineに渡す根拠を蓄積するためのものです。",
        "",
        "## Overview",
        "",
        f"- 生成日時: {generated_at}",
        f"- 対象期間: {', '.join(periods.keys())}",
        f"- 検証対象数: {len(rows)}",
        f"- 期間完了済み: {len(complete_rows)}",
        f"- 期間未完了: {incomplete_count}",
        f"- ベンチマーク: {benchmark_name or 'N/A'}",
        f"- 平均騰落率(期間完了分): {fmt_percent(average_return)}",
        "",
        "## Result Counts(期間完了分)",
        "",
    ]
    for result in RESULT_ORDER:
        lines.append(f"- {result}: {result_counts.get(result, 0)}")
    lines.append(f"- Pending(期間未完了): {incomplete_count}")

    lines.extend(
        [
            "",
            "## Validation Table",
            "",
            markdown_table(
                [
                    "Ticker",
                    "Period",
                    "Discovery Score",
                    "Return",
                    "Benchmark Diff",
                    "Sector Diff",
                    "Sector ETF Diff",
                    "Result",
                    "Complete",
                    "Confidence",
                ],
                ticker_rows,
            ),
            "",
            "## 良かった特徴",
            "",
        ]
    )
    lines.extend([f"- {item}" for item in good_features] or ["- 期間完了済みの良好な特徴はまだ十分に蓄積されていません。"])
    lines.extend(["", "## 改善が必要な特徴", ""])
    lines.extend([f"- {item}" for item in improvement_features[:6]] or ["- 改善点は今後の履歴蓄積で確認します。"])
    lines.extend(
        [
            "",
            "## Validation Rules(期間別閾値)",
            "",
            *validation_rule_lines(periods),
            "",
            "## Notes",
            "",
            "Validationは自動学習ではありません。結果を蓄積し、将来のLearning EngineがスコアリングやDiscoveryルールを検証するための土台です。",
            "",
        ]
    )
    return "\n".join(lines)
