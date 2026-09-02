# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-02T19:43:45.346811-04:00
- Validation件数: 1875
- 完了済みValidation: 463
- 未完了Validation: 1412
- 成功率: 41.47%
- 失敗率: 47.73%
- Result Counts(期間完了分): {'Excellent': 160, 'Poor': 221, 'Neutral': 50, 'Good': 32}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 160 | 160 | 100.00% | 0.00% |
| Good | 32 | 32 | 100.00% | 0.00% |
| Neutral | 1462 | 50 | 0.00% | 0.00% |
| Poor | 221 | 221 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 215 | 62 | {'Excellent': 39, 'Good': 5, 'Neutral': 5, 'Poor': 13, 'Unknown': 0, 'Pending': 153} |
| Mid Score (60-74) | 1305 | 312 | {'Excellent': 92, 'Good': 20, 'Neutral': 35, 'Poor': 165, 'Unknown': 0, 'Pending': 993} |
| Low Score (<60) | 355 | 89 | {'Excellent': 29, 'Good': 7, 'Neutral': 10, 'Poor': 43, 'Unknown': 0, 'Pending': 266} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1320 | 314 | 39.81% | 49.68% | 33 |
| Medium | 555 | 149 | 44.97% | 43.62% | 17 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1145 | 230 | 38.70% | 51.30% | 23 |
| Moderate | 270 | 49 | 53.06% | 30.61% | 8 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 450 | 119 | 25.21% | 60.50% | 17 |
| Consumer Cyclical | 170 | 47 | 31.91% | 59.57% | 4 |
| Technology | 1255 | 297 | 49.49% | 40.74% | 29 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1875 | 463 | {'Excellent': 160, 'Good': 32, 'Neutral': 50, 'Poor': 221, 'Unknown': 0, 'Pending': 1412} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 591 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 576 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 383 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 192 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 178 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 686 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 663 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 441 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 221 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 199 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
