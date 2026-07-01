from __future__ import annotations

import hashlib
from typing import Any


def short_hash(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def proposal_id(date_key: str, area: str, candidate: str) -> str:
    safe_area = "".join(char if char.isalnum() else "-" for char in area.lower()).strip("-") or "general"
    return f"PROP-{date_key}-{safe_area}-{short_hash(candidate)}"


def recommendation_for(candidate: dict[str, Any], overview: dict[str, Any]) -> str:
    completed_count = int(overview.get("completed_count") or 0)
    priority = str(candidate.get("priority") or "").lower()
    if completed_count == 0:
        return "Review Later"
    if priority == "high" and completed_count >= 10:
        return "Approve"
    if priority == "low":
        return "Review Later"
    return "Review Later"


def risk_for(candidate: dict[str, Any], overview: dict[str, Any]) -> list[str]:
    risks = [
        "Knowledgeを自動更新すると、単発のノイズを恒久ルール化する可能性があります。",
        "Validationの完了件数が少ない場合、改善候補は仮説として扱う必要があります。",
    ]
    if int(overview.get("completed_count") or 0) == 0:
        risks.insert(0, "完了済みValidationがないため、承認判断には時期尚早です。")
    if candidate.get("priority") == "High":
        risks.append("High priorityでも、人間レビューなしにScoringやKnowledgeへ反映してはいけません。")
    return risks


def expected_effect_for(candidate: dict[str, Any]) -> list[str]:
    area = str(candidate.get("area") or "")
    if area == "Validation Horizon":
        return [
            "未完了Validationを成功/失敗判定から分離できます。",
            "FeedbackとLearningの過剰反応を抑制できます。",
        ]
    if area == "Score Accuracy":
        return [
            "高スコア企業の評価根拠をより検証しやすくできます。",
            "Scoring weightの見直し候補を明示できます。",
        ]
    if area == "Sector Accuracy":
        return [
            "セクター固有の過大評価または過小評価を発見しやすくできます。",
            "Market IntelligenceとDiscoveryの接続を改善できます。",
        ]
    return ["Feedback Historyを人間がレビューしやすくなります。"]


def build_proposals(feedback_history: list[dict[str, Any]], date_key: str, timestamp: str) -> list[dict[str, Any]]:
    if not feedback_history:
        return []
    latest = feedback_history[-1]
    overview = latest.get("overview", {})
    source_feedback = latest.get("generated_at")
    proposals: list[dict[str, Any]] = []
    for item in latest.get("improvement_candidates", []) or []:
        candidate = item if isinstance(item, dict) else {}
        area = str(candidate.get("area") or "General")
        candidate_text = str(candidate.get("candidate") or "Review feedback candidate")
        proposals.append(
            {
                "proposal_id": proposal_id(date_key, area, candidate_text),
                "title": f"{area}: {candidate_text[:60]}",
                "target": area,
                "reason": candidate.get("reason", ""),
                "evidence": [
                    f"Feedback generated at: {source_feedback or 'N/A'}",
                    f"Validation count: {overview.get('validation_count', 0)}",
                    f"Completed Validation count: {overview.get('completed_count', 0)}",
                    f"Pending Validation count: {overview.get('pending_count', 0)}",
                ],
                "impact_scope": [
                    "Knowledge update candidate",
                    "Future Learning Engine input",
                    "Human review workflow",
                ],
                "expected_effect": expected_effect_for(candidate),
                "risks": risk_for(candidate, overview),
                "recommendation": recommendation_for(candidate, overview),
                "candidate": candidate_text,
                "priority": candidate.get("priority", "Medium"),
                "source_feedback": source_feedback,
                "created": timestamp,
                "updated": timestamp,
            }
        )
    return proposals


def render_proposal_markdown(proposals: list[dict[str, Any]], date_key: str) -> str:
    lines = [
        f"# Decision Proposals - {date_key}",
        "",
        "> CompassはKnowledge、Scoring、Ruleを自動更新しません。このProposalは人間レビュー用です。",
        "",
    ]
    if not proposals:
        lines.extend(["## No Proposals", "", "Feedback Historyに改善候補がありません。", ""])
        return "\n".join(lines)

    for proposal in proposals:
        lines.extend(
            [
                f"## {proposal['proposal_id']}",
                "",
                f"- Proposal ID: {proposal['proposal_id']}",
                f"- 対象: {proposal['target']}",
                f"- 推奨: {proposal['recommendation']}",
                f"- Priority: {proposal['priority']}",
                "",
                "### 理由",
                "",
                f"- {proposal['reason'] or 'N/A'}",
                "",
                "### 根拠",
                "",
            ]
        )
        lines.extend([f"- {item}" for item in proposal["evidence"]])
        lines.extend(["", "### 影響範囲", ""])
        lines.extend([f"- {item}" for item in proposal["impact_scope"]])
        lines.extend(["", "### 期待効果", ""])
        lines.extend([f"- {item}" for item in proposal["expected_effect"]])
        lines.extend(["", "### リスク", ""])
        lines.extend([f"- {item}" for item in proposal["risks"]])
        lines.extend(["", "### Review Options", "", "- Approve", "- Reject", "- Review Later", ""])
    return "\n".join(lines)


def render_knowledge_update_candidate(proposals: list[dict[str, Any]], date_key: str) -> str:
    lines = [
        f"# Knowledge Update Candidates - {date_key}",
        "",
        "> このファイルはKnowledge更新候補です。Knowledge本体は更新していません。",
        "",
    ]
    if not proposals:
        lines.extend(["## No Candidates", "", "提案対象の改善候補がありません。", ""])
        return "\n".join(lines)

    for proposal in proposals:
        lines.extend(
            [
                f"## {proposal['proposal_id']}",
                "",
                f"- 変更対象: {proposal['target']}",
                f"- 変更理由: {proposal['reason'] or 'N/A'}",
                f"- 関連Feedback: {proposal.get('source_feedback') or 'N/A'}",
                f"- 関連Validation: {', '.join(proposal['evidence'][1:])}",
                "",
                "### 根拠",
                "",
            ]
        )
        lines.extend([f"- {item}" for item in proposal["evidence"]])
        lines.extend(["", "### Candidate Text", "", proposal["candidate"], ""])
    return "\n".join(lines)
