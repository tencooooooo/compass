# AMAT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Applied Materials, Inc.
- Total Score: 57 / 100
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

- データが確認できた 80 点満点のうち 57 点を獲得し、シグナル充足率は 71.2% です。
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

12点

理由

- PER はセクター内 64.29 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 60.00 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 60.00 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 33.6575
- forward_pe: 21.0239
- peg_ratio: 0.8900
- price_to_book: 12.0805
- sector_peer_count: 16
- trailing_pe_percentile: 64.2900
- trailing_pe_peer_count: 15
- forward_pe_percentile: 60.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 60.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 16

## Momentum

8点

理由

- 1M の対SPY超過リターンは -18.43pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -20.10pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -0.46pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンが +73.07pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.96 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -17.5447
- 3M: -16.8533
- 6M: 7.1347
- 1Y: 86.2556
- benchmark: SPY
- benchmark_returns: {'1M': 0.88, '3M': 3.24, '6M': 7.6, '1Y': 13.19}
- excess_returns: {'1M': -18.43, '3M': -20.1, '6M': -0.46, '1Y': 73.07}
- latest_volume: 6,701,600.0000
- average_volume_30d: 6,969,336.6667

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
