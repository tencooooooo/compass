# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-17T22:16:08.805429-05:00
- Validation件数: 4155
- 完了済みValidation: 1700
- 未完了Validation: 2455
- 成功率: 45.41%
- 失敗率: 41.88%
- Result Counts(期間完了分): {'Excellent': 602, 'Poor': 712, 'Neutral': 216, 'Good': 170}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 602 | 602 | 100.00% | 0.00% |
| Good | 170 | 170 | 100.00% | 0.00% |
| Neutral | 2671 | 216 | 0.00% | 0.00% |
| Poor | 712 | 712 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 715 | 309 | {'Excellent': 98, 'Good': 24, 'Neutral': 38, 'Poor': 149, 'Unknown': 0, 'Pending': 406} |
| Mid Score (60-74) | 2405 | 966 | {'Excellent': 428, 'Good': 113, 'Neutral': 131, 'Poor': 294, 'Unknown': 0, 'Pending': 1439} |
| Low Score (<60) | 1035 | 425 | {'Excellent': 76, 'Good': 33, 'Neutral': 47, 'Poor': 269, 'Unknown': 0, 'Pending': 610} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2315 | 995 | 53.37% | 35.98% | 106 |
| Medium | 1840 | 705 | 34.18% | 50.21% | 110 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3115 | 1205 | 43.65% | 42.82% | 163 |
| Moderate | 580 | 219 | 47.95% | 40.18% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 820 | 355 | 36.06% | 51.83% | 43 |
| Consumer Cyclical | 285 | 121 | 20.66% | 59.50% | 24 |
| Technology | 3050 | 1224 | 50.57% | 37.25% | 149 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4155 | 1700 | {'Excellent': 602, 'Good': 170, 'Neutral': 216, 'Poor': 712, 'Unknown': 0, 'Pending': 2455} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2346 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2316 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1541 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 772 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 745 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2222 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2136 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1414 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 712 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 636 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
