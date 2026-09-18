# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-18T19:47:17.299921-04:00
- Validation件数: 2645
- 完了済みValidation: 706
- 未完了Validation: 1939
- 成功率: 43.48%
- 失敗率: 43.06%
- Result Counts(期間完了分): {'Excellent': 252, 'Poor': 304, 'Neutral': 95, 'Good': 55}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 252 | 252 | 100.00% | 0.00% |
| Good | 55 | 55 | 100.00% | 0.00% |
| Neutral | 2034 | 95 | 0.00% | 0.00% |
| Poor | 304 | 304 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 680 | 196 | {'Excellent': 93, 'Good': 17, 'Neutral': 18, 'Poor': 68, 'Unknown': 0, 'Pending': 484} |
| Mid Score (60-74) | 1785 | 472 | {'Excellent': 150, 'Good': 38, 'Neutral': 73, 'Poor': 211, 'Unknown': 0, 'Pending': 1313} |
| Low Score (<60) | 180 | 38 | {'Excellent': 9, 'Good': 0, 'Neutral': 4, 'Poor': 25, 'Unknown': 0, 'Pending': 142} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1875 | 488 | 45.49% | 41.80% | 62 |
| Medium | 770 | 218 | 38.99% | 45.87% | 33 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1770 | 428 | 42.76% | 42.99% | 61 |
| Moderate | 415 | 94 | 50.00% | 34.04% | 15 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 580 | 168 | 33.93% | 51.79% | 24 |
| Consumer Cyclical | 205 | 66 | 22.73% | 66.67% | 7 |
| Technology | 1860 | 472 | 49.79% | 36.65% | 64 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2645 | 706 | {'Excellent': 252, 'Good': 55, 'Neutral': 95, 'Poor': 304, 'Unknown': 0, 'Pending': 1939} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 938 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 921 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 611 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 307 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 293 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 955 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 912 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 606 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 304 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 263 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
