# AMD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Advanced Micro Devices, Inc.
- Total Score: 73 / 100
- Confidence: High
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 35.26% で、+30%以上の高成長です。
- eps_growth(直近4四半期平均) は 229.14% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +31.34pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 34,639,000,000.0000
- eps: 2.6700
- net_income: 4,335,000,000.0000
- operating_income: 3,694,000,000.0000
- research_and_development: 8,091,000,000.0000
- revenue_yoy_growth: 37.8500
- eps_yoy_growth: 90.9100
- revenue_yoy_growth_avg: 35.2600
- eps_yoy_growth_avg: 229.1400
- revenue_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.22 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.85 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 5,539,000,000.0000
- total_liabilities: 13,927,000,000.0000
- shareholders_equity: 62,999,000,000.0000
- long_term_debt: 2,348,000,000.0000
- current_ratio: 2.8500

## Valuation

9点

理由

- セクター比較対象が 4 社のため、PER は固定閾値で評価しています。
- PER は 164.70 で、バリュエーション面の加点は抑えています。
- セクター比較対象が 4 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 36.82 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、PEG は固定閾値で評価しています。
- PEG は 1.27 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、PBR は固定閾値で評価しています。
- PBR は 12.54 で、バリュエーション面は中立から注意寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 164.7043
- forward_pe: 36.8191
- peg_ratio: 1.2700
- price_to_book: 12.5360
- sector_peer_count: 4

## Momentum

13点

理由

- 1M の対SPY超過リターンは -1.59pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンが +71.96pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +113.48pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +189.30pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 1.00 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -2.2729
- 3M: 78.1643
- 6M: 121.7174
- 1Y: 209.6952
- benchmark: SPY
- benchmark_returns: {'1M': -0.68, '3M': 6.21, '6M': 8.24, '1Y': 20.39}
- excess_returns: {'1M': -1.59, '3M': 71.96, '6M': 113.48, '1Y': 189.3}
- latest_volume: 30,156,030.0000
- average_volume_30d: 30,070,027.6667

## News

11点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 6 件、悪材料 1 件(純比率 +0.71)で、センチメントは 6.8 点です。
- イベント後の平均株価反応が -1.03% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 6
- negative_count: 1
- sentiment_net_ratio: 0.7100
- event_count: 10
- events_with_price_reaction: 1

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
