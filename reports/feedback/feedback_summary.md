# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-07-27T18:54:13.146047-04:00
- Validation件数: 585
- 完了済みValidation: 98
- 未完了Validation: 487
- 成功率: 44.90%
- 失敗率: 42.86%
- Result Counts(期間完了分): {'Excellent': 35, 'Poor': 42, 'Neutral': 12, 'Good': 9}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 35 | 35 | 100.00% | 0.00% |
| Good | 9 | 9 | 100.00% | 0.00% |
| Neutral | 499 | 12 | 0.00% | 0.00% |
| Poor | 42 | 42 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 465 | 77 | {'Excellent': 23, 'Good': 9, 'Neutral': 10, 'Poor': 35, 'Unknown': 0, 'Pending': 388} |
| Low Score (<60) | 120 | 21 | {'Excellent': 12, 'Good': 0, 'Neutral': 2, 'Poor': 7, 'Unknown': 0, 'Pending': 99} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 370 | 62 | 38.71% | 46.77% | 9 |
| Medium | 215 | 36 | 55.56% | 36.11% | 3 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 110 | 6 | 16.67% | 83.33% | 0 |
| Moderate | 15 | 0 | N/A | N/A | 0 |
| Unknown | 460 | 92 | 46.74% | 40.22% | 12 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 165 | 28 | 25.00% | 67.86% | 2 |
| Consumer Cyclical | 65 | 12 | 33.33% | 50.00% | 2 |
| Technology | 355 | 58 | 56.90% | 29.31% | 8 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 585 | 98 | {'Excellent': 35, 'Good': 9, 'Neutral': 12, 'Poor': 42, 'Unknown': 0, 'Pending': 487} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 135 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 132 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 88 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 44 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 41 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 128 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 126 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 84 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 42 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 40 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
