# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-17T18:16:27.861523-04:00
- Validation件数: 1085
- 完了済みValidation: 273
- 未完了Validation: 812
- 成功率: 41.03%
- 失敗率: 50.18%
- Result Counts(期間完了分): {'Excellent': 92, 'Poor': 137, 'Neutral': 24, 'Good': 20}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 92 | 92 | 100.00% | 0.00% |
| Good | 20 | 20 | 100.00% | 0.00% |
| Neutral | 836 | 24 | 0.00% | 0.00% |
| Poor | 137 | 137 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 100 | 21 | {'Excellent': 7, 'Good': 3, 'Neutral': 2, 'Poor': 9, 'Unknown': 0, 'Pending': 79} |
| Mid Score (60-74) | 670 | 163 | {'Excellent': 65, 'Good': 11, 'Neutral': 14, 'Poor': 73, 'Unknown': 0, 'Pending': 507} |
| Low Score (<60) | 315 | 89 | {'Excellent': 20, 'Good': 6, 'Neutral': 8, 'Poor': 55, 'Unknown': 0, 'Pending': 226} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 705 | 176 | 34.66% | 56.25% | 16 |
| Medium | 380 | 97 | 52.58% | 39.18% | 8 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 520 | 75 | 38.67% | 57.33% | 3 |
| Moderate | 105 | 14 | 42.86% | 42.86% | 2 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 295 | 79 | 24.05% | 65.82% | 8 |
| Consumer Cyclical | 125 | 31 | 35.48% | 58.06% | 2 |
| Technology | 665 | 163 | 50.31% | 41.10% | 14 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1085 | 273 | {'Excellent': 92, 'Good': 20, 'Neutral': 24, 'Poor': 137, 'Unknown': 0, 'Pending': 812} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 346 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 336 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 224 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 112 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 102 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 420 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 411 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 274 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 137 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 128 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
