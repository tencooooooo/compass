# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-13T18:33:08.134419-04:00
- Validation件数: 1000
- 完了済みValidation: 243
- 未完了Validation: 757
- 成功率: 42.39%
- 失敗率: 49.38%
- Result Counts(期間完了分): {'Excellent': 85, 'Poor': 120, 'Neutral': 20, 'Good': 18}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 85 | 85 | 100.00% | 0.00% |
| Good | 18 | 18 | 100.00% | 0.00% |
| Neutral | 777 | 20 | 0.00% | 0.00% |
| Poor | 120 | 120 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 90 | 18 | {'Excellent': 7, 'Good': 2, 'Neutral': 2, 'Poor': 7, 'Unknown': 0, 'Pending': 72} |
| Mid Score (60-74) | 730 | 175 | {'Excellent': 67, 'Good': 10, 'Neutral': 15, 'Poor': 83, 'Unknown': 0, 'Pending': 555} |
| Low Score (<60) | 180 | 50 | {'Excellent': 11, 'Good': 6, 'Neutral': 3, 'Poor': 30, 'Unknown': 0, 'Pending': 130} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 645 | 152 | 34.87% | 56.58% | 13 |
| Medium | 355 | 91 | 54.95% | 37.36% | 7 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 450 | 64 | 40.62% | 56.25% | 2 |
| Moderate | 90 | 12 | 50.00% | 41.67% | 1 |
| Unknown | 460 | 167 | 42.51% | 47.31% | 17 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 285 | 70 | 27.14% | 62.86% | 7 |
| Consumer Cyclical | 115 | 28 | 35.71% | 57.14% | 2 |
| Technology | 600 | 145 | 51.03% | 41.38% | 11 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1000 | 243 | {'Excellent': 85, 'Good': 18, 'Neutral': 20, 'Poor': 120, 'Unknown': 0, 'Pending': 757} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 318 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 309 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 206 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 103 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 94 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 367 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 360 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 240 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 120 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 113 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
