# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-03T19:44:17.691085-04:00
- Validation件数: 1955
- 完了済みValidation: 470
- 未完了Validation: 1485
- 成功率: 41.70%
- 失敗率: 47.66%
- Result Counts(期間完了分): {'Excellent': 162, 'Poor': 224, 'Neutral': 50, 'Good': 34}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 162 | 162 | 100.00% | 0.00% |
| Good | 34 | 34 | 100.00% | 0.00% |
| Neutral | 1535 | 50 | 0.00% | 0.00% |
| Poor | 224 | 224 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 285 | 71 | {'Excellent': 47, 'Good': 5, 'Neutral': 6, 'Poor': 13, 'Unknown': 0, 'Pending': 214} |
| Mid Score (60-74) | 1370 | 324 | {'Excellent': 93, 'Good': 22, 'Neutral': 35, 'Poor': 174, 'Unknown': 0, 'Pending': 1046} |
| Low Score (<60) | 300 | 75 | {'Excellent': 22, 'Good': 7, 'Neutral': 9, 'Poor': 37, 'Unknown': 0, 'Pending': 225} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1380 | 319 | 40.13% | 49.53% | 33 |
| Medium | 575 | 151 | 45.03% | 43.71% | 17 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1205 | 236 | 38.98% | 51.27% | 23 |
| Moderate | 290 | 50 | 54.00% | 30.00% | 8 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 465 | 121 | 25.62% | 60.33% | 17 |
| Consumer Cyclical | 180 | 48 | 31.25% | 60.42% | 4 |
| Technology | 1310 | 301 | 49.83% | 40.53% | 29 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1955 | 470 | {'Excellent': 162, 'Good': 34, 'Neutral': 50, 'Poor': 224, 'Unknown': 0, 'Pending': 1485} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 603 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 588 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 391 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 196 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 182 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 696 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 672 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 447 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 224 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 201 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
