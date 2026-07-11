# Human Review Process

Compassの改善は、人間のレビューを通ってからLearningに進みます。

```text
Feedback
↓
Decision
↓
Learning
↓
Knowledge
```

## Feedback

Validation結果から改善候補を生成します。

## Decision

改善候補をProposalに変換し、人間がApprove、Reject、Deferredを判断します。

Review状態の正本は `memory/decision/proposal_index.json` です。`reports/proposals/proposal_index.json` はWorkspaceとAPI向けのミラーであり、日次Runnerが変わっても承認状態を失わないようにします。

## Learning

Approved ProposalのみをLearning Packageへ取り込みます。

Feedback Historyの正本は `memory/feedback/feedback_history.json` とし、Proposalの根拠を継続的に追跡します。

## Knowledge

Knowledge更新は人間が別途実施します。

CompassはKnowledgeを自動更新しません。
