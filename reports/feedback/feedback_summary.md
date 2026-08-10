# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-10T18:28:43.768448-04:00
- Validation件数: 905
- 完了済みValidation: 210
- 未完了Validation: 695
- 成功率: 44.76%
- 失敗率: 47.14%
- Result Counts(期間完了分): {'Excellent': 78, 'Poor': 99, 'Neutral': 17, 'Good': 16}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 78 | 78 | 100.00% | 0.00% |
| Good | 16 | 16 | 100.00% | 0.00% |
| Neutral | 712 | 17 | 0.00% | 0.00% |
| Poor | 99 | 99 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 110 | 23 | {'Excellent': 14, 'Good': 0, 'Neutral': 2, 'Poor': 7, 'Unknown': 0, 'Pending': 87} |
| Mid Score (60-74) | 480 | 108 | {'Excellent': 48, 'Good': 5, 'Neutral': 9, 'Poor': 46, 'Unknown': 0, 'Pending': 372} |
| Low Score (<60) | 315 | 79 | {'Excellent': 16, 'Good': 11, 'Neutral': 6, 'Poor': 46, 'Unknown': 0, 'Pending': 236} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 595 | 127 | 37.80% | 54.33% | 10 |
| Medium | 310 | 83 | 55.42% | 36.14% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 375 | 48 | 45.83% | 54.17% | 0 |
| Moderate | 70 | 7 | 71.43% | 28.57% | 0 |
| Unknown | 460 | 155 | 43.23% | 45.81% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 260 | 60 | 30.00% | 60.00% | 6 |
| Consumer Cyclical | 100 | 24 | 37.50% | 54.17% | 2 |
| Technology | 545 | 126 | 53.17% | 39.68% | 9 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 905 | 210 | {'Excellent': 78, 'Good': 16, 'Neutral': 17, 'Poor': 99, 'Unknown': 0, 'Pending': 695} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 290 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 282 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 188 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 94 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 86 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 301 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 297 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 198 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 99 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 95 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
