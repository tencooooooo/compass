# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-01T19:42:41.769298-04:00
- Validation件数: 1800
- 完了済みValidation: 440
- 未完了Validation: 1360
- 成功率: 41.36%
- 失敗率: 47.95%
- Result Counts(期間完了分): {'Excellent': 150, 'Poor': 211, 'Neutral': 47, 'Good': 32}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 150 | 150 | 100.00% | 0.00% |
| Good | 32 | 32 | 100.00% | 0.00% |
| Neutral | 1407 | 47 | 0.00% | 0.00% |
| Poor | 211 | 211 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 55 | 7 | {'Excellent': 6, 'Good': 0, 'Neutral': 1, 'Poor': 0, 'Unknown': 0, 'Pending': 48} |
| Mid Score (60-74) | 1475 | 377 | {'Excellent': 128, 'Good': 28, 'Neutral': 39, 'Poor': 182, 'Unknown': 0, 'Pending': 1098} |
| Low Score (<60) | 270 | 56 | {'Excellent': 16, 'Good': 4, 'Neutral': 7, 'Poor': 29, 'Unknown': 0, 'Pending': 214} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1265 | 298 | 39.26% | 50.67% | 30 |
| Medium | 535 | 142 | 45.77% | 42.25% | 17 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1090 | 211 | 37.91% | 52.13% | 21 |
| Moderate | 250 | 45 | 55.56% | 28.89% | 7 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 430 | 114 | 25.44% | 60.53% | 16 |
| Consumer Cyclical | 165 | 45 | 33.33% | 57.78% | 4 |
| Technology | 1205 | 281 | 49.11% | 41.28% | 27 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 1800 | 440 | {'Excellent': 150, 'Good': 32, 'Neutral': 47, 'Poor': 211, 'Unknown': 0, 'Pending': 1360} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 561 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 546 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 363 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 182 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 168 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 652 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 633 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 422 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 211 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 192 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
