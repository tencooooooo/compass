# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-07T21:28:46.685750-04:00
- Validation件数: 3280
- 完了済みValidation: 1071
- 未完了Validation: 2209
- 成功率: 46.97%
- 失敗率: 39.78%
- Result Counts(期間完了分): {'Excellent': 412, 'Poor': 426, 'Neutral': 142, 'Good': 91}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 412 | 412 | 100.00% | 0.00% |
| Good | 91 | 91 | 100.00% | 0.00% |
| Neutral | 2351 | 142 | 0.00% | 0.00% |
| Poor | 426 | 426 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 1040 | 328 | {'Excellent': 181, 'Good': 29, 'Neutral': 33, 'Poor': 85, 'Unknown': 0, 'Pending': 712} |
| Low Score (<60) | 2240 | 743 | {'Excellent': 231, 'Good': 62, 'Neutral': 109, 'Poor': 341, 'Unknown': 0, 'Pending': 1497} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 708 | 50.14% | 38.28% | 82 |
| Medium | 1240 | 363 | 40.77% | 42.70% | 60 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2340 | 682 | 47.51% | 38.12% | 98 |
| Moderate | 480 | 155 | 42.58% | 43.23% | 22 |
| Unknown | 460 | 234 | 48.29% | 42.31% | 22 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 695 | 241 | 35.68% | 49.38% | 36 |
| Consumer Cyclical | 225 | 87 | 18.39% | 68.97% | 11 |
| Technology | 2360 | 743 | 53.97% | 33.24% | 95 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3275 | 1071 | {'Excellent': 412, 'Good': 91, 'Neutral': 142, 'Poor': 426, 'Unknown': 0, 'Pending': 2204} |

## Success Patterns

- Momentum: 1527 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1509 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1003 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 503 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 488 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1348 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1278 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 845 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 426 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 363 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
