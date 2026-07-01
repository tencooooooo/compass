from __future__ import annotations

from typing import Any


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "対象データがありません。"
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(str(cell) if cell not in (None, "") else "N/A" for cell in row) + " |" for row in rows]
    return "\n".join([header_line, separator, *body])


def adoption_rate(approved: int, total: int) -> float | None:
    if total == 0:
        return None
    return round(approved / total * 100, 2)


def build_learning_metrics(
    status_counts: dict[str, int],
    applied_count: int,
    knowledge_version: str,
) -> dict[str, Any]:
    total = sum(status_counts.values())
    return {
        "approved": status_counts.get("Approved", 0),
        "rejected": status_counts.get("Rejected", 0),
        "deferred": status_counts.get("Deferred", 0),
        "pending": status_counts.get("Pending", 0),
        "applied": applied_count,
        "proposal_count": total,
        "adoption_rate": adoption_rate(status_counts.get("Approved", 0), total),
        "knowledge_version": knowledge_version,
    }


def render_learning_package(
    date_key: str,
    approved: list[dict[str, Any]],
    proposal_details: dict[str, str],
    knowledge_candidates: dict[str, str],
    history_rows: list[dict[str, Any]],
    knowledge_version: str,
) -> str:
    lines = [
        f"# Learning Package - {date_key}",
        "",
        "> Human Approved Learning packageです。Knowledge本体は自動更新していません。",
        "",
        f"- Knowledge Version: {knowledge_version}",
        f"- Approved Proposal Count: {len(approved)}",
        "",
        "## Proposal一覧",
        "",
        markdown_table(
            ["Proposal ID", "Target", "Reviewer", "Updated"],
            [[p.get("proposal_id"), p.get("target"), p.get("reviewer"), p.get("updated")] for p in approved],
        ),
        "",
    ]
    if not approved:
        lines.extend(
            [
                "## No Approved Proposals",
                "",
                "ApprovedのProposalがないため、Learning Packageは空です。KnowledgeやScoring設定は変更していません。",
                "",
            ]
        )
    for proposal in approved:
        proposal_id = proposal.get("proposal_id")
        lines.extend(
            [
                f"## {proposal_id}",
                "",
                "### 採用理由",
                "",
                f"- StatusがApprovedです。Reviewer: {proposal.get('reviewer') or 'N/A'}",
                "",
                "### 期待効果",
                "",
                "- Proposal本文のExpected effectを参照してください。",
                "",
                "### 影響範囲",
                "",
                "- Knowledge candidate",
                "- Future scoring or rule review",
                "- Learning history",
                "",
                "### Knowledge候補",
                "",
                knowledge_candidates.get(str(proposal_id), "関連Knowledge候補が見つかりません。"),
                "",
                "### Scoring候補",
                "",
                "- Scoring設定の自動変更は行いません。必要な場合は人間レビュー後に別PRで反映します。",
                "",
                "### Proposal Detail",
                "",
                proposal_details.get(str(proposal_id), "Proposal本文が見つかりません。"),
                "",
            ]
        )
    lines.extend(
        [
            "## Review履歴",
            "",
            markdown_table(
                ["Proposal ID", "Applied Date", "Target", "Reviewer", "Knowledge Version"],
                [
                    [
                        row.get("proposal_id"),
                        row.get("applied_date"),
                        row.get("target"),
                        row.get("reviewer"),
                        row.get("knowledge_version"),
                    ]
                    for row in history_rows
                ],
            ),
            "",
            "## Guardrails",
            "",
            "- Learning EngineはKnowledgeを自動更新しません。",
            "- Approved ProposalのみをLearning対象にします。",
            "- Rejected、Deferred、Pendingは対象外です。",
            "- すべてのLearningは説明可能、追跡可能、Rollback可能である必要があります。",
            "",
        ]
    )
    return "\n".join(lines)


def render_learning_summary(date_key: str, metrics: dict[str, Any], approved: list[dict[str, Any]]) -> str:
    categories = sorted({str(item.get("target") or "Unknown") for item in approved})
    lines = [
        f"# Learning Summary - {date_key}",
        "",
        "> Learning SummaryはApproved Proposalの取り込み状況を示します。Knowledge本体は自動更新していません。",
        "",
        f"- 学習件数: {metrics.get('applied')}",
        f"- Proposal数: {metrics.get('proposal_count')}",
        f"- 採用率: {metrics.get('adoption_rate') if metrics.get('adoption_rate') is not None else 'N/A'}%",
        f"- Knowledge Version: {metrics.get('knowledge_version')}",
        "",
        "## Status Counts",
        "",
        f"- Approved: {metrics.get('approved')}",
        f"- Rejected: {metrics.get('rejected')}",
        f"- Deferred: {metrics.get('deferred')}",
        f"- Pending: {metrics.get('pending')}",
        "",
        "## 対象カテゴリ",
        "",
    ]
    lines.extend([f"- {category}" for category in categories] or ["- Approved Proposalがありません。"])
    lines.extend(["", "## 更新候補", ""])
    lines.extend(
        [f"- {item.get('proposal_id')}: {item.get('target')}" for item in approved]
        or ["- 現時点でLearning Packageへ取り込む更新候補はありません。"]
    )
    lines.append("")
    return "\n".join(lines)
