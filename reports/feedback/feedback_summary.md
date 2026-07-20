# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-07-20T18:48:47.939788-04:00
- Validation件数: 490
- 完了済みValidation: 70
- 未完了Validation: 420
- 成功率: 52.86%
- 失敗率: 37.14%
- Result Counts(期間完了分): {'Excellent': 28, 'Poor': 26, 'Neutral': 7, 'Good': 9}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 28 | 28 | 100.00% | 0.00% |
| Good | 9 | 9 | 100.00% | 0.00% |
| Neutral | 427 | 7 | 0.00% | 0.00% |
| Poor | 26 | 26 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 385 | 54 | {'Excellent': 22, 'Good': 4, 'Neutral': 6, 'Poor': 22, 'Unknown': 0, 'Pending': 331} |
| Low Score (<60) | 105 | 16 | {'Excellent': 6, 'Good': 5, 'Neutral': 1, 'Poor': 4, 'Unknown': 0, 'Pending': 89} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 310 | 37 | 45.95% | 43.24% | 4 |
| Medium | 180 | 33 | 60.61% | 30.30% | 3 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 30 | 0 | N/A | N/A | 0 |
| Unknown | 460 | 70 | 52.86% | 37.14% | 7 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 140 | 20 | 35.00% | 55.00% | 2 |
| Consumer Cyclical | 60 | 10 | 40.00% | 40.00% | 2 |
| Technology | 290 | 40 | 65.00% | 27.50% | 3 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 490 | 70 | {'Excellent': 28, 'Good': 9, 'Neutral': 7, 'Poor': 26, 'Unknown': 0, 'Pending': 420} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 114 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 111 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 74 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 37 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 34 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Growth: 78 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Momentum: 78 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Financial Health: 52 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 26 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 26 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
