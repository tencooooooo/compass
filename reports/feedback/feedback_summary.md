# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-02T20:51:30.755783-04:00
- Validation件数: 3180
- 完了済みValidation: 969
- 未完了Validation: 2211
- 成功率: 45.82%
- 失敗率: 41.18%
- Result Counts(期間完了分): {'Excellent': 366, 'Poor': 399, 'Neutral': 126, 'Good': 78}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 366 | 366 | 100.00% | 0.00% |
| Good | 78 | 78 | 100.00% | 0.00% |
| Neutral | 2337 | 126 | 0.00% | 0.00% |
| Poor | 399 | 399 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 510 | 151 | {'Excellent': 68, 'Good': 9, 'Neutral': 19, 'Poor': 55, 'Unknown': 0, 'Pending': 359} |
| Low Score (<60) | 2670 | 818 | {'Excellent': 298, 'Good': 69, 'Neutral': 107, 'Poor': 344, 'Unknown': 0, 'Pending': 1852} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 653 | 48.85% | 39.51% | 76 |
| Medium | 1140 | 316 | 39.56% | 44.62% | 50 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2240 | 614 | 46.25% | 39.74% | 86 |
| Moderate | 480 | 138 | 42.75% | 43.48% | 19 |
| Unknown | 460 | 217 | 46.54% | 43.78% | 21 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 670 | 219 | 35.62% | 50.68% | 30 |
| Consumer Cyclical | 225 | 80 | 18.75% | 70.00% | 9 |
| Technology | 2285 | 670 | 52.39% | 34.63% | 87 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3175 | 969 | {'Excellent': 366, 'Good': 78, 'Neutral': 126, 'Poor': 399, 'Unknown': 0, 'Pending': 2206} |

## Success Patterns

- Momentum: 1349 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1332 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 885 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 444 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 430 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1260 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1197 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 793 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 399 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 341 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
