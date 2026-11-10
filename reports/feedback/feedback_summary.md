# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-09T22:56:02.743816-05:00
- Validation件数: 3785
- 完了済みValidation: 1587
- 未完了Validation: 2198
- 成功率: 45.49%
- 失敗率: 41.34%
- Result Counts(期間完了分): {'Excellent': 561, 'Poor': 656, 'Neutral': 209, 'Good': 161}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 561 | 561 | 100.00% | 0.00% |
| Good | 161 | 161 | 100.00% | 0.00% |
| Neutral | 2407 | 209 | 0.00% | 0.00% |
| Poor | 656 | 656 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 790 | 327 | {'Excellent': 134, 'Good': 32, 'Neutral': 55, 'Poor': 106, 'Unknown': 0, 'Pending': 463} |
| Mid Score (60-74) | 2415 | 995 | {'Excellent': 390, 'Good': 104, 'Neutral': 114, 'Poor': 387, 'Unknown': 0, 'Pending': 1420} |
| Low Score (<60) | 580 | 265 | {'Excellent': 37, 'Good': 25, 'Neutral': 40, 'Poor': 163, 'Unknown': 0, 'Pending': 315} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2105 | 936 | 52.67% | 36.11% | 105 |
| Medium | 1680 | 651 | 35.18% | 48.85% | 104 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 2830 | 1105 | 43.89% | 41.99% | 156 |
| Moderate | 495 | 206 | 46.60% | 40.78% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 735 | 338 | 36.09% | 51.18% | 43 |
| Consumer Cyclical | 240 | 111 | 19.82% | 62.16% | 20 |
| Technology | 2810 | 1138 | 50.79% | 36.38% | 146 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 3785 | 1587 | {'Excellent': 561, 'Good': 161, 'Neutral': 209, 'Poor': 656, 'Unknown': 0, 'Pending': 2198} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2190 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2166 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1441 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 722 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 701 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2050 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 1968 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1302 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 656 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 584 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
