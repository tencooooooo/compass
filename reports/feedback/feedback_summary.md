# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-24T23:44:49.379606-05:00
- Validation件数: 4385
- 完了済みValidation: 1858
- 未完了Validation: 2527
- 成功率: 44.83%
- 失敗率: 43.38%
- Result Counts(期間完了分): {'Excellent': 642, 'Poor': 806, 'Neutral': 219, 'Good': 191}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 642 | 642 | 100.00% | 0.00% |
| Good | 191 | 191 | 100.00% | 0.00% |
| Neutral | 2746 | 219 | 0.00% | 0.00% |
| Poor | 806 | 806 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 460 | 197 | {'Excellent': 100, 'Good': 24, 'Neutral': 35, 'Poor': 38, 'Unknown': 0, 'Pending': 263} |
| Mid Score (60-74) | 1310 | 536 | {'Excellent': 159, 'Good': 63, 'Neutral': 63, 'Poor': 251, 'Unknown': 0, 'Pending': 774} |
| Low Score (<60) | 2615 | 1125 | {'Excellent': 383, 'Good': 104, 'Neutral': 121, 'Poor': 517, 'Unknown': 0, 'Pending': 1490} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2480 | 1087 | 52.35% | 37.81% | 107 |
| Medium | 1905 | 771 | 34.24% | 51.23% | 112 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3275 | 1330 | 42.93% | 44.66% | 165 |
| Moderate | 650 | 252 | 48.02% | 41.27% | 27 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 860 | 384 | 36.98% | 51.82% | 43 |
| Consumer Cyclical | 330 | 134 | 25.37% | 55.22% | 26 |
| Technology | 3195 | 1340 | 49.03% | 39.78% | 150 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4385 | 1858 | {'Excellent': 642, 'Good': 191, 'Neutral': 219, 'Poor': 806, 'Unknown': 0, 'Pending': 2527} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2544 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2499 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1663 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 833 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 791 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2514 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2418 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1599 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 806 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 723 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
