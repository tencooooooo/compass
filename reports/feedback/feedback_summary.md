# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-29T21:29:19.860813-04:00
- Validation件数: 3655
- 完了済みValidation: 1437
- 未完了Validation: 2218
- 成功率: 46.56%
- 失敗率: 39.81%
- Result Counts(期間完了分): {'Excellent': 519, 'Poor': 572, 'Neutral': 196, 'Good': 150}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 519 | 519 | 100.00% | 0.00% |
| Good | 150 | 150 | 100.00% | 0.00% |
| Neutral | 2414 | 196 | 0.00% | 0.00% |
| Poor | 572 | 572 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 1025 | 375 | {'Excellent': 177, 'Good': 26, 'Neutral': 51, 'Poor': 121, 'Unknown': 0, 'Pending': 650} |
| Low Score (<60) | 2630 | 1062 | {'Excellent': 342, 'Good': 124, 'Neutral': 145, 'Poor': 451, 'Unknown': 0, 'Pending': 1568} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 895 | 51.96% | 36.65% | 102 |
| Medium | 1615 | 542 | 37.64% | 45.02% | 94 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2715 | 969 | 45.61% | 39.63% | 143 |
| Moderate | 480 | 192 | 44.79% | 41.67% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 309 | 36.89% | 49.19% | 43 |
| Consumer Cyclical | 225 | 102 | 21.57% | 61.76% | 17 |
| Technology | 2715 | 1026 | 51.95% | 34.80% | 136 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3650 | 1437 | {'Excellent': 519, 'Good': 150, 'Neutral': 196, 'Poor': 572, 'Unknown': 0, 'Pending': 2213} |

## Success Patterns

- Momentum: 2031 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2007 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1335 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 669 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 648 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1792 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1716 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1134 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 572 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 506 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
