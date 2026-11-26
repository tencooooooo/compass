# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-25T22:53:10.995136-05:00
- Validation件数: 4440
- 完了済みValidation: 1873
- 未完了Validation: 2567
- 成功率: 44.63%
- 失敗率: 43.57%
- Result Counts(期間完了分): {'Excellent': 645, 'Poor': 816, 'Neutral': 221, 'Good': 191}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 645 | 645 | 100.00% | 0.00% |
| Good | 191 | 191 | 100.00% | 0.00% |
| Neutral | 2788 | 221 | 0.00% | 0.00% |
| Poor | 816 | 816 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 2725 | 1086 | {'Excellent': 435, 'Good': 99, 'Neutral': 119, 'Poor': 433, 'Unknown': 0, 'Pending': 1639} |
| Low Score (<60) | 1715 | 787 | {'Excellent': 210, 'Good': 92, 'Neutral': 102, 'Poor': 383, 'Unknown': 0, 'Pending': 928} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2520 | 1096 | 52.10% | 37.96% | 109 |
| Medium | 1920 | 777 | 34.11% | 51.48% | 112 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3325 | 1343 | 42.74% | 44.90% | 166 |
| Moderate | 655 | 254 | 47.64% | 41.34% | 28 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 870 | 386 | 37.05% | 51.55% | 44 |
| Consumer Cyclical | 340 | 136 | 25.00% | 55.15% | 27 |
| Technology | 3230 | 1351 | 48.78% | 40.12% | 150 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4440 | 1873 | {'Excellent': 645, 'Good': 191, 'Neutral': 221, 'Poor': 816, 'Unknown': 0, 'Pending': 2567} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2554 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2508 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1669 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 836 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 793 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2546 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2448 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1618 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 816 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 732 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
