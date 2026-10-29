# META Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Meta Platforms, Inc.
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

20点

理由

- revenue_growth(直近4四半期平均) は 28.34% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 57.77% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +278.21pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 26.0700
- eps_yoy_growth: 264.7600
- revenue_yoy_growth_avg: 28.3400
- eps_yoy_growth_avg: 57.7700
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

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

6点

理由

- PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 20.8970
- forward_pe: 17.4250
- peg_ratio: 0.8100
- price_to_book: 5.7475
- sector_peer_count: 10
- trailing_pe_percentile: 77.7800
- trailing_pe_peer_count: 10
- forward_pe_percentile: 77.7800
- forward_pe_peer_count: 10
- peg_ratio_percentile: 33.3300
- peg_ratio_peer_count: 10
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 10

## Momentum

7点

理由

- 1M の対SPY超過リターンは -13.86pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは +0.22pt で、市場並み以上です。
- 6M の対SPY超過リターンは -16.15pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -30.59pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 2.21 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -13.3353
- 3M: 5.9885
- 6M: -7.4605
- 1Y: -15.7195
- benchmark: SPY
- benchmark_returns: {'1M': 0.53, '3M': 5.77, '6M': 8.69, '1Y': 14.87}
- excess_returns: {'1M': -13.86, '3M': 0.22, '6M': -16.15, '1Y': -30.59}
- latest_volume: 51,334,100.0000
- average_volume_30d: 23,213,476.6667

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
