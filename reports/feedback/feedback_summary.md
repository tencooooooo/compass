# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-07-31T18:53:33.580964-04:00
- Validation件数: 700
- 完了済みValidation: 118
- 未完了Validation: 582
- 成功率: 43.22%
- 失敗率: 44.92%
- Result Counts(期間完了分): {'Excellent': 42, 'Poor': 53, 'Neutral': 14, 'Good': 9}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 42 | 42 | 100.00% | 0.00% |
| Good | 9 | 9 | 100.00% | 0.00% |
| Neutral | 596 | 14 | 0.00% | 0.00% |
| Poor | 53 | 53 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 125 | 20 | {'Excellent': 5, 'Good': 2, 'Neutral': 4, 'Poor': 9, 'Unknown': 0, 'Pending': 105} |
| Mid Score (60-74) | 550 | 92 | {'Excellent': 36, 'Good': 7, 'Neutral': 10, 'Poor': 39, 'Unknown': 0, 'Pending': 458} |
| Low Score (<60) | 25 | 6 | {'Excellent': 1, 'Good': 0, 'Neutral': 0, 'Poor': 5, 'Unknown': 0, 'Pending': 19} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 460 | 76 | 38.16% | 48.68% | 10 |
| Medium | 240 | 42 | 52.38% | 38.10% | 4 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 215 | 18 | 27.78% | 72.22% | 0 |
| Moderate | 25 | 0 | N/A | N/A | 0 |
| Unknown | 460 | 100 | 46.00% | 40.00% | 14 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 200 | 33 | 24.24% | 66.67% | 3 |
| Consumer Cyclical | 70 | 14 | 35.71% | 50.00% | 2 |
| Technology | 430 | 71 | 53.52% | 33.80% | 9 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 700 | 118 | {'Excellent': 42, 'Good': 9, 'Neutral': 14, 'Poor': 53, 'Unknown': 0, 'Pending': 582} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 157 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 153 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 102 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 51 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 47 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 161 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 159 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 106 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 53 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 51 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
