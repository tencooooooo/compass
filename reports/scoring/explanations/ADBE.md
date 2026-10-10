# ADBE Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Adobe Inc.
- Total Score: 54 / 100
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

- データが確認できた 80 点満点のうち 54 点を獲得し、シグナル充足率は 67.5% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

14点

理由

- revenue_growth(直近4四半期平均) は 12.07% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 10.17% で、プラス成長を維持しています。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 23,769,000,000.0000
- eps: 16.7300
- net_income: 7,130,000,000.0000
- operating_income: 8,706,000,000.0000
- research_and_development: 4,294,000,000.0000
- revenue_yoy_growth: 12.8900
- eps_yoy_growth: 10.5300
- revenue_yoy_growth_avg: 12.0700
- eps_yoy_growth_avg: 10.1700
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

## Financial Health

14点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.54 倍で、負債負担は中程度です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.00 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 5,431,000,000.0000
- total_liabilities: 17,873,000,000.0000
- shareholders_equity: 11,623,000,000.0000
- long_term_debt: 6,210,000,000.0000
- current_ratio: 0.9964

## Valuation

18点

理由

- PER はセクター内 0.00 パーセンタイル / 母数 15 で、相対的に割安寄りです。
- Forward PER はセクター内 6.67 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PEG はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PBR はセクター内 33.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 13.4594
- forward_pe: 8.7547
- peg_ratio: 0.5800
- price_to_book: 8.0523
- sector_peer_count: 16
- trailing_pe_percentile: 0
- trailing_pe_peer_count: 15
- forward_pe_percentile: 6.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 20.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 33.3300
- price_to_book_peer_count: 16

## Momentum

8点

理由

- 1M の対SPY超過リターンは -7.18pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは +5.02pt で、市場並み以上です。
- 6M の対SPY超過リターンは -9.57pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -47.71pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.10 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -5.4187
- 3M: 7.7848
- 6M: 4.8317
- 1Y: -30.7944
- benchmark: SPY
- benchmark_returns: {'1M': 1.76, '3M': 2.77, '6M': 14.4, '1Y': 16.91}
- excess_returns: {'1M': -7.18, '3M': 5.02, '6M': -9.57, '1Y': -47.71}
- latest_volume: 5,802,200.0000
- average_volume_30d: 5,276,280.0000

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
