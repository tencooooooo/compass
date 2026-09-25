# Feedback Summary

> このレポートはKnowledgeを自動更新しません。Validation結果から改善候補を人間へ提示するためのFeedbackです。

## Overview

- 生成日時: 2026-09-24T20:11:58.494187-04:00
- Validation件数: 2890
- 完了済みValidation: 784
- 未完了Validation: 2106
- 成功率: 45.03%
- 失敗率: 42.35%
- Result Counts(期間完了分): {'Excellent': 287, 'Poor': 332, 'Neutral': 99, 'Good': 66}

## Discovery Accuracy

| Result | Total | Completed | Success Rate | Failure Rate |
| --- | --- | --- | --- | --- |
| Excellent | 287 | 287 | 100.00% | 0.00% |
| Good | 66 | 66 | 100.00% | 0.00% |
| Neutral | 2205 | 99 | 0.00% | 0.00% |
| Poor | 332 | 332 | 0.00% | 100.00% |

## Score Accuracy

| Score Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| High Score (75+) | 310 | 96 | {'Excellent': 38, 'Good': 6, 'Neutral': 7, 'Poor': 45, 'Unknown': 0, 'Pending': 214} |
| Mid Score (60-74) | 2380 | 641 | {'Excellent': 237, 'Good': 60, 'Neutral': 88, 'Poor': 256, 'Unknown': 0, 'Pending': 1739} |
| Low Score (<60) | 200 | 47 | {'Excellent': 12, 'Good': 0, 'Neutral': 4, 'Poor': 31, 'Unknown': 0, 'Pending': 153} |
| Unknown | 0 | 0 | {'Excellent': 0, 'Good': 0, 'Neutral': 0, 'Poor': 0, 'Unknown': 0, 'Pending': 0} |

## Confidence Accuracy

| Confidence | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| High | 1975 | 544 | 47.06% | 40.81% | 66 |
| Medium | 915 | 240 | 40.42% | 45.83% | 33 |

## Signal Strength Accuracy

Confidence(データ充足度)と分離したシグナル強度別の成績です。分離導入前の検証行はUnknownに集計されます。

| Signal Strength | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Strong | 1980 | 487 | 44.97% | 41.89% | 64 |
| Moderate | 450 | 113 | 50.44% | 35.40% | 16 |
| Unknown | 460 | 184 | 41.85% | 47.83% | 19 |

## Sector Accuracy

| Sector | Total | Completed | Success Rate | Failure Rate | Neutral |
| --- | --- | --- | --- | --- | --- |
| Communication Services | 620 | 182 | 35.71% | 51.10% | 24 |
| Consumer Cyclical | 215 | 69 | 21.74% | 68.12% | 7 |
| Technology | 2055 | 533 | 51.22% | 36.02% | 68 |

## Event Accuracy

| Event Bucket | Total | Completed | Result Counts |
| --- | --- | --- | --- |
| Has Events | 2750 | 756 | {'Excellent': 272, 'Good': 65, 'Neutral': 97, 'Poor': 322, 'Unknown': 0, 'Pending': 1994} |
| No Events | 140 | 28 | {'Excellent': 15, 'Good': 1, 'Neutral': 2, 'Poor': 10, 'Unknown': 0, 'Pending': 112} |

## Success Patterns

- Momentum: 1076 件 / 例: 1Mモメンタムは -3.89% と弱めですが、大きな崩れではありません。
- Growth: 1059 件 / 例: Scoring EngineのGrowthが 20/20 で、成長性の基礎条件が確認できます。
- Financial Health: 703 件 / 例: Financial Healthが 12/20 で、継続調査に必要な財務基盤を評価しています。
- News: 353 件 / 例: Newsスコアが 16/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 339 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Failure Patterns

- Momentum: 1046 件 / 例: 1Mモメンタムが 6.03% とプラス圏です。
- Growth: 996 件 / 例: Scoring EngineのGrowthが 18/20 で、成長性の基礎条件が確認できます。
- Financial Health: 661 件 / 例: Financial Healthが 20/20 で、継続調査に必要な財務基盤を評価しています。
- News: 332 件 / 例: Newsスコアが 12/20 で、材料の量と市場関心を候補評価に反映しています。
- R&D: 285 件 / 例: 研究開発費が確認でき、将来成長への投資シグナルがあります。

## Notes

Feedback EngineはLearning Engineではありません。改善候補を生成し、Knowledge更新は人間のレビュー後に行います。
