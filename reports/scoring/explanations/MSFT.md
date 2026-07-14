# MSFT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Microsoft Corporation
- Total Score: 69 / 100
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
- PER は 22.95 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 4 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 19.88 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 4 社のため、PEG は固定閾値で評価しています。
- PEG は 1.19 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、PBR は固定閾値で評価しています。
- PBR は 6.90 で、評価ルール上は過度な割高さが抑えられています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 22.9535
- forward_pe: 19.8828
- peg_ratio: 1.1900
- price_to_book: 6.9012
- sector_peer_count: 4

## Momentum

3点

理由

- 1M の対SPY超過リターンは -3.56pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -9.50pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -28.23pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -44.81pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.64 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -1.3860
- 3M: 0.3626
- 6M: -19.3281
- 1Y: -22.9109
- benchmark: SPY
- benchmark_returns: {'1M': 2.17, '3M': 9.86, '6M': 8.9, '1Y': 21.89}
- excess_returns: {'1M': -3.56, '3M': -9.5, '6M': -28.23, '1Y': -44.81}
- latest_volume: 27,741,653.0000
- average_volume_30d: 43,660,788.4333

## News

12点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が -1.55% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 3
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 6

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
