# MSFT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Microsoft Corporation
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

18点

理由

- revenue_growth(直近4四半期平均) は 16.68% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 28.39% で、+15%以上の成長です。
- eps_growth は直近四半期が前四半期より -36.34pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 281,724,000,000.0000
- eps: 13.7000
- net_income: 101,832,000,000.0000
- operating_income: 128,528,000,000.0000
- research_and_development: 32,488,000,000.0000
- revenue_yoy_growth: 18.3000
- eps_yoy_growth: 23.4100
- revenue_yoy_growth_avg: 16.6800
- eps_yoy_growth_avg: 28.3900
- revenue_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']

## Financial Health

18点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.80 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.35 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 30,242,000,000.0000
- total_liabilities: 275,524,000,000.0000
- shareholders_equity: 343,479,000,000.0000
- long_term_debt: 40,152,000,000.0000
- current_ratio: 1.3534

## Valuation

18点

理由

- セクター比較対象が 4 社のため、PER は固定閾値で評価しています。
- PER は 23.58 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 4 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 20.43 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 4 社のため、PEG は固定閾値で評価しています。
- PEG は 1.19 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、PBR は固定閾値で評価しています。
- PBR は 7.09 で、評価ルール上は過度な割高さが抑えられています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 23.5775
- forward_pe: 20.4264
- peg_ratio: 1.1900
- price_to_book: 7.0931
- sector_peer_count: 4

## Momentum

3点

理由

- 1M の対SPY超過リターンは -0.77pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -8.11pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -25.88pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -42.87pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.76 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 1.2515
- 3M: 0.8590
- 6M: -16.7208
- 1Y: -20.7208
- benchmark: SPY
- benchmark_returns: {'1M': 2.02, '3M': 8.97, '6M': 9.16, '1Y': 22.14}
- excess_returns: {'1M': -0.77, '3M': -8.11, '6M': -25.88, '1Y': -42.87}
- latest_volume: 32,663,427.0000
- average_volume_30d: 42,966,014.2333

## News

16点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 1 件(純比率 +0.67)で、センチメントは 6.7 点です。
- イベント後の平均株価反応が 2.78% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 5
- negative_count: 1
- sentiment_net_ratio: 0.6700
- event_count: 10
- events_with_price_reaction: 3

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
