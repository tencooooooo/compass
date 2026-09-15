# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-15T19:52:06.397797-04:00
- Validation件数: 2435
- 完了済みValidation: 632
- 未完了Validation: 1803
- 成功率: 42.72%
- 失敗率: 44.62%
- Result Counts(期間完了分): {'Excellent': 221, 'Poor': 282, 'Neutral': 80, 'Good': 49}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 221 | 221 | 100.00% | 0.00% |
| Good | 49 | 49 | 100.00% | 0.00% |
| Neutral | 1883 | 80 | 0.00% | 0.00% |
| Poor | 282 | 282 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 590 | 162 | {'Excellent': 66, 'Good': 10, 'Neutral': 15, 'Poor': 71, 'Unknown': 0, 'Pending': 428} |
| Mid Score (60-74) | 1525 | 386 | {'Excellent': 139, 'Good': 33, 'Neutral': 54, 'Poor': 160, 'Unknown': 0, 'Pending': 1139} |
| Low Score (<60) | 320 | 84 | {'Excellent': 16, 'Good': 6, 'Neutral': 11, 'Poor': 51, 'Unknown': 0, 'Pending': 236} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1700 | 428 | 44.63% | 43.69% | 50 |
| Medium | 735 | 204 | 38.73% | 46.57% | 30 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1605 | 362 | 41.16% | 45.58% | 48 |
| Moderate | 370 | 86 | 51.16% | 33.72% | 13 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 550 | 157 | 30.57% | 54.78% | 23 |
| Consumer Cyclical | 195 | 62 | 24.19% | 66.13% | 6 |
| Technology | 1690 | 413 | 50.12% | 37.53% | 51 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2435 | 632 | {'Excellent': 221, 'Good': 49, 'Neutral': 80, 'Poor': 282, 'Unknown': 0, 'Pending': 1803} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 827 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 810 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 537 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 270 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 256 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 885 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 846 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 562 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 282 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 245 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
