# NVDA Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: NVIDIA Corporation
- Total Score: 77 / 100
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

- revenue_growth(直近4四半期平均) は 68.12% で、+30%以上の高成長です。
- eps_growth(直近4四半期平均) は 92.25% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +22.74pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +147.80pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 215,938,000,000.0000
- eps: 4.9300
- net_income: 120,067,000,000.0000
- operating_income: 130,387,000,000.0000
- research_and_development: 18,497,000,000.0000
- revenue_yoy_growth: 85.2300
- eps_yoy_growth: 214.4700
- revenue_yoy_growth_avg: 68.1200
- eps_yoy_growth_avg: 92.2500
- revenue_growth_quarters: ['2026-Q2', '2025-Q4', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2025-Q4', '2025-Q3', '2025-Q2']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.31 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 3.91 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 10,605,000,000.0000
- total_liabilities: 49,510,000,000.0000
- shareholders_equity: 157,293,000,000.0000
- long_term_debt: 7,469,000,000.0000
- current_ratio: 3.9053

## Valuation

14点

理由

- セクター比較対象が 4 社のため、PER は固定閾値で評価しています。
- PER は 32.59 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 16.60 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 4 社のため、PEG は固定閾値で評価しています。
- PEG は 0.65 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 4 社のため、PBR は固定閾値で評価しています。
- PBR は 26.33 で、バリュエーション面は中立から注意寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 32.5920
- forward_pe: 16.5952
- peg_ratio: 0.6500
- price_to_book: 26.3321
- sector_peer_count: 4

## Momentum

8点

理由

- 1M の対SPY超過リターンは +1.54pt で、市場並み以上です。
- 3M の対SPY超過リターンは -0.71pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは +5.88pt で、市場並み以上です。
- 1Y の対SPY超過リターンは +7.55pt で、市場並み以上です。
- 直近出来高が30日平均の 0.79 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 3.5626
- 3M: 8.2630
- 6M: 15.0423
- 1Y: 29.6904
- benchmark: SPY
- benchmark_returns: {'1M': 2.02, '3M': 8.97, '6M': 9.16, '1Y': 22.14}
- excess_returns: {'1M': 1.54, '3M': -0.71, '6M': 5.88, '1Y': 7.55}
- latest_volume: 118,979,465.0000
- average_volume_30d: 150,849,102.1667

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 6 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が 0.33% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 6
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 2

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
