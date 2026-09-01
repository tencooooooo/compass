# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-31T20:56:28.793785-04:00
- Validation件数: 1735
- 完了済みValidation: 424
- 未完了Validation: 1311
- 成功率: 40.80%
- 失敗率: 48.11%
- Result Counts(期間完了分): {'Excellent': 141, 'Poor': 204, 'Neutral': 47, 'Good': 32}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 141 | 141 | 100.00% | 0.00% |
| Good | 32 | 32 | 100.00% | 0.00% |
| Neutral | 1358 | 47 | 0.00% | 0.00% |
| Poor | 204 | 204 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 255 | 65 | {'Excellent': 41, 'Good': 5, 'Neutral': 6, 'Poor': 13, 'Unknown': 0, 'Pending': 190} |
| Mid Score (60-74) | 1225 | 286 | {'Excellent': 92, 'Good': 19, 'Neutral': 32, 'Poor': 143, 'Unknown': 0, 'Pending': 939} |
| Low Score (<60) | 255 | 73 | {'Excellent': 8, 'Good': 8, 'Neutral': 9, 'Poor': 48, 'Unknown': 0, 'Pending': 182} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1210 | 285 | 37.89% | 51.58% | 30 |
| Medium | 525 | 139 | 46.76% | 41.01% | 17 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1035 | 199 | 36.68% | 52.76% | 21 |
| Moderate | 240 | 41 | 56.10% | 26.83% | 7 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 420 | 110 | 25.45% | 60.00% | 16 |
| Consumer Cyclical | 165 | 44 | 34.09% | 56.82% | 4 |
| Technology | 1150 | 270 | 48.15% | 41.85% | 27 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1735 | 424 | {'Excellent': 141, 'Good': 32, 'Neutral': 47, 'Poor': 204, 'Unknown': 0, 'Pending': 1311} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 534 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 519 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 345 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 173 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 159 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 629 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 612 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 408 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 204 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 187 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
