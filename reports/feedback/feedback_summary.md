# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-22T20:17:46.619642-04:00
- Validation件数: 3545
- 完了済みValidation: 1329
- 未完了Validation: 2216
- 成功率: 46.65%
- 失敗率: 39.73%
- Result Counts(期間完了分): {'Excellent': 481, 'Poor': 528, 'Neutral': 181, 'Good': 139}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 481 | 481 | 100.00% | 0.00% |
| Good | 139 | 139 | 100.00% | 0.00% |
| Neutral | 2397 | 181 | 0.00% | 0.00% |
| Poor | 528 | 528 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 985 | 381 | {'Excellent': 152, 'Good': 44, 'Neutral': 45, 'Poor': 140, 'Unknown': 0, 'Pending': 604} |
| Low Score (<60) | 2560 | 948 | {'Excellent': 329, 'Good': 95, 'Neutral': 136, 'Poor': 388, 'Unknown': 0, 'Pending': 1612} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 852 | 51.41% | 37.09% | 98 |
| Medium | 1505 | 477 | 38.16% | 44.44% | 83 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2605 | 874 | 46.34% | 38.90% | 129 |
| Moderate | 480 | 179 | 41.34% | 44.69% | 25 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 291 | 38.14% | 47.42% | 42 |
| Consumer Cyclical | 225 | 99 | 20.20% | 63.64% | 16 |
| Technology | 2605 | 939 | 52.08% | 34.82% | 123 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3540 | 1329 | {'Excellent': 481, 'Good': 139, 'Neutral': 181, 'Poor': 528, 'Unknown': 0, 'Pending': 2211} |

## Success Patterns

- Momentum: 1882 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1860 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1237 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 620 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 601 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1660 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1584 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1046 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 528 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 462 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
