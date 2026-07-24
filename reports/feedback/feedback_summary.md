# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-07-24T18:54:57.944451-04:00
- Validation件数: 550
- 完了済みValidation: 92
- 未完了Validation: 458
- 成功率: 46.74%
- 失敗率: 40.22%
- Result Counts(期間完了分): {'Excellent': 34, 'Poor': 37, 'Neutral': 12, 'Good': 9}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 34 | 34 | 100.00% | 0.00% |
| Good | 9 | 9 | 100.00% | 0.00% |
| Neutral | 470 | 12 | 0.00% | 0.00% |
| Poor | 37 | 37 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 365 | 60 | {'Excellent': 21, 'Good': 4, 'Neutral': 9, 'Poor': 26, 'Unknown': 0, 'Pending': 305} |
| Low Score (<60) | 185 | 32 | {'Excellent': 13, 'Good': 5, 'Neutral': 3, 'Poor': 11, 'Unknown': 0, 'Pending': 153} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 350 | 57 | 40.35% | 43.86% | 9 |
| Medium | 200 | 35 | 57.14% | 34.29% | 3 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 90 | 0 | N/A | N/A | 0 |
| Unknown | 460 | 92 | 46.74% | 40.22% | 12 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 155 | 27 | 25.93% | 66.67% | 2 |
| Consumer Cyclical | 60 | 11 | 36.36% | 45.45% | 2 |
| Technology | 335 | 54 | 59.26% | 25.93% | 8 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 550 | 92 | {'Excellent': 34, 'Good': 9, 'Neutral': 12, 'Poor': 37, 'Unknown': 0, 'Pending': 458} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 132 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 129 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 86 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 43 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 40 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 112 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 111 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 74 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 37 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 36 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
