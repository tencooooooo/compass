# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-04T18:54:36.702634-04:00
- Validation件数: 770
- 完了済みValidation: 156
- 未完了Validation: 614
- 成功率: 46.15%
- 失敗率: 42.95%
- Result Counts(期間完了分): {'Excellent': 59, 'Poor': 67, 'Neutral': 17, 'Good': 13}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 59 | 59 | 100.00% | 0.00% |
| Good | 13 | 13 | 100.00% | 0.00% |
| Neutral | 631 | 17 | 0.00% | 0.00% |
| Poor | 67 | 67 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 130 | 26 | {'Excellent': 9, 'Good': 1, 'Neutral': 1, 'Poor': 15, 'Unknown': 0, 'Pending': 104} |
| Mid Score (60-74) | 485 | 97 | {'Excellent': 39, 'Good': 7, 'Neutral': 13, 'Poor': 38, 'Unknown': 0, 'Pending': 388} |
| Low Score (<60) | 155 | 33 | {'Excellent': 11, 'Good': 5, 'Neutral': 3, 'Poor': 14, 'Unknown': 0, 'Pending': 122} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 505 | 85 | 37.65% | 50.59% | 10 |
| Medium | 265 | 71 | 56.34% | 33.80% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 270 | 27 | 37.04% | 62.96% | 0 |
| Moderate | 40 | 4 | 75.00% | 25.00% | 0 |
| Unknown | 460 | 125 | 47.20% | 39.20% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 220 | 44 | 31.82% | 54.55% | 6 |
| Consumer Cyclical | 80 | 17 | 41.18% | 47.06% | 2 |
| Technology | 470 | 95 | 53.68% | 36.84% | 9 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 770 | 156 | {'Excellent': 59, 'Good': 13, 'Neutral': 17, 'Poor': 67, 'Unknown': 0, 'Pending': 614} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 222 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 216 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 144 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 72 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 66 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 203 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 201 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 134 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 67 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 65 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
