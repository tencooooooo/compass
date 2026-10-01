# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-30T20:57:32.743969-04:00
- Validation件数: 3115
- 完了済みValidation: 894
- 未完了Validation: 2221
- 成功率: 44.97%
- 失敗率: 42.17%
- Result Counts(期間完了分): {'Excellent': 331, 'Poor': 377, 'Neutral': 115, 'Good': 71}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 331 | 331 | 100.00% | 0.00% |
| Good | 71 | 71 | 100.00% | 0.00% |
| Neutral | 2336 | 115 | 0.00% | 0.00% |
| Poor | 377 | 377 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 645 | 202 | {'Excellent': 97, 'Good': 18, 'Neutral': 20, 'Poor': 67, 'Unknown': 0, 'Pending': 443} |
| Mid Score (60-74) | 2255 | 633 | {'Excellent': 220, 'Good': 53, 'Neutral': 91, 'Poor': 269, 'Unknown': 0, 'Pending': 1622} |
| Low Score (<60) | 215 | 59 | {'Excellent': 14, 'Good': 0, 'Neutral': 4, 'Poor': 41, 'Unknown': 0, 'Pending': 156} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 623 | 48.31% | 39.97% | 73 |
| Medium | 1075 | 271 | 37.27% | 47.23% | 42 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2175 | 570 | 45.96% | 40.35% | 78 |
| Moderate | 480 | 132 | 43.94% | 43.18% | 17 |
| Unknown | 460 | 192 | 42.71% | 46.88% | 20 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 660 | 203 | 35.47% | 51.23% | 27 |
| Consumer Cyclical | 225 | 78 | 19.23% | 70.51% | 8 |
| Technology | 2230 | 613 | 51.39% | 35.56% | 80 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 3115 | 894 | {'Excellent': 331, 'Good': 71, 'Neutral': 115, 'Poor': 377, 'Unknown': 0, 'Pending': 2221} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 1223 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1206 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 801 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 402 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 388 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1193 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1131 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 749 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 377 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 320 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
