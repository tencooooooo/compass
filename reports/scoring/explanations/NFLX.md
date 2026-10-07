# NFLX Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Netflix, Inc.
- Total Score: 41 / 100
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

- データが確認できた 80 点満点のうち 41 点を獲得し、シグナル充足率は 51.2% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

16点

理由

- revenue_growth(直近4四半期平均) は 15.65% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 5.23% で、プラス成長を維持しています。
- eps_growth は直近四半期が前四半期より -75.25pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 45,183,036,000.0000
- eps: 2.5800
- net_income: 10,981,201,000.0000
- operating_income: 13,326,603,000.0000
- research_and_development: 3,391,390,000.0000
- revenue_yoy_growth: 13.3700
- eps_yoy_growth: 11.1100
- revenue_yoy_growth_avg: 15.6500
- eps_yoy_growth_avg: 5.2300
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

16点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.09 倍で、負債負担は中程度です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.19 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 9,033,681,000.0000
- total_liabilities: 28,981,505,000.0000
- shareholders_equity: 26,615,488,000.0000
- long_term_debt: 13,463,971,000.0000
- current_ratio: 1.1857

## Valuation

6点

理由

- PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.6006
- forward_pe: 18.0381
- peg_ratio: 1.1500
- price_to_book: 9.4863
- sector_peer_count: 10
- trailing_pe_percentile: 77.7800
- trailing_pe_peer_count: 10
- forward_pe_percentile: 66.6700
- forward_pe_peer_count: 10
- peg_ratio_percentile: 44.4400
- peg_ratio_peer_count: 10
- price_to_book_percentile: 100
- price_to_book_peer_count: 10

## Momentum

3点

理由

- 1M の対SPY超過リターンは -13.62pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -13.91pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -49.27pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -58.12pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.06 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -12.2172
- 3M: -9.1282
- 6M: -30.4898
- 1Y: -40.4415
- benchmark: SPY
- benchmark_returns: {'1M': 1.41, '3M': 4.78, '6M': 18.78, '1Y': 17.68}
- excess_returns: {'1M': -13.62, '3M': -13.91, '6M': -49.27, '1Y': -58.12}
- latest_volume: 35,052,500.0000
- average_volume_30d: 33,155,463.3333

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
