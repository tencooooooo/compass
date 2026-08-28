# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-28T01:54:40.192740-04:00
- Validation件数: 1655
- 完了済みValidation: 377
- 未完了Validation: 1278
- 成功率: 39.52%
- 失敗率: 50.40%
- Result Counts(期間完了分): {'Excellent': 120, 'Poor': 190, 'Neutral': 38, 'Good': 29}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 120 | 120 | 100.00% | 0.00% |
| Good | 29 | 29 | 100.00% | 0.00% |
| Neutral | 1316 | 38 | 0.00% | 0.00% |
| Poor | 190 | 190 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 280 | 62 | {'Excellent': 38, 'Good': 5, 'Neutral': 6, 'Poor': 13, 'Unknown': 0, 'Pending': 218} |
| Mid Score (60-74) | 1115 | 248 | {'Excellent': 67, 'Good': 18, 'Neutral': 26, 'Poor': 137, 'Unknown': 0, 'Pending': 867} |
| Low Score (<60) | 260 | 67 | {'Excellent': 15, 'Good': 6, 'Neutral': 6, 'Poor': 40, 'Unknown': 0, 'Pending': 193} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1150 | 248 | 34.68% | 55.24% | 25 |
| Medium | 505 | 129 | 48.84% | 41.09% | 13 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 970 | 162 | 34.57% | 56.17% | 15 |
| Moderate | 225 | 31 | 51.61% | 35.48% | 4 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 395 | 98 | 25.51% | 63.27% | 11 |
| Consumer Cyclical | 165 | 41 | 34.15% | 56.10% | 4 |
| Technology | 1095 | 238 | 46.22% | 44.12% | 23 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1655 | 377 | {'Excellent': 120, 'Good': 29, 'Neutral': 38, 'Poor': 190, 'Unknown': 0, 'Pending': 1278} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 460 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 447 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 298 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 149 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 136 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 584 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 570 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 380 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 190 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 176 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
