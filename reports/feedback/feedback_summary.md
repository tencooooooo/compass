# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-23T20:10:59.883841-04:00
- Validation件数: 3570
- 完了済みValidation: 1351
- 未完了Validation: 2219
- 成功率: 46.48%
- 失敗率: 39.82%
- Result Counts(期間完了分): {'Excellent': 487, 'Poor': 538, 'Neutral': 185, 'Good': 141}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 487 | 487 | 100.00% | 0.00% |
| Good | 141 | 141 | 100.00% | 0.00% |
| Neutral | 2404 | 185 | 0.00% | 0.00% |
| Poor | 538 | 538 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 975 | 361 | {'Excellent': 159, 'Good': 38, 'Neutral': 38, 'Poor': 126, 'Unknown': 0, 'Pending': 614} |
| Low Score (<60) | 2595 | 990 | {'Excellent': 328, 'Good': 103, 'Neutral': 147, 'Poor': 412, 'Unknown': 0, 'Pending': 1605} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 865 | 51.45% | 37.11% | 99 |
| Medium | 1530 | 486 | 37.65% | 44.65% | 86 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2630 | 893 | 46.02% | 39.19% | 132 |
| Moderate | 480 | 182 | 41.76% | 43.96% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 294 | 37.76% | 47.62% | 43 |
| Consumer Cyclical | 225 | 100 | 20.00% | 63.00% | 17 |
| Technology | 2630 | 957 | 51.93% | 35.01% | 125 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3565 | 1351 | {'Excellent': 487, 'Good': 141, 'Neutral': 185, 'Poor': 538, 'Unknown': 0, 'Pending': 2214} |

## Success Patterns

- Momentum: 1906 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1884 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1253 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 628 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 609 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1690 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1614 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1066 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 538 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 472 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
