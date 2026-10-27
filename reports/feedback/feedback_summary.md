# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-26T21:02:38.267028-04:00
- Validation件数: 3590
- 完了済みValidation: 1366
- 未完了Validation: 2224
- 成功率: 46.34%
- 失敗率: 40.04%
- Result Counts(期間完了分): {'Excellent': 492, 'Poor': 547, 'Neutral': 186, 'Good': 141}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 492 | 492 | 100.00% | 0.00% |
| Good | 141 | 141 | 100.00% | 0.00% |
| Neutral | 2410 | 186 | 0.00% | 0.00% |
| Poor | 547 | 547 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 420 | 158 | {'Excellent': 72, 'Good': 9, 'Neutral': 12, 'Poor': 65, 'Unknown': 0, 'Pending': 262} |
| Low Score (<60) | 3170 | 1208 | {'Excellent': 420, 'Good': 132, 'Neutral': 174, 'Poor': 482, 'Unknown': 0, 'Pending': 1962} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 868 | 51.50% | 37.10% | 99 |
| Medium | 1550 | 498 | 37.35% | 45.18% | 87 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2650 | 907 | 45.76% | 39.58% | 133 |
| Moderate | 480 | 183 | 42.08% | 43.72% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 296 | 37.50% | 47.97% | 43 |
| Consumer Cyclical | 225 | 100 | 20.00% | 63.00% | 17 |
| Technology | 2650 | 970 | 51.75% | 35.26% | 126 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3585 | 1366 | {'Excellent': 492, 'Good': 141, 'Neutral': 186, 'Poor': 547, 'Unknown': 0, 'Pending': 2219} |

## Success Patterns

- Momentum: 1921 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1899 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1263 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 633 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 614 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1717 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1641 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1084 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 547 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 481 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
