# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-07-21T18:46:43.162828-04:00
- Validation件数: 510
- 完了済みValidation: 75
- 未完了Validation: 435
- 成功率: 50.67%
- 失敗率: 38.67%
- Result Counts(期間完了分): {'Excellent': 29, 'Poor': 29, 'Neutral': 8, 'Good': 9}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 29 | 29 | 100.00% | 0.00% |
| Good | 9 | 9 | 100.00% | 0.00% |
| Neutral | 443 | 8 | 0.00% | 0.00% |
| Poor | 29 | 29 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 85 | 12 | {'Excellent': 5, 'Good': 1, 'Neutral': 1, 'Poor': 5, 'Unknown': 0, 'Pending': 73} |
| Mid Score (60-74) | 230 | 34 | {'Excellent': 17, 'Good': 2, 'Neutral': 4, 'Poor': 11, 'Unknown': 0, 'Pending': 196} |
| Low Score (<60) | 195 | 29 | {'Excellent': 7, 'Good': 6, 'Neutral': 3, 'Poor': 13, 'Unknown': 0, 'Pending': 166} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 325 | 41 | 43.90% | 43.90% | 5 |
| Medium | 185 | 34 | 58.82% | 32.35% | 3 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 50 | 0 | N/A | N/A | 0 |
| Unknown | 460 | 75 | 50.67% | 38.67% | 8 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 150 | 22 | 31.82% | 59.09% | 2 |
| Consumer Cyclical | 60 | 10 | 40.00% | 40.00% | 2 |
| Technology | 300 | 43 | 62.79% | 27.91% | 4 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 510 | 75 | {'Excellent': 29, 'Good': 9, 'Neutral': 8, 'Poor': 29, 'Unknown': 0, 'Pending': 435} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 117 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 114 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 76 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 38 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 35 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Growth: 87 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Momentum: 87 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Financial Health: 58 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 29 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 29 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
