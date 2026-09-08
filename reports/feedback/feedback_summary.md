# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-08T19:47:09.945415-04:00
- Validation件数: 2135
- 完了済みValidation: 534
- 未完了Validation: 1601
- 成功率: 41.39%
- 失敗率: 46.44%
- Result Counts(期間完了分): {'Excellent': 181, 'Poor': 248, 'Neutral': 65, 'Good': 40}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 181 | 181 | 100.00% | 0.00% |
| Good | 40 | 40 | 100.00% | 0.00% |
| Neutral | 1666 | 65 | 0.00% | 0.00% |
| Poor | 248 | 248 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 560 | 153 | {'Excellent': 69, 'Good': 14, 'Neutral': 13, 'Poor': 57, 'Unknown': 0, 'Pending': 407} |
| Mid Score (60-74) | 945 | 209 | {'Excellent': 80, 'Good': 10, 'Neutral': 27, 'Poor': 92, 'Unknown': 0, 'Pending': 736} |
| Low Score (<60) | 630 | 172 | {'Excellent': 32, 'Good': 16, 'Neutral': 25, 'Poor': 99, 'Unknown': 0, 'Pending': 458} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1485 | 367 | 40.87% | 47.14% | 44 |
| Medium | 650 | 167 | 42.51% | 44.91% | 21 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1340 | 287 | 39.02% | 49.13% | 34 |
| Moderate | 335 | 63 | 50.79% | 30.16% | 12 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 495 | 136 | 27.21% | 58.09% | 20 |
| Consumer Cyclical | 190 | 52 | 28.85% | 63.46% | 4 |
| Technology | 1450 | 346 | 48.84% | 39.31% | 41 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2135 | 534 | {'Excellent': 181, 'Good': 40, 'Neutral': 65, 'Poor': 248, 'Unknown': 0, 'Pending': 1601} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 678 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 663 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 441 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 221 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 207 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 773 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 744 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 495 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 248 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 220 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
