# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-06T21:28:50.265637-04:00
- Validation件数: 840
- 完了済みValidation: 179
- 未完了Validation: 661
- 成功率: 46.37%
- 失敗率: 44.13%
- Result Counts(期間完了分): {'Excellent': 70, 'Poor': 79, 'Neutral': 17, 'Good': 13}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 70 | 70 | 100.00% | 0.00% |
| Good | 13 | 13 | 100.00% | 0.00% |
| Neutral | 678 | 17 | 0.00% | 0.00% |
| Poor | 79 | 79 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 140 | 30 | {'Excellent': 10, 'Good': 1, 'Neutral': 1, 'Poor': 18, 'Unknown': 0, 'Pending': 110} |
| Mid Score (60-74) | 535 | 111 | {'Excellent': 49, 'Good': 7, 'Neutral': 13, 'Poor': 42, 'Unknown': 0, 'Pending': 424} |
| Low Score (<60) | 165 | 38 | {'Excellent': 11, 'Good': 5, 'Neutral': 3, 'Poor': 19, 'Unknown': 0, 'Pending': 127} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 555 | 101 | 38.61% | 51.49% | 10 |
| Medium | 285 | 78 | 56.41% | 34.62% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 320 | 36 | 44.44% | 55.56% | 0 |
| Moderate | 60 | 5 | 80.00% | 20.00% | 0 |
| Unknown | 460 | 138 | 45.65% | 42.03% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 240 | 51 | 33.33% | 54.90% | 6 |
| Consumer Cyclical | 90 | 19 | 42.11% | 47.37% | 2 |
| Technology | 510 | 109 | 53.21% | 38.53% | 9 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 840 | 179 | {'Excellent': 70, 'Good': 13, 'Neutral': 17, 'Poor': 79, 'Unknown': 0, 'Pending': 661} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 256 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 249 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 166 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 83 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 76 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 239 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 237 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 158 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 79 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 77 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
