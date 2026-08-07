# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-07T18:26:51.158228-04:00
- Validation件数: 875
- 完了済みValidation: 190
- 未完了Validation: 685
- 成功率: 46.32%
- 失敗率: 44.74%
- Result Counts(期間完了分): {'Excellent': 74, 'Poor': 85, 'Neutral': 17, 'Good': 14}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 74 | 74 | 100.00% | 0.00% |
| Good | 14 | 14 | 100.00% | 0.00% |
| Neutral | 702 | 17 | 0.00% | 0.00% |
| Poor | 85 | 85 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 705 | 150 | {'Excellent': 63, 'Good': 9, 'Neutral': 14, 'Poor': 64, 'Unknown': 0, 'Pending': 555} |
| Low Score (<60) | 170 | 40 | {'Excellent': 11, 'Good': 5, 'Neutral': 3, 'Poor': 21, 'Unknown': 0, 'Pending': 130} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 575 | 111 | 39.64% | 51.35% | 10 |
| Medium | 300 | 79 | 55.70% | 35.44% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 345 | 43 | 46.51% | 53.49% | 0 |
| Moderate | 70 | 5 | 80.00% | 20.00% | 0 |
| Unknown | 460 | 142 | 45.07% | 42.96% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 250 | 54 | 33.33% | 55.56% | 6 |
| Consumer Cyclical | 95 | 20 | 40.00% | 50.00% | 2 |
| Technology | 530 | 116 | 53.45% | 38.79% | 9 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 875 | 190 | {'Excellent': 74, 'Good': 14, 'Neutral': 17, 'Poor': 85, 'Unknown': 0, 'Pending': 685} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 271 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 264 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 176 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 88 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 81 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 258 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 255 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 170 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 85 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 82 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
