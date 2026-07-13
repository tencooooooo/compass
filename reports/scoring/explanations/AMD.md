# AMD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Advanced Micro Devices, Inc.
- Total Score: 72 / 100
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

7点

理由

- セクター比較対象が 4 社のため、PER は固定閾値で評価しています。
- PER は 177.54 で、バリュエーション面の加点は抑えています。
- セクター比較対象が 4 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 40.24 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、PEG は固定閾値で評価しています。
- PEG は 1.34 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、PBR は固定閾値で評価しています。
- PBR は 13.51 で、バリュエーション面は中立から注意寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 177.5382
- forward_pe: 40.2358
- peg_ratio: 1.3400
- price_to_book: 13.5128
- sector_peer_count: 4

## Momentum

13点

理由

- 1M の対SPY超過リターンが +14.58pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +107.54pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +151.86pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +249.66pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.74 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 18.1233
- 3M: 118.0828
- 6M: 161.0856
- 1Y: 270.6923
- benchmark: SPY
- benchmark_returns: {'1M': 3.54, '3M': 10.54, '6M': 9.23, '1Y': 21.04}
- excess_returns: {'1M': 14.58, '3M': 107.54, '6M': 151.86, '1Y': 249.66}
- latest_volume: 22,515,725.0000
- average_volume_30d: 30,439,950.8333

## News

12点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 7 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が -4.21% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 7
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 5

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
