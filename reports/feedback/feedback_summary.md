# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-28T21:27:06.186308-04:00
- Validation件数: 3640
- 完了済みValidation: 1414
- 未完了Validation: 2226
- 成功率: 46.53%
- 失敗率: 39.89%
- Result Counts(期間完了分): {'Excellent': 510, 'Poor': 564, 'Neutral': 192, 'Good': 148}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 510 | 510 | 100.00% | 0.00% |
| Good | 148 | 148 | 100.00% | 0.00% |
| Neutral | 2418 | 192 | 0.00% | 0.00% |
| Poor | 564 | 564 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 1565 | 581 | {'Excellent': 274, 'Good': 56, 'Neutral': 70, 'Poor': 181, 'Unknown': 0, 'Pending': 984} |
| Low Score (<60) | 2075 | 833 | {'Excellent': 236, 'Good': 92, 'Neutral': 122, 'Poor': 383, 'Unknown': 0, 'Pending': 1242} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 889 | 51.86% | 36.78% | 101 |
| Medium | 1600 | 525 | 37.52% | 45.14% | 91 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2700 | 948 | 45.68% | 39.66% | 139 |
| Moderate | 480 | 190 | 44.21% | 42.11% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 305 | 37.05% | 48.85% | 43 |
| Consumer Cyclical | 225 | 101 | 20.79% | 62.38% | 17 |
| Technology | 2700 | 1008 | 51.98% | 34.92% | 132 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3635 | 1414 | {'Excellent': 510, 'Good': 148, 'Neutral': 192, 'Poor': 564, 'Unknown': 0, 'Pending': 2221} |

## Success Patterns

- Momentum: 1997 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1974 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1313 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 658 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 638 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1768 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1692 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1118 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 564 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 498 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
