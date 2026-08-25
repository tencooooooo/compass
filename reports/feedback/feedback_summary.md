# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-08-25T18:18:51.343243-04:00
- Validation件数: 1500
- 完了済みValidation: 338
- 未完了Validation: 1162
- 成功率: 38.76%
- 失敗率: 52.07%
- Result Counts(期間完了分): {'Excellent': 107, 'Poor': 176, 'Neutral': 31, 'Good': 24}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 107 | 107 | 100.00% | 0.00% |
| Good | 24 | 24 | 100.00% | 0.00% |
| Neutral | 1193 | 31 | 0.00% | 0.00% |
| Poor | 176 | 176 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 190 | 52 | {'Excellent': 31, 'Good': 5, 'Neutral': 4, 'Poor': 12, 'Unknown': 0, 'Pending': 138} |
| Mid Score (60-74) | 1080 | 223 | {'Excellent': 61, 'Good': 13, 'Neutral': 23, 'Poor': 126, 'Unknown': 0, 'Pending': 857} |
| Low Score (<60) | 230 | 63 | {'Excellent': 15, 'Good': 6, 'Neutral': 4, 'Poor': 38, 'Unknown': 0, 'Pending': 167} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1030 | 220 | 33.18% | 58.18% | 19 |
| Medium | 470 | 118 | 49.15% | 40.68% | 12 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 840 | 132 | 32.58% | 60.61% | 9 |
| Moderate | 200 | 22 | 50.00% | 36.36% | 3 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 370 | 91 | 25.27% | 63.74% | 10 |
| Consumer Cyclical | 155 | 38 | 34.21% | 55.26% | 4 |
| Technology | 975 | 209 | 45.45% | 46.41% | 17 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1500 | 338 | {'Excellent': 107, 'Good': 24, 'Neutral': 31, 'Poor': 176, 'Unknown': 0, 'Pending': 1162} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 405 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 393 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 262 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 131 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 119 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 540 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 528 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 352 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 176 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 164 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
