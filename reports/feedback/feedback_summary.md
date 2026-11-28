# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-27T22:41:02.832250-05:00
- Validation件数: 4590
- 完了済みValidation: 1920
- 未完了Validation: 2670
- 成功率: 44.58%
- 失敗率: 43.75%
- Result Counts(期間完了分): {'Excellent': 661, 'Poor': 840, 'Neutral': 224, 'Good': 195}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 661 | 661 | 100.00% | 0.00% |
| Good | 195 | 195 | 100.00% | 0.00% |
| Neutral | 2894 | 224 | 0.00% | 0.00% |
| Poor | 840 | 840 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 270 | 117 | {'Excellent': 12, 'Good': 20, 'Neutral': 26, 'Poor': 59, 'Unknown': 0, 'Pending': 153} |
| Mid Score (60-74) | 3950 | 1647 | {'Excellent': 599, 'Good': 168, 'Neutral': 190, 'Poor': 690, 'Unknown': 0, 'Pending': 2303} |
| Low Score (<60) | 370 | 156 | {'Excellent': 50, 'Good': 7, 'Neutral': 8, 'Poor': 91, 'Unknown': 0, 'Pending': 214} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2600 | 1120 | 52.05% | 38.21% | 109 |
| Medium | 1990 | 800 | 34.12% | 51.50% | 115 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3435 | 1382 | 42.62% | 45.22% | 168 |
| Moderate | 695 | 262 | 48.09% | 40.84% | 29 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 910 | 394 | 37.56% | 51.02% | 45 |
| Consumer Cyclical | 365 | 141 | 26.24% | 53.90% | 28 |
| Technology | 3315 | 1385 | 48.45% | 40.65% | 151 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4590 | 1920 | {'Excellent': 661, 'Good': 195, 'Neutral': 224, 'Poor': 840, 'Unknown': 0, 'Pending': 2670} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2619 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2568 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1709 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 856 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 808 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2619 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2520 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1666 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 840 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 755 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
