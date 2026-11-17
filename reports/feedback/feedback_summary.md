# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-16T23:17:20.407937-05:00
- Validation件数: 4100
- 完了済みValidation: 1674
- 未完了Validation: 2426
- 成功率: 45.58%
- 失敗率: 41.58%
- Result Counts(期間完了分): {'Excellent': 593, 'Poor': 696, 'Neutral': 215, 'Good': 170}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 593 | 593 | 100.00% | 0.00% |
| Good | 170 | 170 | 100.00% | 0.00% |
| Neutral | 2641 | 215 | 0.00% | 0.00% |
| Poor | 696 | 696 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 3160 | 1277 | {'Excellent': 521, 'Good': 139, 'Neutral': 163, 'Poor': 454, 'Unknown': 0, 'Pending': 1883} |
| Low Score (<60) | 940 | 397 | {'Excellent': 72, 'Good': 31, 'Neutral': 52, 'Poor': 242, 'Unknown': 0, 'Pending': 543} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2275 | 977 | 53.53% | 35.62% | 106 |
| Medium | 1825 | 697 | 34.43% | 49.93% | 109 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3075 | 1183 | 43.96% | 42.35% | 162 |
| Moderate | 565 | 215 | 47.44% | 40.47% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 810 | 350 | 36.00% | 51.71% | 43 |
| Consumer Cyclical | 275 | 119 | 21.01% | 59.66% | 23 |
| Technology | 3015 | 1205 | 50.79% | 36.85% | 149 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4100 | 1674 | {'Excellent': 593, 'Good': 170, 'Neutral': 215, 'Poor': 696, 'Unknown': 0, 'Pending': 2426} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2318 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2289 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1523 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 763 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 737 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2172 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2088 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1382 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 696 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 622 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
