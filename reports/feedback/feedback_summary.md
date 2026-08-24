# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-24T18:18:01.402582-04:00
- Validation件数: 1420
- 完了済みValidation: 327
- 未完了Validation: 1093
- 成功率: 39.14%
- 失敗率: 52.60%
- Result Counts(期間完了分): {'Excellent': 105, 'Poor': 172, 'Neutral': 27, 'Good': 23}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 105 | 105 | 100.00% | 0.00% |
| Good | 23 | 23 | 100.00% | 0.00% |
| Neutral | 1120 | 27 | 0.00% | 0.00% |
| Poor | 172 | 172 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 1010 | 214 | {'Excellent': 59, 'Good': 12, 'Neutral': 20, 'Poor': 123, 'Unknown': 0, 'Pending': 796} |
| Low Score (<60) | 410 | 113 | {'Excellent': 46, 'Good': 11, 'Neutral': 7, 'Poor': 49, 'Unknown': 0, 'Pending': 297} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 965 | 211 | 33.65% | 58.77% | 16 |
| Medium | 455 | 116 | 49.14% | 41.38% | 11 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 780 | 122 | 32.79% | 63.11% | 5 |
| Moderate | 180 | 21 | 52.38% | 33.33% | 3 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 350 | 90 | 24.44% | 64.44% | 10 |
| Consumer Cyclical | 150 | 37 | 35.14% | 56.76% | 3 |
| Technology | 920 | 200 | 46.50% | 46.50% | 14 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1420 | 327 | {'Excellent': 105, 'Good': 23, 'Neutral': 27, 'Poor': 172, 'Unknown': 0, 'Pending': 1093} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 396 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 384 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 256 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 128 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 116 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 528 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 516 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 344 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 172 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 160 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
