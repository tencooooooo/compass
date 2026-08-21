# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-21T18:15:30.455934-04:00
- Validation件数: 1350
- 完了済みValidation: 308
- 未完了Validation: 1042
- 成功率: 39.29%
- 失敗率: 51.95%
- Result Counts(期間完了分): {'Excellent': 99, 'Poor': 160, 'Neutral': 27, 'Good': 22}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 99 | 99 | 100.00% | 0.00% |
| Good | 22 | 22 | 100.00% | 0.00% |
| Neutral | 1069 | 27 | 0.00% | 0.00% |
| Poor | 160 | 160 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 1140 | 249 | {'Excellent': 85, 'Good': 16, 'Neutral': 24, 'Poor': 124, 'Unknown': 0, 'Pending': 891} |
| Low Score (<60) | 210 | 59 | {'Excellent': 14, 'Good': 6, 'Neutral': 3, 'Poor': 36, 'Unknown': 0, 'Pending': 151} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 910 | 197 | 34.01% | 57.87% | 16 |
| Medium | 440 | 111 | 48.65% | 41.44% | 11 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 725 | 104 | 32.69% | 62.50% | 5 |
| Moderate | 165 | 20 | 50.00% | 35.00% | 3 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 330 | 88 | 22.73% | 65.91% | 10 |
| Consumer Cyclical | 145 | 36 | 33.33% | 58.33% | 3 |
| Technology | 875 | 184 | 48.37% | 44.02% | 14 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1350 | 308 | {'Excellent': 99, 'Good': 22, 'Neutral': 27, 'Poor': 160, 'Unknown': 0, 'Pending': 1042} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 374 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 363 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 242 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 121 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 110 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 492 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 480 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 320 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 160 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 148 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
