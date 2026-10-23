# NFLX Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Netflix, Inc.
- Total Score: 44 / 100
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

- データが確認できた 80 点満点のうち 44 点を獲得し、シグナル充足率は 55.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

14点

理由

- revenue_growth(直近4四半期平均) は 14.64% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 13.97% で、プラス成長を維持しています。
- eps_growth は直近四半期が前四半期より +36.35pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 11.8500
- eps_yoy_growth: 47.4600
- revenue_yoy_growth_avg: 14.6400
- eps_yoy_growth_avg: 13.9700
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

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

9点

理由

- PER はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 19.3786
- forward_pe: 17.7800
- peg_ratio: 1.0600
- price_to_book: 9.4663
- sector_peer_count: 10
- trailing_pe_percentile: 66.6700
- trailing_pe_peer_count: 10
- forward_pe_percentile: 66.6700
- forward_pe_peer_count: 10
- peg_ratio_percentile: 44.4400
- peg_ratio_peer_count: 10
- price_to_book_percentile: 100
- price_to_book_peer_count: 10

## Momentum

5点

理由

- 1M の対SPY超過リターンは -9.83pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -10.58pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -39.50pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -63.89pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 2.59 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -9.8670
- 3M: -5.5886
- 6M: -30.2445
- 1Y: -47.4874
- benchmark: SPY
- benchmark_returns: {'1M': -0.04, '3M': 4.99, '6M': 9.25, '1Y': 16.41}
- excess_returns: {'1M': -9.83, '3M': -10.58, '6M': -39.5, '1Y': -63.89}
- latest_volume: 101,393,300.0000
- average_volume_30d: 39,194,896.6667

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
