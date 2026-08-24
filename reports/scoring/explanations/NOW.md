# NOW Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: ServiceNow, Inc.
- Total Score: 65 / 100
- Confidence: High
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 100 点満点のうち 65 点を獲得し、シグナル充足率は 65.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

14点

理由

- revenue_growth(直近4四半期平均) は 22.57% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は -18.51% で、前年同期比ではマイナスです。
- eps_growth は直近四半期が前四半期より -23.89pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 13,278,000,000.0000
- eps: 1.6900
- net_income: 1,748,000,000.0000
- operating_income: 1,824,000,000.0000
- research_and_development: 2,960,000,000.0000
- revenue_yoy_growth: 24.0100
- eps_yoy_growth: -21.6200
- revenue_yoy_growth_avg: 22.5700
- eps_yoy_growth_avg: -18.5100
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

16点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.01 倍で、負債負担は中程度です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.00 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 3,726,000,000.0000
- total_liabilities: 13,074,000,000.0000
- shareholders_equity: 12,964,000,000.0000
- long_term_debt: 1,491,000,000.0000
- current_ratio: 1.0027

## Valuation

9点

理由

- PER はセクター内 92.86 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 79.5342
- forward_pe: 25.5818
- peg_ratio: 1.1500
- price_to_book: 10.5774
- sector_peer_count: 16
- trailing_pe_percentile: 92.8600
- trailing_pe_peer_count: 15
- forward_pe_percentile: 73.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 53.3300
- price_to_book_peer_count: 16

## Momentum

13点

理由

- 1M の対SPY超過リターンが +26.31pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +22.72pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +14.56pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -48.45pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.40 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 29.6315
- 3M: 25.3794
- 6M: 27.0337
- 1Y: -26.9929
- benchmark: SPY
- benchmark_returns: {'1M': 3.32, '3M': 2.66, '6M': 12.48, '1Y': 21.46}
- excess_returns: {'1M': 26.31, '3M': 22.72, '6M': 14.56, '1Y': -48.45}
- latest_volume: 8,930,312.0000
- average_volume_30d: 22,492,497.0667

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 1 件(純比率 +0.60)で、センチメントは 6.4 点です。
- イベント後の平均株価反応が -0.72% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 1
- sentiment_net_ratio: 0.6000
- event_count: 10
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
