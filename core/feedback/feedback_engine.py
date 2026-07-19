from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]

from core.feedback.feedback_analyzer import analyze_feedback  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402


SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
REPORT_DIR = PROJECT_ROOT / "reports" / "feedback"
REPORT_HISTORY_PATH = REPORT_DIR / "feedback_history.json"
MEMORY_HISTORY_PATH = PROJECT_ROOT / "memory" / "feedback" / "feedback_history.json"


def fmt_percent(value: Any) -> str:
    if value is None:
        return "N/A"
    return f"{float(value):.2f}%"


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "対象データがありません。"
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(str(cell) if cell not in (None, "") else "N/A" for cell in row) + " |" for row in rows]
    return "\n".join([header_line, separator, *body])


def render_feedback_summary(analysis: dict[str, Any]) -> str:
    overview = analysis["overview"]
    sector_rows = [
        [
            item.get("sector"),
            item.get("total_count"),
            item.get("completed_count"),
            fmt_percent(item.get("success_rate")),
            fmt_percent(item.get("failure_rate")),
            item.get("result_counts", {}).get("Neutral", 0),
        ]
        for item in analysis.get("sector_accuracy", [])
    ]
    confidence_rows = [
        [
            item.get("confidence"),
            item.get("total_count"),
            item.get("completed_count"),
            fmt_percent(item.get("success_rate")),
            fmt_percent(item.get("failure_rate")),
            item.get("result_counts", {}).get("Neutral", 0),
        ]
        for item in analysis.get("confidence_accuracy", [])
    ]
    score_rows = [
        [item.get("bucket"), item.get("total_count"), item.get("completed_count"), item.get("result_counts")]
        for item in analysis.get("score_accuracy", [])
    ]
    event_rows = [
        [item.get("event_bucket"), item.get("total_count"), item.get("completed_count"), item.get("result_counts")]
        for item in analysis.get("event_accuracy", [])
    ]

    lines = [
        "# Feedback Summary",
        "",
        "> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。",
        "",
        "## Overview",
        "",
        f"- 生成日時: {analysis.get('generated_at')}",
        f"- Validation件数: {overview.get('validation_count')}",
        f"- 完了済みValidation: {overview.get('completed_count')}",
        f"- 未完了Validation: {overview.get('pending_count')}",
        f"- 成功率: {fmt_percent(overview.get('success_rate'))}",
        f"- 失敗率: {fmt_percent(overview.get('failure_rate'))}",
        f"- Result Counts(期間完了分): {overview.get('completed_result_counts')}",
        "",
        "## Discovery Accuracy",
        "",
        markdown_table(
            ["Result", "Total", "Completed", "Success Rate", "Failure Rate"],
            [
                [
                    item.get("validation_result"),
                    item.get("total_count"),
                    item.get("completed_count"),
                    fmt_percent(item.get("success_rate")),
                    fmt_percent(item.get("failure_rate")),
                ]
                for item in analysis.get("discovery_accuracy", [])
            ],
        ),
        "",
        "## Score Accuracy",
        "",
        markdown_table(["Score Bucket", "Total", "Completed", "Result Counts"], score_rows),
        "",
        "## Confidence Accuracy",
        "",
        markdown_table(["Confidence", "Total", "Completed", "Success Rate", "Failure Rate", "Neutral"], confidence_rows),
        "",
        "## Sector Accuracy",
        "",
        markdown_table(["Sector", "Total", "Completed", "Success Rate", "Failure Rate", "Neutral"], sector_rows),
        "",
        "## Event Accuracy",
        "",
        markdown_table(["Event Bucket", "Total", "Completed", "Result Counts"], event_rows),
        "",
        "## Success Patterns",
        "",
    ]
    success_patterns = analysis.get("success_patterns", [])
    lines.extend(
        [f"- {item['category']}: {item['count']} 件 / 例: {item['example']}" for item in success_patterns]
        or ["- 完了済みValidationの成功パターンはまだ十分に蓄積されていません。"]
    )
    lines.extend(["", "## Failure Patterns", ""])
    failure_patterns = analysis.get("failure_patterns", [])
    lines.extend(
        [f"- {item['category']}: {item['count']} 件 / 例: {item['example']}" for item in failure_patterns]
        or ["- 完了済みValidationの失敗パターンはまだ十分に蓄積されていません。"]
    )
    lines.extend(["", "## Notes", "", "Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。", ""])
    return "\n".join(lines)


def render_improvement_candidates(analysis: dict[str, Any]) -> str:
    lines = [
        "# Improvement Candidates",
        "",
        "> Knowledge更新候補です。Compassはこのファイルを根拠にKnowledgeを自動更新しません。",
        "",
        "## Knowledge更新候補",
        "",
    ]
    for item in analysis.get("improvement_candidates", []):
        lines.extend(
            [
                f"### {item.get('area')} / {item.get('priority')}",
                "",
                f"- 候補: {item.get('candidate')}",
                f"- 理由: {item.get('reason')}",
                "",
            ]
        )
    lines.extend(
        [
            "## Review Policy",
            "",
            "- Knowledge更新は人間が確認してから行います。",
            "- 完了済みValidationが少ない場合は、改善候補を仮説として扱います。",
            "- Learning EngineはFeedback Historyが十分に蓄積された後の将来機能です。",
            "",
        ]
    )
    return "\n".join(lines)


def load_history() -> list[dict[str, Any]]:
    for path in (MEMORY_HISTORY_PATH, REPORT_HISTORY_PATH):
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
    return []


def save_outputs(analysis: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "feedback_summary.md").write_text(render_feedback_summary(analysis), encoding="utf-8")
    (REPORT_DIR / "improvement_candidates.md").write_text(render_improvement_candidates(analysis), encoding="utf-8")
    history = load_history()
    # 同日の再実行・リトライで履歴が重複しないよう、同じ日付のエントリは最新結果で置き換える。
    date_key = str(analysis.get("generated_at") or "")[:10]
    history = [item for item in history if str(item.get("generated_at") or "")[:10] != date_key]
    history.append(
        {
            "generated_at": analysis.get("generated_at"),
            "overview": analysis.get("overview"),
            "improvement_candidates": analysis.get("improvement_candidates"),
        }
    )
    serialized = json.dumps(history, ensure_ascii=False, indent=2)
    MEMORY_HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    MEMORY_HISTORY_PATH.write_text(serialized, encoding="utf-8")
    REPORT_HISTORY_PATH.write_text(serialized, encoding="utf-8")


def main() -> int:
    settings = load_yaml(SETTINGS_PATH)
    logger = setup_logger(PROJECT_ROOT, settings, "compass.feedback")
    timezone = get_timezone(settings)
    generated_at = datetime.now(timezone).isoformat()

    logger.info("Compass Core 02 - Feedback Engine")
    analysis = analyze_feedback(PROJECT_ROOT, generated_at)
    save_outputs(analysis)
    logger.info("Feedback reports saved: %s", REPORT_DIR)
    logger.info("Improvement candidates: %s", len(analysis.get("improvement_candidates", [])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
