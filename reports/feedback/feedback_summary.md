# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-29T20:56:32.249864-04:00
- Validation件数: 3045
- 完了済みValidation: 873
- 未完了Validation: 2172
- 成功率: 45.02%
- 失敗率: 42.04%
- Result Counts(期間完了分): {'Excellent': 323, 'Poor': 367, 'Neutral': 113, 'Good': 70}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 323 | 323 | 100.00% | 0.00% |
| Good | 70 | 70 | 100.00% | 0.00% |
| Neutral | 2285 | 113 | 0.00% | 0.00% |
| Poor | 367 | 367 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 940 | 264 | {'Excellent': 133, 'Good': 24, 'Neutral': 30, 'Poor': 77, 'Unknown': 0, 'Pending': 676} |
| Low Score (<60) | 2105 | 609 | {'Excellent': 190, 'Good': 46, 'Neutral': 83, 'Poor': 290, 'Unknown': 0, 'Pending': 1496} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2015 | 607 | 48.11% | 39.87% | 73 |
| Medium | 1030 | 266 | 37.97% | 46.99% | 40 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2120 | 560 | 46.07% | 40.18% | 77 |
| Moderate | 465 | 129 | 44.96% | 41.86% | 17 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 650 | 199 | 35.18% | 51.26% | 27 |
| Consumer Cyclical | 220 | 75 | 20.00% | 70.67% | 7 |
| Technology | 2175 | 599 | 51.42% | 35.39% | 79 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3040 | 873 | {'Excellent': 323, 'Good': 70, 'Neutral': 113, 'Poor': 367, 'Unknown': 0, 'Pending': 2167} |

## Success Patterns

- Momentum: 1196 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1179 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 783 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 393 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 379 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1162 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1101 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 729 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 367 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 311 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
