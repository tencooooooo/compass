# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-01T21:14:10.613278-04:00
- Validation件数: 3145
- 完了済みValidation: 944
- 未完了Validation: 2201
- 成功率: 45.87%
- 失敗率: 41.42%
- Result Counts(期間完了分): {'Excellent': 356, 'Poor': 391, 'Neutral': 120, 'Good': 77}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 356 | 356 | 100.00% | 0.00% |
| Good | 77 | 77 | 100.00% | 0.00% |
| Neutral | 2321 | 120 | 0.00% | 0.00% |
| Poor | 391 | 391 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 950 | 308 | {'Excellent': 151, 'Good': 28, 'Neutral': 42, 'Poor': 87, 'Unknown': 0, 'Pending': 642} |
| Low Score (<60) | 2195 | 636 | {'Excellent': 205, 'Good': 49, 'Neutral': 78, 'Poor': 304, 'Unknown': 0, 'Pending': 1559} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 639 | 48.67% | 39.75% | 74 |
| Medium | 1105 | 305 | 40.00% | 44.92% | 46 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2205 | 592 | 46.28% | 40.03% | 81 |
| Moderate | 480 | 135 | 42.96% | 43.70% | 18 |
| Unknown | 460 | 217 | 46.54% | 43.78% | 21 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 665 | 215 | 35.81% | 51.16% | 28 |
| Consumer Cyclical | 225 | 80 | 18.75% | 70.00% | 9 |
| Technology | 2255 | 649 | 52.54% | 34.67% | 83 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3140 | 944 | {'Excellent': 356, 'Good': 77, 'Neutral': 120, 'Poor': 391, 'Unknown': 0, 'Pending': 2196} |

## Success Patterns

- Momentum: 1316 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1299 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 863 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 433 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 419 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1236 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1173 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 777 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 391 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 333 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
