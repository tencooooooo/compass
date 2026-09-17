# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-16T20:00:39.857011-04:00
- Validation件数: 2505
- 完了済みValidation: 654
- 未完了Validation: 1851
- 成功率: 42.97%
- 失敗率: 44.50%
- Result Counts(期間完了分): {'Excellent': 230, 'Poor': 291, 'Neutral': 82, 'Good': 51}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 230 | 230 | 100.00% | 0.00% |
| Good | 51 | 51 | 100.00% | 0.00% |
| Neutral | 1933 | 82 | 0.00% | 0.00% |
| Poor | 291 | 291 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 280 | 86 | {'Excellent': 28, 'Good': 6, 'Neutral': 7, 'Poor': 45, 'Unknown': 0, 'Pending': 194} |
| Mid Score (60-74) | 2050 | 534 | {'Excellent': 196, 'Good': 45, 'Neutral': 71, 'Poor': 222, 'Unknown': 0, 'Pending': 1516} |
| Low Score (<60) | 175 | 34 | {'Excellent': 6, 'Good': 0, 'Neutral': 4, 'Poor': 24, 'Unknown': 0, 'Pending': 141} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1760 | 446 | 44.84% | 43.50% | 52 |
| Medium | 745 | 208 | 38.94% | 46.63% | 30 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1655 | 382 | 41.62% | 45.29% | 50 |
| Moderate | 390 | 88 | 51.14% | 34.09% | 13 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 560 | 160 | 31.87% | 53.75% | 23 |
| Consumer Cyclical | 195 | 63 | 23.81% | 66.67% | 6 |
| Technology | 1750 | 431 | 49.88% | 37.82% | 53 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2505 | 654 | {'Excellent': 230, 'Good': 51, 'Neutral': 82, 'Poor': 291, 'Unknown': 0, 'Pending': 1851} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 860 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 843 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 559 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 281 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 267 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 913 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 873 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 580 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 291 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 253 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
