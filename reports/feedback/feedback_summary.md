# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-05T18:50:39.912420-04:00
- Validation件数: 805
- 完了済みValidation: 166
- 未完了Validation: 639
- 成功率: 45.78%
- 失敗率: 43.98%
- Result Counts(期間完了分): {'Excellent': 63, 'Poor': 73, 'Neutral': 17, 'Good': 13}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 63 | 63 | 100.00% | 0.00% |
| Good | 13 | 13 | 100.00% | 0.00% |
| Neutral | 656 | 17 | 0.00% | 0.00% |
| Poor | 73 | 73 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 125 | 26 | {'Excellent': 18, 'Good': 0, 'Neutral': 3, 'Poor': 5, 'Unknown': 0, 'Pending': 99} |
| Mid Score (60-74) | 520 | 104 | {'Excellent': 34, 'Good': 8, 'Neutral': 11, 'Poor': 51, 'Unknown': 0, 'Pending': 416} |
| Low Score (<60) | 160 | 36 | {'Excellent': 11, 'Good': 5, 'Neutral': 3, 'Poor': 17, 'Unknown': 0, 'Pending': 124} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 535 | 93 | 38.71% | 50.54% | 10 |
| Medium | 270 | 73 | 54.79% | 35.62% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 295 | 31 | 41.94% | 58.06% | 0 |
| Moderate | 50 | 4 | 75.00% | 25.00% | 0 |
| Unknown | 460 | 131 | 45.80% | 41.22% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 230 | 47 | 31.91% | 55.32% | 6 |
| Consumer Cyclical | 85 | 18 | 38.89% | 50.00% | 2 |
| Technology | 490 | 101 | 53.47% | 37.62% | 9 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 805 | 166 | {'Excellent': 63, 'Good': 13, 'Neutral': 17, 'Poor': 73, 'Unknown': 0, 'Pending': 639} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 234 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 228 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 152 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 76 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 70 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 221 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 219 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 146 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 73 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 71 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
