# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-23T20:08:55.161271-04:00
- Validation件数: 2830
- 完了済みValidation: 756
- 未完了Validation: 2074
- 成功率: 44.84%
- 失敗率: 42.46%
- Result Counts(期間完了分): {'Excellent': 274, 'Poor': 321, 'Neutral': 96, 'Good': 65}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 274 | 274 | 100.00% | 0.00% |
| Good | 65 | 65 | 100.00% | 0.00% |
| Neutral | 2170 | 96 | 0.00% | 0.00% |
| Poor | 321 | 321 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 555 | 140 | {'Excellent': 73, 'Good': 15, 'Neutral': 11, 'Poor': 41, 'Unknown': 0, 'Pending': 415} |
| Mid Score (60-74) | 1785 | 483 | {'Excellent': 158, 'Good': 38, 'Neutral': 70, 'Poor': 217, 'Unknown': 0, 'Pending': 1302} |
| Low Score (<60) | 490 | 133 | {'Excellent': 43, 'Good': 12, 'Neutral': 15, 'Poor': 63, 'Unknown': 0, 'Pending': 357} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1960 | 521 | 46.64% | 41.27% | 63 |
| Medium | 870 | 235 | 40.85% | 45.11% | 33 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1925 | 466 | 44.64% | 42.06% | 62 |
| Moderate | 445 | 106 | 50.94% | 34.91% | 15 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 610 | 176 | 35.80% | 50.57% | 24 |
| Consumer Cyclical | 215 | 68 | 22.06% | 67.65% | 7 |
| Technology | 2005 | 512 | 50.98% | 36.33% | 65 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2830 | 756 | {'Excellent': 274, 'Good': 65, 'Neutral': 96, 'Poor': 321, 'Unknown': 0, 'Pending': 2074} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 1034 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1017 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 675 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 339 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 325 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1010 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 963 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 640 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 321 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 276 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
