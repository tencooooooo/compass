# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-17T19:50:11.604293-04:00
- Validation件数: 2575
- 完了済みValidation: 677
- 未完了Validation: 1898
- 成功率: 43.13%
- 失敗率: 43.87%
- Result Counts(期間完了分): {'Excellent': 241, 'Poor': 297, 'Neutral': 88, 'Good': 51}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 241 | 241 | 100.00% | 0.00% |
| Good | 51 | 51 | 100.00% | 0.00% |
| Neutral | 1986 | 88 | 0.00% | 0.00% |
| Poor | 297 | 297 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 890 | 255 | {'Excellent': 119, 'Good': 18, 'Neutral': 25, 'Poor': 93, 'Unknown': 0, 'Pending': 635} |
| Mid Score (60-74) | 1510 | 387 | {'Excellent': 115, 'Good': 33, 'Neutral': 59, 'Poor': 180, 'Unknown': 0, 'Pending': 1123} |
| Low Score (<60) | 175 | 35 | {'Excellent': 7, 'Good': 0, 'Neutral': 4, 'Poor': 24, 'Unknown': 0, 'Pending': 140} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1820 | 465 | 45.16% | 42.80% | 56 |
| Medium | 755 | 212 | 38.68% | 46.23% | 32 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1710 | 403 | 41.94% | 44.17% | 56 |
| Moderate | 405 | 90 | 51.11% | 34.44% | 13 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 570 | 163 | 32.52% | 52.76% | 24 |
| Consumer Cyclical | 200 | 64 | 23.44% | 67.19% | 6 |
| Technology | 1805 | 450 | 49.78% | 37.33% | 58 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2575 | 677 | {'Excellent': 241, 'Good': 51, 'Neutral': 88, 'Poor': 297, 'Unknown': 0, 'Pending': 1898} |
| No Events | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Success Patterns

- Momentum: 893 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 876 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 581 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 292 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 278 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 932 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 891 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 592 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 297 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 258 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
