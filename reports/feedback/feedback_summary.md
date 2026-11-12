# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-11T21:38:26.065806-05:00
- Validation件数: 3930
- 完了済みValidation: 1606
- 未完了Validation: 2324
- 成功率: 45.52%
- 失敗率: 41.41%
- Result Counts(期間完了分): {'Excellent': 569, 'Poor': 665, 'Neutral': 210, 'Good': 162}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 569 | 569 | 100.00% | 0.00% |
| Good | 162 | 162 | 100.00% | 0.00% |
| Neutral | 2534 | 210 | 0.00% | 0.00% |
| Poor | 665 | 665 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 645 | 260 | {'Excellent': 114, 'Good': 13, 'Neutral': 17, 'Poor': 116, 'Unknown': 0, 'Pending': 385} |
| Mid Score (60-74) | 2555 | 1007 | {'Excellent': 365, 'Good': 115, 'Neutral': 151, 'Poor': 376, 'Unknown': 0, 'Pending': 1548} |
| Low Score (<60) | 730 | 339 | {'Excellent': 90, 'Good': 34, 'Neutral': 42, 'Poor': 173, 'Unknown': 0, 'Pending': 391} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2200 | 943 | 53.02% | 35.84% | 105 |
| Medium | 1730 | 663 | 34.84% | 49.32% | 105 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2925 | 1122 | 43.85% | 42.16% | 157 |
| Moderate | 545 | 208 | 47.12% | 40.38% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 765 | 342 | 35.96% | 51.46% | 43 |
| Consumer Cyclical | 260 | 113 | 20.35% | 61.06% | 21 |
| Technology | 2905 | 1151 | 50.83% | 36.49% | 146 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 3930 | 1606 | {'Excellent': 569, 'Good': 162, 'Neutral': 210, 'Poor': 665, 'Unknown': 0, 'Pending': 2324} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2218 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2193 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1459 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 731 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 709 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2077 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1995 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1320 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 665 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 593 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
