# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-12T18:31:44.889225-04:00
- Validation件数: 965
- 完了済みValidation: 231
- 未完了Validation: 734
- 成功率: 43.72%
- 失敗率: 48.05%
- Result Counts(期間完了分): {'Excellent': 84, 'Poor': 111, 'Neutral': 19, 'Good': 17}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 84 | 84 | 100.00% | 0.00% |
| Good | 17 | 17 | 100.00% | 0.00% |
| Neutral | 753 | 19 | 0.00% | 0.00% |
| Poor | 111 | 111 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 790 | 183 | {'Excellent': 73, 'Good': 11, 'Neutral': 16, 'Poor': 83, 'Unknown': 0, 'Pending': 607} |
| Low Score (<60) | 175 | 48 | {'Excellent': 11, 'Good': 6, 'Neutral': 3, 'Poor': 28, 'Unknown': 0, 'Pending': 127} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 625 | 144 | 36.81% | 54.86% | 12 |
| Medium | 340 | 87 | 55.17% | 36.78% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 420 | 59 | 42.37% | 54.24% | 2 |
| Moderate | 85 | 10 | 60.00% | 40.00% | 0 |
| Unknown | 460 | 162 | 43.21% | 46.30% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 275 | 66 | 28.79% | 62.12% | 6 |
| Consumer Cyclical | 110 | 27 | 37.04% | 55.56% | 2 |
| Technology | 580 | 138 | 52.17% | 39.86% | 11 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 965 | 231 | {'Excellent': 84, 'Good': 17, 'Neutral': 19, 'Poor': 111, 'Unknown': 0, 'Pending': 734} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 312 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 303 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 202 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 101 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 92 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 339 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 333 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 222 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 111 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 105 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
