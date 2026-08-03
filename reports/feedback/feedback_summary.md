# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-03T18:54:01.758843-04:00
- Validation件数: 735
- 完了済みValidation: 150
- 未完了Validation: 585
- 成功率: 45.33%
- 失敗率: 43.33%
- Result Counts(期間完了分): {'Excellent': 55, 'Poor': 65, 'Neutral': 17, 'Good': 13}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 55 | 55 | 100.00% | 0.00% |
| Good | 13 | 13 | 100.00% | 0.00% |
| Neutral | 602 | 17 | 0.00% | 0.00% |
| Poor | 65 | 65 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 260 | 52 | {'Excellent': 20, 'Good': 3, 'Neutral': 5, 'Poor': 24, 'Unknown': 0, 'Pending': 208} |
| Mid Score (60-74) | 325 | 66 | {'Excellent': 24, 'Good': 5, 'Neutral': 9, 'Poor': 28, 'Unknown': 0, 'Pending': 259} |
| Low Score (<60) | 150 | 32 | {'Excellent': 11, 'Good': 5, 'Neutral': 3, 'Poor': 13, 'Unknown': 0, 'Pending': 118} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 480 | 81 | 37.04% | 50.62% | 10 |
| Medium | 255 | 69 | 55.07% | 34.78% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 240 | 22 | 31.82% | 68.18% | 0 |
| Moderate | 35 | 3 | 66.67% | 33.33% | 0 |
| Unknown | 460 | 125 | 47.20% | 39.20% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 210 | 42 | 30.95% | 54.76% | 6 |
| Consumer Cyclical | 75 | 17 | 41.18% | 47.06% | 2 |
| Technology | 450 | 91 | 52.75% | 37.36% | 9 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 735 | 150 | {'Excellent': 55, 'Good': 13, 'Neutral': 17, 'Poor': 65, 'Unknown': 0, 'Pending': 585} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 210 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 204 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 136 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 68 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 62 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 197 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 195 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 130 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 65 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 63 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
