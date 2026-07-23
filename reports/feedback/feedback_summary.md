# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-07-23T18:49:22.478462-04:00
- Validation件数: 525
- 完了済みValidation: 88
- 未完了Validation: 437
- 成功率: 46.59%
- 失敗率: 40.91%
- Result Counts(期間完了分): {'Excellent': 32, 'Poor': 36, 'Neutral': 11, 'Good': 9}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 32 | 32 | 100.00% | 0.00% |
| Good | 9 | 9 | 100.00% | 0.00% |
| Neutral | 448 | 11 | 0.00% | 0.00% |
| Poor | 36 | 36 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |
| Mid Score (60-74) | 325 | 55 | {'Excellent': 25, 'Good': 3, 'Neutral': 7, 'Poor': 20, 'Unknown': 0, 'Pending': 270} |
| Low Score (<60) | 200 | 33 | {'Excellent': 7, 'Good': 6, 'Neutral': 4, 'Poor': 16, 'Unknown': 0, 'Pending': 167} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 335 | 53 | 39.62% | 45.28% | 8 |
| Medium | 190 | 35 | 57.14% | 34.29% | 3 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 65 | 0 | N/A | N/A | 0 |
| Unknown | 460 | 88 | 46.59% | 40.91% | 11 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 150 | 26 | 26.92% | 65.38% | 2 |
| Consumer Cyclical | 60 | 11 | 36.36% | 45.45% | 2 |
| Technology | 315 | 51 | 58.82% | 27.45% | 7 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 525 | 88 | {'Excellent': 32, 'Good': 9, 'Neutral': 11, 'Poor': 36, 'Unknown': 0, 'Pending': 437} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 126 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 123 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 82 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 41 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 38 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 109 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 108 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 72 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 36 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 35 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
