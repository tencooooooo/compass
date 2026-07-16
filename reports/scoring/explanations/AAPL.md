# AAPL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Apple Inc.
- Total Score: 65 / 100
- Confidence: High
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 11.74% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 15.03% で、+15%以上の成長です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 416,161,000,000.0000
- eps: 7.4900
- net_income: 112,010,000,000.0000
- operating_income: 133,050,000,000.0000
- research_and_development: 34,550,000,000.0000
- revenue_yoy_growth: 16.6000
- eps_yoy_growth: 21.8200
- revenue_yoy_growth_avg: 11.7400
- eps_yoy_growth_avg: 15.0300
- revenue_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q2', '2025-Q1']

## Financial Health

12点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 3.87 倍で、負債負担の確認が必要です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 0.89 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 35,934,000,000.0000
- total_liabilities: 285,508,000,000.0000
- shareholders_equity: 73,733,000,000.0000
- long_term_debt: 78,328,000,000.0000
- current_ratio: 0.8933

## Valuation

6点

理由

- セクター比較対象が 4 社のため、PER は固定閾値で評価しています。
- PER は 40.40 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 34.64 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、PEG は固定閾値で評価しています。
- PEG は 2.54 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 4 社のため、PBR は固定閾値で評価しています。
- PBR は 45.90 で、バリュエーション面は中立から注意寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 40.3952
- forward_pe: 34.6391
- peg_ratio: 2.5400
- price_to_book: 45.9036
- sector_peer_count: 4

## Momentum

15点

理由

- 1M の対SPY超過リターンが +12.72pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +17.67pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +19.11pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +38.00pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 1.01 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 12.4283
- 3M: 25.1988
- 6M: 27.8986
- 1Y: 60.0029
- benchmark: SPY
- benchmark_returns: {'1M': -0.29, '3M': 7.53, '6M': 8.78, '1Y': 22.0}
- excess_returns: {'1M': 12.72, '3M': 17.67, '6M': 19.11, '1Y': 38.0}
- latest_volume: 62,673,782.0000
- average_volume_30d: 61,872,959.4000

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 1 件(純比率 +0.60)で、センチメントは 6.4 点です。
- イベント後の平均株価反応が 1.76% とプラスです。

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
- events_with_price_reaction: 6

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
