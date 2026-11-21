# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-20T21:57:48.280423-05:00
- Validation件数: 4315
- 完了済みValidation: 1780
- 未完了Validation: 2535
- 成功率: 45.34%
- 失敗率: 42.53%
- Result Counts(期間完了分): {'Excellent': 626, 'Poor': 757, 'Neutral': 216, 'Good': 181}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 626 | 626 | 100.00% | 0.00% |
| Good | 181 | 181 | 100.00% | 0.00% |
| Neutral | 2751 | 216 | 0.00% | 0.00% |
| Poor | 757 | 757 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 250 | 108 | {'Excellent': 12, 'Good': 17, 'Neutral': 23, 'Poor': 56, 'Unknown': 0, 'Pending': 142} |
| Mid Score (60-74) | 2385 | 909 | {'Excellent': 407, 'Good': 71, 'Neutral': 93, 'Poor': 338, 'Unknown': 0, 'Pending': 1476} |
| Low Score (<60) | 1680 | 763 | {'Excellent': 207, 'Good': 93, 'Neutral': 100, 'Poor': 363, 'Unknown': 0, 'Pending': 917} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2425 | 1036 | 52.99% | 36.78% | 106 |
| Medium | 1890 | 744 | 34.68% | 50.54% | 110 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3240 | 1265 | 43.40% | 43.72% | 163 |
| Moderate | 615 | 239 | 48.95% | 40.17% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 850 | 368 | 37.23% | 51.09% | 43 |
| Consumer Cyclical | 315 | 128 | 24.22% | 57.03% | 24 |
| Technology | 3150 | 1284 | 49.77% | 38.63% | 149 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4315 | 1780 | {'Excellent': 626, 'Good': 181, 'Neutral': 216, 'Poor': 757, 'Unknown': 0, 'Pending': 2535} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2462 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2421 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1611 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 807 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 769 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2361 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2271 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1502 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 757 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 679 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
