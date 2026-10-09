# MSFT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Microsoft Corporation
- Total Score: 59 / 100
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

- データが確認できた 80 点満点のうち 59 点を獲得し、シグナル充足率は 73.8% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

18点

理由

- revenue_growth(直近4四半期平均) は 16.68% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 28.39% で、+15%以上の成長です。
- eps_growth は直近四半期が前四半期より -36.34pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 331,839,000,000.0000
- eps: 18.0000
- net_income: 133,749,000,000.0000
- operating_income: 155,237,000,000.0000
- research_and_development: 35,562,000,000.0000
- revenue_yoy_growth: 18.3000
- eps_yoy_growth: 23.4100
- revenue_yoy_growth_avg: 16.6800
- eps_yoy_growth_avg: 28.3900
- revenue_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']

## Financial Health

18点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.71 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.23 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 20,935,000,000.0000
- total_liabilities: 315,989,000,000.0000
- shareholders_equity: 442,387,000,000.0000
- long_term_debt: 31,067,000,000.0000
- current_ratio: 1.2303

## Valuation

9点

理由

- PER はセクター内 42.86 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 60.00 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 86.67 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PBR はセクター内 33.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 29.1148
- forward_pe: 22.0722
- peg_ratio: 1.7200
- price_to_book: 8.7738
- sector_peer_count: 16
- trailing_pe_percentile: 42.8600
- trailing_pe_peer_count: 15
- forward_pe_percentile: 60.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 86.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 33.3300
- price_to_book_peer_count: 16

## Momentum

14点

理由

- 1M の対SPY超過リターンは +4.53pt で、市場並み以上です。
- 3M の対SPY超過リターンが +33.19pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +26.25pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -16.35pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.92 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 6.2972
- 3M: 35.9631
- 6M: 40.6513
- 1Y: 0.5592
- benchmark: SPY
- benchmark_returns: {'1M': 1.76, '3M': 2.77, '6M': 14.4, '1Y': 16.91}
- excess_returns: {'1M': 4.53, '3M': 33.19, '6M': 26.25, '1Y': -16.35}
- latest_volume: 20,201,700.0000
- average_volume_30d: 21,847,233.3333

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
