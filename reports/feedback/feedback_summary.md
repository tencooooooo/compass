# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-20T18:19:07.196041-04:00
- Validation件数: 1270
- 完了済みValidation: 302
- 未完了Validation: 968
- 成功率: 39.40%
- 失敗率: 51.66%
- Result Counts(期間完了分): {'Excellent': 98, 'Poor': 156, 'Neutral': 27, 'Good': 21}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 98 | 98 | 100.00% | 0.00% |
| Good | 21 | 21 | 100.00% | 0.00% |
| Neutral | 995 | 27 | 0.00% | 0.00% |
| Poor | 156 | 156 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 750 | 157 | {'Excellent': 71, 'Good': 10, 'Neutral': 14, 'Poor': 62, 'Unknown': 0, 'Pending': 593} |
| Low Score (<60) | 520 | 145 | {'Excellent': 27, 'Good': 11, 'Neutral': 13, 'Poor': 94, 'Unknown': 0, 'Pending': 375} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 850 | 194 | 34.02% | 57.73% | 16 |
| Medium | 420 | 108 | 49.07% | 40.74% | 11 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 675 | 100 | 33.00% | 62.00% | 5 |
| Moderate | 135 | 18 | 50.00% | 33.33% | 3 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 315 | 87 | 21.84% | 66.67% | 10 |
| Consumer Cyclical | 140 | 35 | 34.29% | 57.14% | 3 |
| Technology | 815 | 180 | 48.89% | 43.33% | 14 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1270 | 302 | {'Excellent': 98, 'Good': 21, 'Neutral': 27, 'Poor': 156, 'Unknown': 0, 'Pending': 968} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 368 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 357 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 238 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 119 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 108 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 479 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 468 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 312 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 156 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 145 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
