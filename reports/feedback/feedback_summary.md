# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-10T20:37:58.400691-05:00
- Validation件数: 3845
- 完了済みValidation: 1593
- 未完了Validation: 2252
- 成功率: 45.57%
- 失敗率: 41.31%
- Result Counts(期間完了分): {'Excellent': 564, 'Poor': 658, 'Neutral': 209, 'Good': 162}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 564 | 564 | 100.00% | 0.00% |
| Good | 162 | 162 | 100.00% | 0.00% |
| Neutral | 2461 | 209 | 0.00% | 0.00% |
| Poor | 658 | 658 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 455 | 193 | {'Excellent': 82, 'Good': 10, 'Neutral': 14, 'Poor': 87, 'Unknown': 0, 'Pending': 262} |
| Mid Score (60-74) | 2485 | 984 | {'Excellent': 394, 'Good': 94, 'Neutral': 122, 'Poor': 374, 'Unknown': 0, 'Pending': 1501} |
| Low Score (<60) | 905 | 416 | {'Excellent': 88, 'Good': 58, 'Neutral': 73, 'Poor': 197, 'Unknown': 0, 'Pending': 489} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2140 | 939 | 52.82% | 36.00% | 105 |
| Medium | 1705 | 654 | 35.17% | 48.93% | 104 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2880 | 1110 | 43.96% | 41.98% | 156 |
| Moderate | 505 | 207 | 46.86% | 40.58% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 750 | 339 | 35.99% | 51.33% | 43 |
| Consumer Cyclical | 245 | 112 | 20.54% | 61.61% | 20 |
| Technology | 2850 | 1142 | 50.88% | 36.34% | 146 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 3845 | 1593 | {'Excellent': 564, 'Good': 162, 'Neutral': 209, 'Poor': 658, 'Unknown': 0, 'Pending': 2252} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2203 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2178 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1449 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 726 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 704 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2056 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1974 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1306 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 658 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 586 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
