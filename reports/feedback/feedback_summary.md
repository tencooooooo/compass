# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-10T19:35:43.024268-04:00
- Validation件数: 2250
- 完了済みValidation: 577
- 未完了Validation: 1673
- 成功率: 41.59%
- 失敗率: 46.10%
- Result Counts(期間完了分): {'Excellent': 197, 'Poor': 266, 'Neutral': 71, 'Good': 43}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 197 | 197 | 100.00% | 0.00% |
| Good | 43 | 43 | 100.00% | 0.00% |
| Neutral | 1744 | 71 | 0.00% | 0.00% |
| Poor | 266 | 266 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 85 | 12 | {'Excellent': 7, 'Good': 3, 'Neutral': 1, 'Poor': 1, 'Unknown': 0, 'Pending': 73} |
| Mid Score (60-74) | 2015 | 532 | {'Excellent': 184, 'Good': 40, 'Neutral': 66, 'Poor': 242, 'Unknown': 0, 'Pending': 1483} |
| Low Score (<60) | 150 | 33 | {'Excellent': 6, 'Good': 0, 'Neutral': 4, 'Poor': 23, 'Unknown': 0, 'Pending': 117} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1580 | 397 | 42.32% | 45.59% | 48 |
| Medium | 670 | 180 | 40.00% | 47.22% | 23 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1445 | 320 | 39.69% | 47.81% | 40 |
| Moderate | 345 | 73 | 49.32% | 34.25% | 12 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 515 | 147 | 27.89% | 58.50% | 20 |
| Consumer Cyclical | 190 | 57 | 26.32% | 64.91% | 5 |
| Technology | 1545 | 373 | 49.33% | 38.34% | 46 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2250 | 577 | {'Excellent': 197, 'Good': 43, 'Neutral': 71, 'Poor': 266, 'Unknown': 0, 'Pending': 1673} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 737 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 720 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 477 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 240 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 226 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 832 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 798 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 531 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 266 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 233 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
