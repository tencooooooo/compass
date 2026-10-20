# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-19T20:51:18.306089-04:00
- Validation件数: 3475
- 完了済みValidation: 1259
- 未完了Validation: 2216
- 成功率: 47.58%
- 失敗率: 39.32%
- Result Counts(期間完了分): {'Excellent': 472, 'Poor': 495, 'Neutral': 165, 'Good': 127}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 472 | 472 | 100.00% | 0.00% |
| Good | 127 | 127 | 100.00% | 0.00% |
| Neutral | 2381 | 165 | 0.00% | 0.00% |
| Poor | 495 | 495 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 395 | 144 | {'Excellent': 72, 'Good': 8, 'Neutral': 11, 'Poor': 53, 'Unknown': 0, 'Pending': 251} |
| Low Score (<60) | 3080 | 1115 | {'Excellent': 400, 'Good': 119, 'Neutral': 154, 'Poor': 442, 'Unknown': 0, 'Pending': 1965} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 815 | 51.78% | 37.30% | 89 |
| Medium | 1435 | 444 | 39.86% | 43.02% | 76 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2535 | 811 | 47.72% | 38.22% | 114 |
| Moderate | 480 | 172 | 41.28% | 44.77% | 24 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 280 | 38.57% | 46.79% | 41 |
| Consumer Cyclical | 225 | 95 | 18.95% | 66.32% | 14 |
| Technology | 2535 | 884 | 53.51% | 34.05% | 110 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3470 | 1259 | {'Excellent': 472, 'Good': 127, 'Neutral': 165, 'Poor': 495, 'Unknown': 0, 'Pending': 2211} |

## Success Patterns

- Momentum: 1817 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1797 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1195 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 599 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 582 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1560 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1485 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 981 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 495 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 429 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
