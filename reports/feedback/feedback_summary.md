# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-10-27T20:51:29.497400-04:00
- Validation件数: 3610
- 完了済みValidation: 1406
- 未完了Validation: 2204
- 成功率: 46.51%
- 失敗率: 39.97%
- Result Counts(期間完了分): {'Excellent': 506, 'Poor': 562, 'Neutral': 190, 'Good': 148}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 506 | 506 | 100.00% | 0.00% |
| Good | 148 | 148 | 100.00% | 0.00% |
| Neutral | 2394 | 190 | 0.00% | 0.00% |
| Poor | 562 | 562 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 425 | 163 | {'Excellent': 73, 'Good': 10, 'Neutral': 12, 'Poor': 68, 'Unknown': 0, 'Pending': 262} |
| Low Score (<60) | 3185 | 1243 | {'Excellent': 433, 'Good': 138, 'Neutral': 178, 'Poor': 494, 'Unknown': 0, 'Pending': 1942} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2040 | 885 | 51.86% | 36.72% | 101 |
| Medium | 1570 | 521 | 37.43% | 45.49% | 89 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2670 | 940 | 45.64% | 39.79% | 137 |
| Moderate | 480 | 190 | 44.21% | 42.11% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 715 | 304 | 37.17% | 48.68% | 43 |
| Consumer Cyclical | 225 | 101 | 20.79% | 62.38% | 17 |
| Technology | 2670 | 1001 | 51.95% | 35.06% | 130 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 5 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 5} |
| No Events | 3605 | 1406 | {'Excellent': 506, 'Good': 148, 'Neutral': 190, 'Poor': 562, 'Unknown': 0, 'Pending': 2199} |

## Success Patterns

- Momentum: 1985 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1962 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1305 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 654 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 634 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1762 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1686 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1114 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 562 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 496 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
