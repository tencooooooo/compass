# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-13T20:46:50.286527-04:00
- Validation件数: 3400
- 完了済みValidation: 1181
- 未完了Validation: 2219
- 成功率: 48.01%
- 失敗率: 39.12%
- Result Counts(期間完了分): {'Excellent': 453, 'Poor': 462, 'Neutral': 152, 'Good': 114}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 453 | 453 | 100.00% | 0.00% |
| Good | 114 | 114 | 100.00% | 0.00% |
| Neutral | 2371 | 152 | 0.00% | 0.00% |
| Poor | 462 | 462 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 200 | 53 | {'Excellent': 26, 'Good': 3, 'Neutral': 2, 'Poor': 22, 'Unknown': 0, 'Pending': 147} |
| Low Score (<60) | 3200 | 1128 | {'Excellent': 427, 'Good': 111, 'Neutral': 150, 'Poor': 440, 'Unknown': 0, 'Pending': 2072} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 775 | 51.48% | 37.68% | 84 |
| Medium | 1360 | 406 | 41.38% | 41.87% | 68 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2460 | 757 | 48.48% | 37.52% | 106 |
| Moderate | 480 | 165 | 41.82% | 44.24% | 23 |
| Unknown | 460 | 259 | 50.58% | 40.54% | 23 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 264 | 38.26% | 47.35% | 38 |
| Consumer Cyclical | 225 | 94 | 19.15% | 67.02% | 13 |
| Technology | 2460 | 823 | 54.43% | 33.29% | 101 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3395 | 1181 | {'Excellent': 453, 'Good': 114, 'Neutral': 152, 'Poor': 462, 'Unknown': 0, 'Pending': 2214} |

## Success Patterns

- Momentum: 1721 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1701 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1131 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 567 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 550 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1459 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1386 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 916 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 462 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 397 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
