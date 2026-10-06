# ADBE Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Adobe Inc.
- Total Score: 50 / 100
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

- データが確認できた 80 点満点のうち 50 点を獲得し、シグナル充足率は 62.5% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

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

- trailing_pe: 13.3325
- forward_pe: 8.6287
- peg_ratio: 0.5700
- price_to_book: 7.9365
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

4点

理由

- 1M の対SPY超過リターンは -16.90pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは +3.90pt で、市場並み以上です。
- 6M の対SPY超過リターンは -20.46pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -49.09pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.64 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -16.4339
- 3M: 7.7864
- 6M: -2.2794
- 1Y: -32.0616
- benchmark: SPY
- benchmark_returns: {'1M': 0.46, '3M': 3.88, '6M': 18.18, '1Y': 17.03}
- excess_returns: {'1M': -16.9, '3M': 3.9, '6M': -20.46, '1Y': -49.09}
- latest_volume: 3,292,400.0000
- average_volume_30d: 5,121,240.0000

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
