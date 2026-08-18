# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-18T18:14:34.080870-04:00
- Validation件数: 1140
- 完了済みValidation: 279
- 未完了Validation: 861
- 成功率: 40.86%
- 失敗率: 50.18%
- Result Counts(期間完了分): {'Excellent': 93, 'Poor': 140, 'Neutral': 25, 'Good': 21}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 93 | 93 | 100.00% | 0.00% |
| Good | 21 | 21 | 100.00% | 0.00% |
| Neutral | 886 | 25 | 0.00% | 0.00% |
| Poor | 140 | 140 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 770 | 180 | {'Excellent': 77, 'Good': 10, 'Neutral': 18, 'Poor': 75, 'Unknown': 0, 'Pending': 590} |
| Low Score (<60) | 370 | 99 | {'Excellent': 16, 'Good': 11, 'Neutral': 7, 'Poor': 65, 'Unknown': 0, 'Pending': 271} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 750 | 179 | 34.64% | 56.42% | 16 |
| Medium | 390 | 100 | 52.00% | 39.00% | 9 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 570 | 79 | 37.97% | 58.23% | 3 |
| Moderate | 110 | 16 | 43.75% | 37.50% | 3 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 300 | 81 | 23.46% | 65.43% | 9 |
| Consumer Cyclical | 130 | 32 | 34.38% | 59.38% | 2 |
| Technology | 710 | 166 | 50.60% | 40.96% | 14 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1140 | 279 | {'Excellent': 93, 'Good': 21, 'Neutral': 25, 'Poor': 140, 'Unknown': 0, 'Pending': 861} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 352 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 342 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 228 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 114 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 104 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 430 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 420 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 280 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 140 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 130 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
