# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-30T21:17:47.584073-04:00
- Validation件数: 3670
- 完了済みValidation: 1456
- 未完了Validation: 2214
- 成功率: 46.63%
- 失敗率: 39.77%
- Result Counts(期間完了分): {'Excellent': 526, 'Poor': 579, 'Neutral': 198, 'Good': 153}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 526 | 526 | 100.00% | 0.00% |
| Good | 153 | 153 | 100.00% | 0.00% |
| Neutral | 2412 | 198 | 0.00% | 0.00% |
| Poor | 579 | 579 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 1095 | 395 | {'Excellent': 201, 'Good': 34, 'Neutral': 52, 'Poor': 108, 'Unknown': 0, 'Pending': 700} |
| Low Score (<60) | 2575 | 1061 | {'Excellent': 325, 'Good': 119, 'Neutral': 146, 'Poor': 471, 'Unknown': 0, 'Pending': 1514} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 901 | 52.16% | 36.51% | 102 |
| Medium | 1630 | 555 | 37.66% | 45.05% | 96 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2730 | 988 | 45.75% | 39.57% | 145 |
| Moderate | 480 | 192 | 44.79% | 41.67% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 313 | 36.74% | 49.52% | 43 |
| Consumer Cyclical | 225 | 103 | 21.36% | 62.14% | 17 |
| Technology | 2730 | 1040 | 52.12% | 34.62% | 138 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3665 | 1456 | {'Excellent': 526, 'Good': 153, 'Neutral': 198, 'Poor': 579, 'Unknown': 0, 'Pending': 2209} |

## Success Patterns

- Momentum: 2061 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2037 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1355 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 679 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 658 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1814 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1737 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1148 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 579 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 512 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
