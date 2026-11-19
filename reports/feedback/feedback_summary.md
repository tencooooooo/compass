# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-11-18T21:54:59.919331-05:00
- Validation件数: 4210
- 完了済みValidation: 1732
- 未完了Validation: 2478
- 成功率: 45.50%
- 失敗率: 42.03%
- Result Counts(期間完了分): {'Excellent': 613, 'Poor': 728, 'Neutral': 216, 'Good': 175}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 613 | 613 | 100.00% | 0.00% |
| Good | 175 | 175 | 100.00% | 0.00% |
| Neutral | 2694 | 216 | 0.00% | 0.00% |
| Poor | 728 | 728 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 1170 | 499 | {'Excellent': 199, 'Good': 46, 'Neutral': 73, 'Poor': 181, 'Unknown': 0, 'Pending': 671} |
| Mid Score (60-74) | 1080 | 385 | {'Excellent': 173, 'Good': 32, 'Neutral': 38, 'Poor': 142, 'Unknown': 0, 'Pending': 695} |
| Low Score (<60) | 1960 | 848 | {'Excellent': 241, 'Good': 97, 'Neutral': 105, 'Poor': 405, 'Unknown': 0, 'Pending': 1112} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 2360 | 1016 | 53.25% | 36.32% | 106 |
| Medium | 1850 | 716 | 34.50% | 50.14% | 110 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 3160 | 1226 | 43.64% | 43.07% | 163 |
| Moderate | 590 | 230 | 48.70% | 40.00% | 26 |
| Unknown | 460 | 276 | 51.09% | 39.13% | 27 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 830 | 359 | 36.49% | 51.53% | 43 |
| Consumer Cyclical | 295 | 125 | 22.40% | 58.40% | 24 |
| Technology | 3085 | 1248 | 50.40% | 37.66% | 149 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 4210 | 1732 | {'Excellent': 613, 'Good': 175, 'Neutral': 216, 'Poor': 728, 'Unknown': 0, 'Pending': 2478} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 2398 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 2364 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1573 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 788 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 757 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 2272 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 2184 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 1445 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 728 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 651 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
