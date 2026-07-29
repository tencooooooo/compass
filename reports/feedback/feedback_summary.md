# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-07-29T18:53:26.792267-04:00
- Validation件数: 635
- 完了済みValidation: 102
- 未完了Validation: 533
- 成功率: 44.12%
- 失敗率: 44.12%
- Result Counts(期間完了分): {'Excellent': 36, 'Poor': 45, 'Neutral': 12, 'Good': 9}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 36 | 36 | 100.00% | 0.00% |
| Good | 9 | 9 | 100.00% | 0.00% |
| Neutral | 545 | 12 | 0.00% | 0.00% |
| Poor | 45 | 45 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 610 | 97 | {'Excellent': 35, 'Good': 9, 'Neutral': 12, 'Poor': 41, 'Unknown': 0, 'Pending': 513} |
| Low Score (<60) | 25 | 5 | {'Excellent': 1, 'Good': 0, 'Neutral': 0, 'Poor': 4, 'Unknown': 0, 'Pending': 20} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 410 | 65 | 38.46% | 47.69% | 9 |
| Medium | 225 | 37 | 54.05% | 37.84% | 3 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 155 | 10 | 20.00% | 80.00% | 0 |
| Moderate | 20 | 0 | N/A | N/A | 0 |
| Unknown | 460 | 92 | 46.74% | 40.22% | 12 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 180 | 30 | 23.33% | 70.00% | 2 |
| Consumer Cyclical | 65 | 12 | 33.33% | 50.00% | 2 |
| Technology | 390 | 60 | 56.67% | 30.00% | 8 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 635 | 102 | {'Excellent': 36, 'Good': 9, 'Neutral': 12, 'Poor': 45, 'Unknown': 0, 'Pending': 533} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 138 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 135 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 90 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 45 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 42 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 137 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 135 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 90 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 45 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 43 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
