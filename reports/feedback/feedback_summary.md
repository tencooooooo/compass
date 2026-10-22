# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-21T20:21:59.473174-04:00
- Validation件数: 3520
- 完了済みValidation: 1309
- 未完了Validation: 2211
- 成功率: 46.83%
- 失敗率: 39.72%
- Result Counts(期間完了分): {'Excellent': 478, 'Poor': 520, 'Neutral': 176, 'Good': 135}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 478 | 478 | 100.00% | 0.00% |
| Good | 135 | 135 | 100.00% | 0.00% |
| Neutral | 2387 | 176 | 0.00% | 0.00% |
| Poor | 520 | 520 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 735 | 279 | {'Excellent': 97, 'Good': 35, 'Neutral': 38, 'Poor': 109, 'Unknown': 0, 'Pending': 456} |
| Low Score (<60) | 2785 | 1030 | {'Excellent': 381, 'Good': 100, 'Neutral': 138, 'Poor': 411, 'Unknown': 0, 'Pending': 1755} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 846 | 51.30% | 37.23% | 97 |
| Medium | 1480 | 463 | 38.66% | 44.28% | 79 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2580 | 856 | 46.73% | 38.79% | 124 |
| Moderate | 480 | 177 | 40.68% | 45.20% | 25 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 289 | 38.41% | 47.06% | 42 |
| Consumer Cyclical | 225 | 98 | 20.41% | 64.29% | 15 |
| Technology | 2580 | 922 | 52.28% | 34.82% | 119 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3515 | 1309 | {'Excellent': 478, 'Good': 135, 'Neutral': 176, 'Poor': 520, 'Unknown': 0, 'Pending': 2206} |

## Success Patterns

- Momentum: 1861 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1839 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1223 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 613 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 594 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1636 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1560 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1030 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 520 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 454 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
