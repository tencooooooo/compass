# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-07-30T18:57:37.932983-04:00
- Validation件数: 665
- 完了済みValidation: 105
- 未完了Validation: 560
- 成功率: 43.81%
- 失敗率: 44.76%
- Result Counts(期間完了分): {'Excellent': 37, 'Poor': 47, 'Neutral': 12, 'Good': 9}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 37 | 37 | 100.00% | 0.00% |
| Good | 9 | 9 | 100.00% | 0.00% |
| Neutral | 572 | 12 | 0.00% | 0.00% |
| Poor | 47 | 47 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 190 | 28 | {'Excellent': 9, 'Good': 1, 'Neutral': 3, 'Poor': 15, 'Unknown': 0, 'Pending': 162} |
| Mid Score (60-74) | 450 | 72 | {'Excellent': 27, 'Good': 8, 'Neutral': 9, 'Poor': 28, 'Unknown': 0, 'Pending': 378} |
| Low Score (<60) | 25 | 5 | {'Excellent': 1, 'Good': 0, 'Neutral': 0, 'Poor': 4, 'Unknown': 0, 'Pending': 20} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 430 | 67 | 38.81% | 47.76% | 9 |
| Medium | 235 | 38 | 52.63% | 39.47% | 3 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 180 | 13 | 23.08% | 76.92% | 0 |
| Moderate | 25 | 0 | N/A | N/A | 0 |
| Unknown | 460 | 92 | 46.74% | 40.22% | 12 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 190 | 30 | 23.33% | 70.00% | 2 |
| Consumer Cyclical | 65 | 12 | 33.33% | 50.00% | 2 |
| Technology | 410 | 63 | 55.56% | 31.75% | 8 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 665 | 105 | {'Excellent': 37, 'Good': 9, 'Neutral': 12, 'Poor': 47, 'Unknown': 0, 'Pending': 560} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 141 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 138 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 92 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 46 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 43 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 143 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 141 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 94 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 47 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 45 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
