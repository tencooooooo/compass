# GOOGL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Alphabet Inc.
- Total Score: 75 / 100
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

- revenue_growth(直近4四半期平均) は 15.89% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 47.03% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +5.84pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +46.47pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 402,836,000,000.0000
- eps: 10.9100
- net_income: 132,170,000,000.0000
- operating_income: 129,039,000,000.0000
- research_and_development: 61,087,000,000.0000
- revenue_yoy_growth: 21.7900
- eps_yoy_growth: 81.8500
- revenue_yoy_growth_avg: 15.8900
- eps_yoy_growth_avg: 47.0300
- revenue_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.43 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.01 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 30,708,000,000.0000
- total_liabilities: 180,016,000,000.0000
- shareholders_equity: 415,265,000,000.0000
- long_term_debt: 46,547,000,000.0000
- current_ratio: 2.0053

## Valuation

14点

理由

- セクター比較対象が 2 社のため、PER は固定閾値で評価しています。
- PER は 26.43 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 2 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 23.69 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 2 社のため、PEG は固定閾値で評価しています。
- PEG は 1.42 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 2 社のため、PBR は固定閾値で評価しています。
- PBR は 8.78 で、バリュエーション面は中立から注意寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 26.4306
- forward_pe: 23.6912
- peg_ratio: 1.4200
- price_to_book: 8.7759
- sector_peer_count: 2

## Momentum

9点

理由

- 1M の対SPY超過リターンは -6.41pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -2.95pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -4.85pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンが +69.67pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.88 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -7.0944
- 3M: 3.2609
- 6M: 3.3889
- 1Y: 90.0635
- benchmark: SPY
- benchmark_returns: {'1M': -0.68, '3M': 6.21, '6M': 8.24, '1Y': 20.39}
- excess_returns: {'1M': -6.41, '3M': -2.95, '6M': -4.85, '1Y': 69.67}
- latest_volume: 29,853,865.0000
- average_volume_30d: 33,859,692.1667

## News

12点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が -2.17% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 5
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 1

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
