# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-13T20:56:31.413632-05:00
- Validation件数: 4045
- 完了済みValidation: 1631
- 未完了Validation: 2414
- 成功率: 45.62%
- 失敗率: 41.45%
- Result Counts(期間完了分): {'Excellent': 578, 'Poor': 676, 'Neutral': 211, 'Good': 166}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 578 | 578 | 100.00% | 0.00% |
| Good | 166 | 166 | 100.00% | 0.00% |
| Neutral | 2625 | 211 | 0.00% | 0.00% |
| Poor | 676 | 676 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 2395 | 916 | {'Excellent': 386, 'Good': 75, 'Neutral': 104, 'Poor': 351, 'Unknown': 0, 'Pending': 1479} |
| Low Score (<60) | 1650 | 715 | {'Excellent': 192, 'Good': 91, 'Neutral': 107, 'Poor': 325, 'Unknown': 0, 'Pending': 935} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2240 | 950 | 53.37% | 35.58% | 105 |
| Medium | 1805 | 681 | 34.80% | 49.63% | 106 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3025 | 1144 | 43.97% | 42.22% | 158 |
| Moderate | 560 | 211 | 47.39% | 40.28% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 795 | 345 | 35.94% | 51.59% | 43 |
| Consumer Cyclical | 270 | 115 | 21.74% | 60.00% | 21 |
| Technology | 2980 | 1171 | 50.81% | 36.64% | 147 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4045 | 1631 | {'Excellent': 578, 'Good': 166, 'Neutral': 211, 'Poor': 676, 'Unknown': 0, 'Pending': 2414} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2260 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2232 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1485 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 744 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 719 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2110 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2028 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1342 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 676 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 604 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
