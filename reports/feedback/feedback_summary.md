# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-14T20:13:13.739216-04:00
- Validation件数: 3420
- 完了済みValidation: 1195
- 未完了Validation: 2225
- 成功率: 48.03%
- 失敗率: 39.08%
- Result Counts(期間完了分): {'Excellent': 458, 'Poor': 467, 'Neutral': 154, 'Good': 116}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 458 | 458 | 100.00% | 0.00% |
| Good | 116 | 116 | 100.00% | 0.00% |
| Neutral | 2379 | 154 | 0.00% | 0.00% |
| Poor | 467 | 467 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 950 | 320 | {'Excellent': 163, 'Good': 32, 'Neutral': 27, 'Poor': 98, 'Unknown': 0, 'Pending': 630} |
| Low Score (<60) | 2470 | 875 | {'Excellent': 295, 'Good': 84, 'Neutral': 127, 'Poor': 369, 'Unknown': 0, 'Pending': 1595} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 781 | 51.60% | 37.52% | 85 |
| Medium | 1380 | 414 | 41.30% | 42.03% | 69 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2480 | 764 | 48.43% | 37.70% | 106 |
| Moderate | 480 | 165 | 41.82% | 44.24% | 23 |
| Unknown | 460 | 266 | 50.75% | 39.85% | 25 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 268 | 38.81% | 47.01% | 38 |
| Consumer Cyclical | 225 | 95 | 18.95% | 66.32% | 14 |
| Technology | 2480 | 832 | 54.33% | 33.41% | 102 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3415 | 1195 | {'Excellent': 458, 'Good': 116, 'Neutral': 154, 'Poor': 467, 'Unknown': 0, 'Pending': 2220} |

## Success Patterns

- Momentum: 1742 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1722 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1145 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 574 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 557 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1474 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1401 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 926 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 467 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 402 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
