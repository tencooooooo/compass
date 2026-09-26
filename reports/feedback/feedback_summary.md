# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-25T20:18:33.689841-04:00
- Validation件数: 2950
- 完了済みValidation: 814
- 未完了Validation: 2136
- 成功率: 45.09%
- 失敗率: 42.14%
- Result Counts(期間完了分): {'Excellent': 299, 'Poor': 343, 'Neutral': 104, 'Good': 68}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 299 | 299 | 100.00% | 0.00% |
| Good | 68 | 68 | 100.00% | 0.00% |
| Neutral | 2240 | 104 | 0.00% | 0.00% |
| Poor | 343 | 343 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 760 | 220 | {'Excellent': 106, 'Good': 18, 'Neutral': 19, 'Poor': 77, 'Unknown': 0, 'Pending': 540} |
| Mid Score (60-74) | 1985 | 544 | {'Excellent': 180, 'Good': 50, 'Neutral': 81, 'Poor': 233, 'Unknown': 0, 'Pending': 1441} |
| Low Score (<60) | 205 | 50 | {'Excellent': 13, 'Good': 0, 'Neutral': 4, 'Poor': 33, 'Unknown': 0, 'Pending': 155} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2005 | 569 | 47.45% | 40.25% | 70 |
| Medium | 945 | 245 | 39.59% | 46.53% | 34 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2030 | 510 | 45.49% | 41.18% | 68 |
| Moderate | 460 | 120 | 48.33% | 37.50% | 17 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 630 | 188 | 35.64% | 51.06% | 25 |
| Consumer Cyclical | 215 | 71 | 21.13% | 69.01% | 7 |
| Technology | 2105 | 555 | 51.35% | 35.68% | 72 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2950 | 814 | {'Excellent': 299, 'Good': 68, 'Neutral': 104, 'Poor': 343, 'Unknown': 0, 'Pending': 2136} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 1118 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1101 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 731 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 367 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 353 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1083 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1029 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 682 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 343 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 293 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
