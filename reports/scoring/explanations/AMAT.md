# AMAT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Applied Materials, Inc.
- Total Score: 53 / 100
- Confidence: Medium
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 4 領域です。
- 欠損または計算不可の項目数は 2 件です。
- データが不足している領域: News。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 80 点満点のうち 53 点を獲得し、シグナル充足率は 66.2% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 10.45% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 39.93% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +13.42pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +9.33pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 28,368,000,000.0000
- eps: 8.7100
- net_income: 6,998,000,000.0000
- operating_income: 8,470,000,000.0000
- research_and_development: 3,570,000,000.0000
- revenue_yoy_growth: 24.8300
- eps_yoy_growth: 42.7900
- revenue_yoy_growth_avg: 10.4500
- eps_yoy_growth_avg: 39.9300
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.78 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.61 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 7,241,000,000.0000
- total_liabilities: 15,884,000,000.0000
- shareholders_equity: 20,415,000,000.0000
- long_term_debt: 6,455,000,000.0000
- current_ratio: 2.6105

## Valuation

3点

理由

- PER はセクター内 78.57 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 80.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PEG はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 80.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 46.8023
- forward_pe: 28.7163
- peg_ratio: 1.0800
- price_to_book: 16.4216
- sector_peer_count: 16
- trailing_pe_percentile: 78.5700
- trailing_pe_peer_count: 15
- forward_pe_percentile: 80.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 73.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 80.0000
- price_to_book_peer_count: 16

## Momentum

13点

理由

- 1M の対SPY超過リターンが +15.21pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -11.73pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンが +31.23pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +127.44pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.79 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 16.6172
- 3M: -6.9523
- 6M: 50.0090
- 1Y: 145.1170
- benchmark: SPY
- benchmark_returns: {'1M': 1.41, '3M': 4.78, '6M': 18.78, '1Y': 17.68}
- excess_returns: {'1M': 15.21, '3M': -11.73, '6M': 31.23, '1Y': 127.44}
- latest_volume: 4,876,100.0000
- average_volume_30d: 6,176,450.0000

## News

0点

理由

- ニュースが取得できないため、News項目は評価を控えています。
- イベントDBが取得できないため、イベント項目は加点していません。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 0
- positive_count: 0
- negative_count: 0
- sentiment_net_ratio: N/A
- event_count: 0
- events_with_price_reaction: 0

欠損・計算不可

- news
- events

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
