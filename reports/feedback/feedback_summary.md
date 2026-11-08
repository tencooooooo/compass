# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-08T02:16:47.142073-05:00
- Validation件数: 3725
- 完了済みValidation: 1563
- 未完了Validation: 2162
- 成功率: 45.55%
- 失敗率: 41.20%
- Result Counts(期間完了分): {'Excellent': 551, 'Poor': 644, 'Neutral': 207, 'Good': 161}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 551 | 551 | 100.00% | 0.00% |
| Good | 161 | 161 | 100.00% | 0.00% |
| Neutral | 2369 | 207 | 0.00% | 0.00% |
| Poor | 644 | 644 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 3515 | 1476 | {'Excellent': 541, 'Good': 158, 'Neutral': 201, 'Poor': 576, 'Unknown': 0, 'Pending': 2039} |
| Low Score (<60) | 210 | 87 | {'Excellent': 10, 'Good': 3, 'Neutral': 6, 'Poor': 68, 'Unknown': 0, 'Pending': 123} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2060 | 929 | 52.42% | 36.28% | 105 |
| Medium | 1665 | 634 | 35.49% | 48.42% | 102 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2780 | 1083 | 43.86% | 41.92% | 154 |
| Moderate | 485 | 204 | 47.06% | 40.20% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 725 | 332 | 36.14% | 50.90% | 43 |
| Consumer Cyclical | 230 | 109 | 20.18% | 63.30% | 18 |
| Technology | 2770 | 1122 | 50.80% | 36.19% | 146 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 3725 | 1563 | {'Excellent': 551, 'Good': 161, 'Neutral': 207, 'Poor': 644, 'Unknown': 0, 'Pending': 2162} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2160 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2136 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1421 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 712 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 691 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2014 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1932 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1278 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 644 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 572 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
