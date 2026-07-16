# META Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Meta Platforms, Inc.
- Total Score: 74 / 100
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

- revenue_growth(直近4四半期平均) は 24.25% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 13.66% で、プラス成長を維持しています。
- revenue_growth は直近四半期が前四半期より +6.83pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +144.95pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 200,966,000,000.0000
- eps: 23.9800
- net_income: 60,458,000,000.0000
- operating_income: 83,276,000,000.0000
- research_and_development: 57,372,000,000.0000
- revenue_yoy_growth: 33.0800
- eps_yoy_growth: 62.3600
- revenue_yoy_growth_avg: 24.2500
- eps_yoy_growth_avg: 13.6600
- revenue_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.68 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.60 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 35,873,000,000.0000
- total_liabilities: 148,778,000,000.0000
- shareholders_equity: 217,243,000,000.0000
- long_term_debt: 58,744,000,000.0000
- current_ratio: 2.5988

## Valuation

20点

理由

- セクター比較対象が 2 社のため、PER は固定閾値で評価しています。
- PER は 24.15 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 2 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 18.29 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 2 社のため、PEG は固定閾値で評価しています。
- PEG は 0.96 で、評価ルール上は過度な割高さが抑えられています。
- セクター比較対象が 2 社のため、PBR は固定閾値で評価しています。
- PBR は 6.92 で、評価ルール上は過度な割高さが抑えられています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 24.1475
- forward_pe: 18.2923
- peg_ratio: 0.9600
- price_to_book: 6.9214
- sector_peer_count: 2

## Momentum

6点

理由

- 1M の対SPY超過リターンが +12.26pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -8.49pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -3.30pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -28.15pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.78 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 11.9734
- 3M: -0.9566
- 6M: 5.4882
- 1Y: -6.1476
- benchmark: SPY
- benchmark_returns: {'1M': -0.29, '3M': 7.53, '6M': 8.78, '1Y': 22.0}
- excess_returns: {'1M': 12.26, '3M': -8.49, '6M': -3.3, '1Y': -28.15}
- latest_volume: 15,736,700.0000
- average_volume_30d: 20,180,736.6667

## News

11点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 1 件(純比率 +0.67)で、センチメントは 6.7 点です。
- イベント後の平均株価反応が -2.46% と弱く、注意が必要です。

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
- events_with_price_reaction: 5

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
