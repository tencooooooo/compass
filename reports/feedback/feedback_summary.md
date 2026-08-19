# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-19T18:16:41.278159-04:00
- Validation件数: 1210
- 完了済みValidation: 291
- 未完了Validation: 919
- 成功率: 40.55%
- 失敗率: 50.17%
- Result Counts(期間完了分): {'Excellent': 97, 'Poor': 146, 'Neutral': 27, 'Good': 21}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 97 | 97 | 100.00% | 0.00% |
| Good | 21 | 21 | 100.00% | 0.00% |
| Neutral | 946 | 27 | 0.00% | 0.00% |
| Poor | 146 | 146 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 15 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 15} |
| Mid Score (60-74) | 1170 | 281 | {'Excellent': 96, 'Good': 21, 'Neutral': 27, 'Poor': 137, 'Unknown': 0, 'Pending': 889} |
| Low Score (<60) | 25 | 10 | {'Excellent': 1, 'Good': 0, 'Neutral': 0, 'Poor': 9, 'Unknown': 0, 'Pending': 15} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 805 | 187 | 34.76% | 56.68% | 16 |
| Medium | 405 | 104 | 50.96% | 38.46% | 11 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 630 | 90 | 36.67% | 57.78% | 5 |
| Moderate | 120 | 17 | 47.06% | 35.29% | 3 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 310 | 83 | 22.89% | 65.06% | 10 |
| Consumer Cyclical | 135 | 34 | 35.29% | 55.88% | 3 |
| Technology | 765 | 174 | 50.00% | 41.95% | 14 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1210 | 291 | {'Excellent': 97, 'Good': 21, 'Neutral': 27, 'Poor': 146, 'Unknown': 0, 'Pending': 919} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 365 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 354 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 236 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 118 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 107 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 448 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 438 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 292 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 146 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 136 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
