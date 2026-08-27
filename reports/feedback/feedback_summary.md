# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-26T22:27:57.254049-04:00
- Validation件数: 1580
- 完了済みValidation: 359
- 未完了Validation: 1221
- 成功率: 38.72%
- 失敗率: 51.25%
- Result Counts(期間完了分): {'Excellent': 113, 'Poor': 184, 'Neutral': 36, 'Good': 26}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 113 | 113 | 100.00% | 0.00% |
| Good | 26 | 26 | 100.00% | 0.00% |
| Neutral | 1257 | 36 | 0.00% | 0.00% |
| Poor | 184 | 184 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 1325 | 294 | {'Excellent': 98, 'Good': 20, 'Neutral': 31, 'Poor': 145, 'Unknown': 0, 'Pending': 1031} |
| Low Score (<60) | 255 | 65 | {'Excellent': 15, 'Good': 6, 'Neutral': 5, 'Poor': 39, 'Unknown': 0, 'Pending': 190} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1090 | 235 | 33.19% | 57.02% | 23 |
| Medium | 490 | 124 | 49.19% | 40.32% | 13 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 910 | 148 | 32.43% | 58.11% | 14 |
| Moderate | 210 | 27 | 51.85% | 37.04% | 3 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 385 | 95 | 26.32% | 62.11% | 11 |
| Consumer Cyclical | 160 | 40 | 35.00% | 55.00% | 4 |
| Technology | 1035 | 224 | 44.64% | 45.98% | 21 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1580 | 359 | {'Excellent': 113, 'Good': 26, 'Neutral': 36, 'Poor': 184, 'Unknown': 0, 'Pending': 1221} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 430 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 417 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 278 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 139 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 126 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 565 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 552 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 368 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 184 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 171 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
