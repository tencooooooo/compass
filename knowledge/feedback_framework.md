# Feedback Framework

Feedback Engineは、DiscoveryとValidationを比較してCompassの分析品質を評価するための層です。

FeedbackはLearning Engineではありません。Compassはこの段階で自動学習せず、改善候補を人間へ提示します。

## Purpose

- Discovery候補が後続Validationでどう評価されたか確認する。
- Scoring、Confidence、Sector、Eventの評価が妥当だったか整理する。
- Knowledge更新候補を生成する。
- 成功パターンと失敗パターンを蓄積する。

## Inputs

- Discovery Memory
- Validation Memory
- Company Memory
- Sector Memory
- Scoring results
- Human-maintained Knowledge

## Outputs

- `reports/feedback/feedback_summary.md`
- `reports/feedback/improvement_candidates.md`
- `reports/feedback/feedback_history.json`

## Human Review

Knowledge更新は必ず人間が確認してから行います。

Feedback Engineの役割は、改善候補を提示することです。
