# ORCL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Oracle Corporation
- Total Score: 51 / 100
- Confidence: Medium
- Signal Strength: Moderate
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

Moderate

理由

- データが確認できた 80 点満点のうち 51 点を獲得し、シグナル充足率は 63.8% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

19点

理由

- revenue_growth(直近4四半期平均) は 19.41% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 41.98% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +7.95pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +29.95pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 67,357,000,000.0000
- eps: 5.9400
- net_income: 17,087,000,000.0000
- operating_income: 22,444,000,000.0000
- research_and_development: 10,272,000,000.0000
- revenue_yoy_growth: 29.6100
- eps_yoy_growth: 54.4600
- revenue_yoy_growth_avg: 19.4100
- eps_yoy_growth_avg: 41.9800
- revenue_growth_quarters: ['2026-Q3', '2026-Q1', '2025-Q4', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q1', '2025-Q4', '2025-Q3']

## Financial Health

13点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 5.14 倍で、負債負担の確認が必要です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 1.12 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 31,289,000,000.0000
- total_liabilities: 218,703,000,000.0000
- shareholders_equity: 42,508,000,000.0000
- long_term_debt: 122,342,000,000.0000
- current_ratio: 1.1150

## Valuation

14点

理由

- PER はセクター内 35.71 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 13.33 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PEG はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.2680
- forward_pe: 12.3366
- peg_ratio: 0.8100
- price_to_book: 10.4057
- sector_peer_count: 16
- trailing_pe_percentile: 35.7100
- trailing_pe_peer_count: 15
- forward_pe_percentile: 13.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 46.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 46.6700
- price_to_book_peer_count: 16

## Momentum

5点

理由

- 1M の対SPY超過リターンは -17.81pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -6.29pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -15.64pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -68.63pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.32 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -16.0490
- 3M: -3.5196
- 6M: -1.2316
- 1Y: -51.7181
- benchmark: SPY
- benchmark_returns: {'1M': 1.76, '3M': 2.77, '6M': 14.4, '1Y': 16.91}
- excess_returns: {'1M': -17.81, '3M': -6.29, '6M': -15.64, '1Y': -68.63}
- latest_volume: 42,225,400.0000
- average_volume_30d: 31,945,563.3333

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
