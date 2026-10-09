# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-08T21:36:51.267449-04:00
- Validation件数: 3310
- 完了済みValidation: 1117
- 未完了Validation: 2193
- 成功率: 47.45%
- 失敗率: 39.39%
- Result Counts(期間完了分): {'Excellent': 428, 'Poor': 440, 'Neutral': 147, 'Good': 102}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 428 | 428 | 100.00% | 0.00% |
| Good | 102 | 102 | 100.00% | 0.00% |
| Neutral | 2340 | 147 | 0.00% | 0.00% |
| Poor | 440 | 440 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 895 | 297 | {'Excellent': 158, 'Good': 28, 'Neutral': 34, 'Poor': 77, 'Unknown': 0, 'Pending': 598} |
| Low Score (<60) | 2415 | 820 | {'Excellent': 270, 'Good': 74, 'Neutral': 113, 'Poor': 363, 'Unknown': 0, 'Pending': 1595} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 734 | 50.54% | 38.15% | 83 |
| Medium | 1270 | 383 | 41.51% | 41.78% | 64 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2370 | 709 | 47.95% | 37.66% | 102 |
| Moderate | 480 | 161 | 42.24% | 43.48% | 23 |
| Unknown | 460 | 247 | 49.39% | 41.70% | 22 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 700 | 250 | 36.40% | 48.80% | 37 |
| Consumer Cyclical | 225 | 92 | 19.57% | 68.48% | 11 |
| Technology | 2385 | 775 | 54.32% | 32.90% | 99 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3305 | 1117 | {'Excellent': 428, 'Good': 102, 'Neutral': 147, 'Poor': 440, 'Unknown': 0, 'Pending': 2188} |

## Success Patterns

- Momentum: 1610 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1590 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1057 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 530 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 513 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1392 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1320 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 872 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 440 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 376 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
