# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-28T21:23:33.007858-04:00
- Validation件数: 3010
- 完了済みValidation: 844
- 未完了Validation: 2166
- 成功率: 45.26%
- 失敗率: 41.82%
- Result Counts(期間完了分): {'Excellent': 313, 'Poor': 353, 'Neutral': 109, 'Good': 69}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 313 | 313 | 100.00% | 0.00% |
| Good | 69 | 69 | 100.00% | 0.00% |
| Neutral | 2275 | 109 | 0.00% | 0.00% |
| Poor | 353 | 353 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 625 | 194 | {'Excellent': 93, 'Good': 17, 'Neutral': 18, 'Poor': 66, 'Unknown': 0, 'Pending': 431} |
| Mid Score (60-74) | 1885 | 498 | {'Excellent': 180, 'Good': 39, 'Neutral': 67, 'Poor': 212, 'Unknown': 0, 'Pending': 1387} |
| Low Score (<60) | 500 | 152 | {'Excellent': 40, 'Good': 13, 'Neutral': 24, 'Poor': 75, 'Unknown': 0, 'Pending': 348} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2015 | 592 | 47.97% | 39.70% | 73 |
| Medium | 995 | 252 | 38.89% | 46.83% | 36 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2085 | 536 | 46.08% | 40.30% | 73 |
| Moderate | 465 | 124 | 46.77% | 39.52% | 17 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 640 | 193 | 35.75% | 50.78% | 26 |
| Consumer Cyclical | 220 | 73 | 20.55% | 69.86% | 7 |
| Technology | 2150 | 578 | 51.56% | 35.29% | 76 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 3010 | 844 | {'Excellent': 313, 'Good': 69, 'Neutral': 109, 'Poor': 353, 'Unknown': 0, 'Pending': 2166} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 1163 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1146 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 761 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 382 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 368 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1117 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1059 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 701 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 353 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 300 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
