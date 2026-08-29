# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-28T23:27:46.426431-04:00
- Validation件数: 1665
- 完了済みValidation: 397
- 未完了Validation: 1268
- 成功率: 40.30%
- 失敗率: 49.12%
- Result Counts(期間完了分): {'Excellent': 130, 'Poor': 195, 'Neutral': 42, 'Good': 30}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 130 | 130 | 100.00% | 0.00% |
| Good | 30 | 30 | 100.00% | 0.00% |
| Neutral | 1310 | 42 | 0.00% | 0.00% |
| Poor | 195 | 195 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 340 | 89 | {'Excellent': 44, 'Good': 9, 'Neutral': 9, 'Poor': 27, 'Unknown': 0, 'Pending': 251} |
| Mid Score (60-74) | 1080 | 239 | {'Excellent': 70, 'Good': 15, 'Neutral': 27, 'Poor': 127, 'Unknown': 0, 'Pending': 841} |
| Low Score (<60) | 245 | 69 | {'Excellent': 16, 'Good': 6, 'Neutral': 6, 'Poor': 41, 'Unknown': 0, 'Pending': 176} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1150 | 264 | 36.36% | 53.79% | 26 |
| Medium | 515 | 133 | 48.12% | 39.85% | 16 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 975 | 176 | 35.80% | 54.55% | 17 |
| Moderate | 230 | 37 | 54.05% | 29.73% | 6 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 405 | 102 | 25.49% | 61.76% | 13 |
| Consumer Cyclical | 165 | 42 | 35.71% | 54.76% | 4 |
| Technology | 1095 | 253 | 47.04% | 43.08% | 25 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1665 | 397 | {'Excellent': 130, 'Good': 30, 'Neutral': 42, 'Poor': 195, 'Unknown': 0, 'Pending': 1268} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 495 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 480 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 319 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 160 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 146 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 599 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 585 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 390 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 195 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 181 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
