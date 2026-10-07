# AMD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Advanced Micro Devices, Inc.
- Total Score: 65 / 100
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

- データが確認できた 80 点満点のうち 65 点を獲得し、シグナル充足率は 81.2% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 38.82% で、+30%以上の高成長です。
- eps_growth(直近4四半期平均) は 135.88% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +12.26pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +64.65pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 50.1100
- eps_yoy_growth: 155.5600
- revenue_yoy_growth_avg: 38.8200
- eps_yoy_growth_avg: 135.8800
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

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

6点

理由

- PER はセクター内 100.00 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 93.33 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PEG はセクター内 26.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 165.6684
- forward_pe: 41.3067
- peg_ratio: 0.6400
- price_to_book: 15.7661
- sector_peer_count: 16
- trailing_pe_percentile: 100
- trailing_pe_peer_count: 15
- forward_pe_percentile: 93.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 26.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 73.3300
- price_to_book_peer_count: 16

## Momentum

19点

理由

- 1M の対SPY超過リターンが +34.58pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +20.73pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +174.37pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +276.70pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 1.19 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 35.9842
- 3M: 25.5136
- 6M: 193.1522
- 1Y: 294.3766
- benchmark: SPY
- benchmark_returns: {'1M': 1.41, '3M': 4.78, '6M': 18.78, '1Y': 17.68}
- excess_returns: {'1M': 34.58, '3M': 20.73, '6M': 174.37, '1Y': 276.7}
- latest_volume: 24,200,600.0000
- average_volume_30d: 20,421,410.0000

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
