# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-24T00:43:05.409311-05:00
- Validation件数: 4380
- 完了済みValidation: 1831
- 未完了Validation: 2549
- 成功率: 45.00%
- 失敗率: 43.15%
- Result Counts(期間完了分): {'Excellent': 636, 'Poor': 790, 'Neutral': 217, 'Good': 188}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 636 | 636 | 100.00% | 0.00% |
| Good | 188 | 188 | 100.00% | 0.00% |
| Neutral | 2766 | 217 | 0.00% | 0.00% |
| Poor | 790 | 790 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 3390 | 1360 | {'Excellent': 525, 'Good': 134, 'Neutral': 156, 'Poor': 545, 'Unknown': 0, 'Pending': 2030} |
| Low Score (<60) | 990 | 471 | {'Excellent': 111, 'Good': 54, 'Neutral': 61, 'Poor': 245, 'Unknown': 0, 'Pending': 519} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2475 | 1067 | 52.58% | 37.49% | 106 |
| Medium | 1905 | 764 | 34.42% | 51.05% | 111 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3285 | 1308 | 43.12% | 44.34% | 164 |
| Moderate | 635 | 247 | 48.18% | 41.30% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 860 | 379 | 36.94% | 51.72% | 43 |
| Consumer Cyclical | 330 | 131 | 25.19% | 55.73% | 25 |
| Technology | 3190 | 1321 | 49.28% | 39.44% | 149 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4380 | 1831 | {'Excellent': 636, 'Good': 188, 'Neutral': 217, 'Poor': 790, 'Unknown': 0, 'Pending': 2549} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2516 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2472 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1645 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 824 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 783 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2463 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2370 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1568 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 790 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 709 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
