# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-21T20:26:43.977630-04:00
- Validation件数: 2710
- 完了済みValidation: 706
- 未完了Validation: 2004
- 成功率: 43.48%
- 失敗率: 43.48%
- Result Counts(期間完了分): {'Excellent': 251, 'Poor': 307, 'Neutral': 92, 'Good': 56}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 251 | 251 | 100.00% | 0.00% |
| Good | 56 | 56 | 100.00% | 0.00% |
| Neutral | 2096 | 92 | 0.00% | 0.00% |
| Poor | 307 | 307 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 125 | 22 | {'Excellent': 4, 'Good': 2, 'Neutral': 0, 'Poor': 16, 'Unknown': 0, 'Pending': 103} |
| Mid Score (60-74) | 2450 | 655 | {'Excellent': 238, 'Good': 54, 'Neutral': 90, 'Poor': 273, 'Unknown': 0, 'Pending': 1795} |
| Low Score (<60) | 135 | 29 | {'Excellent': 9, 'Good': 0, 'Neutral': 2, 'Poor': 18, 'Unknown': 0, 'Pending': 106} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1895 | 488 | 45.49% | 42.21% | 60 |
| Medium | 815 | 218 | 38.99% | 46.33% | 32 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1825 | 428 | 42.76% | 43.46% | 59 |
| Moderate | 425 | 94 | 50.00% | 35.11% | 14 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 590 | 168 | 33.93% | 51.79% | 24 |
| Consumer Cyclical | 210 | 66 | 22.73% | 68.18% | 6 |
| Technology | 1910 | 472 | 49.79% | 37.08% | 62 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2710 | 706 | {'Excellent': 251, 'Good': 56, 'Neutral': 92, 'Poor': 307, 'Unknown': 0, 'Pending': 2004} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 938 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 921 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 611 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 307 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 293 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 965 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 921 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 612 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 307 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 265 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
