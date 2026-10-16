# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-15T20:00:16.415573-04:00
- Validation件数: 3440
- 完了済みValidation: 1239
- 未完了Validation: 2201
- 成功率: 47.94%
- 失敗率: 38.98%
- Result Counts(期間完了分): {'Excellent': 470, 'Poor': 483, 'Neutral': 162, 'Good': 124}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 470 | 470 | 100.00% | 0.00% |
| Good | 124 | 124 | 100.00% | 0.00% |
| Neutral | 2363 | 162 | 0.00% | 0.00% |
| Poor | 483 | 483 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 755 | 252 | {'Excellent': 129, 'Good': 14, 'Neutral': 16, 'Poor': 93, 'Unknown': 0, 'Pending': 503} |
| Low Score (<60) | 2685 | 987 | {'Excellent': 341, 'Good': 110, 'Neutral': 146, 'Poor': 390, 'Unknown': 0, 'Pending': 1698} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 803 | 51.93% | 37.11% | 88 |
| Medium | 1400 | 436 | 40.60% | 42.43% | 74 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2500 | 795 | 48.18% | 37.74% | 112 |
| Moderate | 480 | 168 | 41.67% | 44.64% | 23 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 277 | 38.63% | 46.57% | 41 |
| Consumer Cyclical | 225 | 95 | 18.95% | 66.32% | 14 |
| Technology | 2500 | 867 | 54.09% | 33.56% | 107 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3435 | 1239 | {'Excellent': 470, 'Good': 124, 'Neutral': 162, 'Poor': 483, 'Unknown': 0, 'Pending': 2196} |

## Success Patterns

- Momentum: 1802 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1782 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1185 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 594 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 577 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1523 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1449 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 958 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 483 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 417 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
