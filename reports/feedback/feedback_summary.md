# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-04T19:36:23.686156-04:00
- Validation件数: 2020
- 完了済みValidation: 493
- 未完了Validation: 1527
- 成功率: 41.58%
- 失敗率: 47.67%
- Result Counts(期間完了分): {'Excellent': 168, 'Poor': 235, 'Neutral': 53, 'Good': 37}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 168 | 168 | 100.00% | 0.00% |
| Good | 37 | 37 | 100.00% | 0.00% |
| Neutral | 1580 | 53 | 0.00% | 0.00% |
| Poor | 235 | 235 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 465 | 135 | {'Excellent': 59, 'Good': 9, 'Neutral': 11, 'Poor': 56, 'Unknown': 0, 'Pending': 330} |
| Mid Score (60-74) | 945 | 197 | {'Excellent': 77, 'Good': 12, 'Neutral': 23, 'Poor': 85, 'Unknown': 0, 'Pending': 748} |
| Low Score (<60) | 610 | 161 | {'Excellent': 32, 'Good': 16, 'Neutral': 19, 'Poor': 94, 'Unknown': 0, 'Pending': 449} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1425 | 336 | 40.48% | 48.81% | 36 |
| Medium | 595 | 157 | 43.95% | 45.22% | 17 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1255 | 254 | 38.98% | 50.79% | 26 |
| Moderate | 305 | 55 | 52.73% | 32.73% | 8 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 475 | 127 | 25.98% | 60.63% | 17 |
| Consumer Cyclical | 185 | 50 | 30.00% | 62.00% | 4 |
| Technology | 1360 | 316 | 49.68% | 40.19% | 32 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2020 | 493 | {'Excellent': 168, 'Good': 37, 'Neutral': 53, 'Poor': 235, 'Unknown': 0, 'Pending': 1527} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 630 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 615 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 409 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 205 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 191 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 732 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 705 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 469 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 235 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 209 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
