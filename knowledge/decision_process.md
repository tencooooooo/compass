# Decision Process

Decision Layerは、FeedbackからLearningへ進む前に人間レビューを挟むための層です。

```text
Feedback
↓
Proposal
↓
Review
↓
Learning
```

## Purpose

- Feedback Engineが生成した改善候補をProposalへ変換する。
- Knowledge更新候補を人間が確認しやすい形にする。
- CompassがKnowledge、Scoring、Ruleを自動変更しないようにする。

## Principle

Compassは自己改善するAIではありません。

Compassは改善案を提示するAIです。

Knowledgeを変更する権限は人間が持ちます。
