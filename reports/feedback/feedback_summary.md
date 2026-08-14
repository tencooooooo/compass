# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-14T18:14:34.429428-04:00
- Validation件数: 1030
- 完了済みValidation: 257
- 未完了Validation: 773
- 成功率: 41.63%
- 失敗率: 49.81%
- Result Counts(期間完了分): {'Excellent': 87, 'Poor': 128, 'Neutral': 22, 'Good': 20}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 87 | 87 | 100.00% | 0.00% |
| Good | 20 | 20 | 100.00% | 0.00% |
| Neutral | 795 | 22 | 0.00% | 0.00% |
| Poor | 128 | 128 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 265 | 62 | {'Excellent': 18, 'Good': 5, 'Neutral': 4, 'Poor': 35, 'Unknown': 0, 'Pending': 203} |
| Mid Score (60-74) | 580 | 143 | {'Excellent': 58, 'Good': 9, 'Neutral': 15, 'Poor': 61, 'Unknown': 0, 'Pending': 437} |
| Low Score (<60) | 185 | 52 | {'Excellent': 11, 'Good': 6, 'Neutral': 3, 'Poor': 32, 'Unknown': 0, 'Pending': 133} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 660 | 162 | 34.57% | 56.79% | 14 |
| Medium | 370 | 95 | 53.68% | 37.89% | 8 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 470 | 69 | 39.13% | 56.52% | 3 |
| Moderate | 100 | 14 | 42.86% | 42.86% | 2 |
| Unknown | 460 | 174 | 42.53% | 47.70% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 290 | 74 | 25.68% | 63.51% | 8 |
| Consumer Cyclical | 120 | 30 | 36.67% | 56.67% | 2 |
| Technology | 620 | 153 | 50.33% | 41.83% | 12 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1030 | 257 | {'Excellent': 87, 'Good': 20, 'Neutral': 22, 'Poor': 128, 'Unknown': 0, 'Pending': 773} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 331 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 321 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 214 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 107 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 97 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 392 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 384 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 256 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 128 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 120 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
