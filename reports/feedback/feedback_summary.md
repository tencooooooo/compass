# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-05T22:00:53.015200-04:00
- Validation件数: 3215
- 完了済みValidation: 1060
- 未完了Validation: 2155
- 成功率: 46.70%
- 失敗率: 39.91%
- Result Counts(期間完了分): {'Excellent': 406, 'Poor': 423, 'Neutral': 142, 'Good': 89}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 406 | 406 | 100.00% | 0.00% |
| Good | 89 | 89 | 100.00% | 0.00% |
| Neutral | 2297 | 142 | 0.00% | 0.00% |
| Poor | 423 | 423 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 1315 | 425 | {'Excellent': 226, 'Good': 39, 'Neutral': 56, 'Poor': 104, 'Unknown': 0, 'Pending': 890} |
| Low Score (<60) | 1900 | 635 | {'Excellent': 180, 'Good': 50, 'Neutral': 86, 'Poor': 319, 'Unknown': 0, 'Pending': 1265} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 704 | 50.00% | 38.35% | 82 |
| Medium | 1175 | 356 | 40.17% | 42.98% | 60 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2275 | 675 | 47.26% | 38.22% | 98 |
| Moderate | 480 | 155 | 42.58% | 43.23% | 22 |
| Unknown | 460 | 230 | 47.83% | 42.61% | 22 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 680 | 238 | 35.71% | 49.16% | 36 |
| Consumer Cyclical | 225 | 87 | 18.39% | 68.97% | 11 |
| Technology | 2310 | 735 | 53.61% | 33.47% | 95 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3210 | 1060 | {'Excellent': 406, 'Good': 89, 'Neutral': 142, 'Poor': 423, 'Unknown': 0, 'Pending': 2150} |

## Success Patterns

- Momentum: 1503 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1485 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 987 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 495 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 480 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1339 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1269 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 839 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 423 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 360 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
