# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-11T18:33:48.303895-04:00
- Validation件数: 935
- 完了済みValidation: 217
- 未完了Validation: 718
- 成功率: 44.70%
- 失敗率: 47.47%
- Result Counts(期間完了分): {'Excellent': 81, 'Poor': 103, 'Neutral': 17, 'Good': 16}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 81 | 81 | 100.00% | 0.00% |
| Good | 16 | 16 | 100.00% | 0.00% |
| Neutral | 735 | 17 | 0.00% | 0.00% |
| Poor | 103 | 103 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 615 | 136 | {'Excellent': 65, 'Good': 5, 'Neutral': 11, 'Poor': 55, 'Unknown': 0, 'Pending': 479} |
| Low Score (<60) | 320 | 81 | {'Excellent': 16, 'Good': 11, 'Neutral': 6, 'Poor': 48, 'Unknown': 0, 'Pending': 239} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 610 | 132 | 37.88% | 54.55% | 10 |
| Medium | 325 | 85 | 55.29% | 36.47% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 395 | 54 | 44.44% | 55.56% | 0 |
| Moderate | 80 | 8 | 75.00% | 25.00% | 0 |
| Unknown | 460 | 155 | 43.23% | 45.81% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 270 | 62 | 30.65% | 59.68% | 6 |
| Consumer Cyclical | 105 | 25 | 36.00% | 56.00% | 2 |
| Technology | 560 | 130 | 53.08% | 40.00% | 9 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 935 | 217 | {'Excellent': 81, 'Good': 16, 'Neutral': 17, 'Poor': 103, 'Unknown': 0, 'Pending': 718} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 299 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 291 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 194 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 97 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 89 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 314 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 309 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 206 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 103 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 98 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
