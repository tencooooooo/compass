# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-20T20:16:37.137070-04:00
- Validation件数: 3495
- 完了済みValidation: 1303
- 未完了Validation: 2192
- 成功率: 47.05%
- 失敗率: 39.45%
- Result Counts(期間完了分): {'Excellent': 478, 'Poor': 514, 'Neutral': 176, 'Good': 135}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 478 | 478 | 100.00% | 0.00% |
| Good | 135 | 135 | 100.00% | 0.00% |
| Neutral | 2368 | 176 | 0.00% | 0.00% |
| Poor | 514 | 514 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 595 | 230 | {'Excellent': 83, 'Good': 17, 'Neutral': 25, 'Poor': 105, 'Unknown': 0, 'Pending': 365} |
| Low Score (<60) | 2900 | 1073 | {'Excellent': 395, 'Good': 118, 'Neutral': 151, 'Poor': 409, 'Unknown': 0, 'Pending': 1827} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 846 | 51.30% | 37.23% | 97 |
| Medium | 1455 | 457 | 39.17% | 43.54% | 79 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2555 | 850 | 47.06% | 38.35% | 124 |
| Moderate | 480 | 177 | 40.68% | 45.20% | 25 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 288 | 38.54% | 46.88% | 42 |
| Consumer Cyclical | 225 | 98 | 20.41% | 64.29% | 15 |
| Technology | 2555 | 917 | 52.56% | 34.46% | 119 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3490 | 1303 | {'Excellent': 478, 'Good': 135, 'Neutral': 176, 'Poor': 514, 'Unknown': 0, 'Pending': 2187} |

## Success Patterns

- Momentum: 1861 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1839 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1223 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 613 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 594 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1618 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1542 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1018 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 514 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 448 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
