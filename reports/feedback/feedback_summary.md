# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-19T21:47:48.238317-05:00
- Validation件数: 4260
- 完了済みValidation: 1760
- 未完了Validation: 2500
- 成功率: 45.40%
- 失敗率: 42.33%
- Result Counts(期間完了分): {'Excellent': 622, 'Poor': 745, 'Neutral': 216, 'Good': 177}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 622 | 622 | 100.00% | 0.00% |
| Good | 177 | 177 | 100.00% | 0.00% |
| Neutral | 2716 | 216 | 0.00% | 0.00% |
| Poor | 745 | 745 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 2850 | 1150 | {'Excellent': 482, 'Good': 112, 'Neutral': 135, 'Poor': 421, 'Unknown': 0, 'Pending': 1700} |
| Low Score (<60) | 1410 | 610 | {'Excellent': 140, 'Good': 65, 'Neutral': 81, 'Poor': 324, 'Unknown': 0, 'Pending': 800} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2390 | 1026 | 53.22% | 36.45% | 106 |
| Medium | 1870 | 734 | 34.47% | 50.54% | 110 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3205 | 1248 | 43.51% | 43.43% | 163 |
| Moderate | 595 | 236 | 48.73% | 40.25% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 840 | 363 | 36.64% | 51.52% | 43 |
| Consumer Cyclical | 300 | 127 | 23.62% | 57.48% | 24 |
| Technology | 3120 | 1270 | 50.08% | 38.19% | 149 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4260 | 1760 | {'Excellent': 622, 'Good': 177, 'Neutral': 216, 'Poor': 745, 'Unknown': 0, 'Pending': 2500} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2435 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2397 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1595 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 799 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 764 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2325 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2235 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1478 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 745 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 667 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
