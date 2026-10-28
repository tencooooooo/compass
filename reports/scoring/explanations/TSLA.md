# TSLA Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Tesla, Inc.
- Total Score: 47 / 100
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

- データが確認できた 80 点満点のうち 47 点を獲得し、シグナル充足率は 58.8% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

12点

理由

- revenue_growth(直近4四半期平均) は 13.17% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は -18.85% で、前年同期比ではマイナスです。
- revenue_growth は直近四半期が前四半期より -25.69pt 低く、成長の減速に注意が必要です。
- eps_growth は直近四半期が前四半期より -40.56pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 94,827,000,000.0000
- eps: 1.1800
- net_income: 3,794,000,000.0000
- operating_income: 4,849,000,000.0000
- research_and_development: 6,411,000,000.0000
- revenue_yoy_growth: -0.1700
- eps_yoy_growth: -43.5900
- revenue_yoy_growth_avg: 13.1700
- eps_yoy_growth_avg: -18.8500
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.67 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.16 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 16,513,000,000.0000
- total_liabilities: 54,941,000,000.0000
- shareholders_equity: 82,137,000,000.0000
- long_term_debt: 6,584,000,000.0000
- current_ratio: 2.1644

## Valuation

3点

理由

- PER はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR はセクター内 75.00 パーセンタイル / 母数 5 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 447.7582
- forward_pe: 189.0494
- peg_ratio: 4.5700
- price_to_book: 18.0388
- sector_peer_count: 10
- trailing_pe_percentile: 100
- trailing_pe_peer_count: 10
- forward_pe_percentile: 100
- forward_pe_peer_count: 10
- peg_ratio_percentile: 100
- peg_ratio_peer_count: 10
- price_to_book_percentile: 75.0000
- price_to_book_peer_count: 5

## Momentum

12点

理由

- 1M の対SPY超過リターンは +6.02pt で、市場並み以上です。
- 3M の対SPY超過リターンが +23.82pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンは -4.14pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -27.94pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.45 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 5.2431
- 3M: 27.3809
- 6M: 3.4199
- 1Y: -12.7756
- benchmark: SPY
- benchmark_returns: {'1M': -0.78, '3M': 3.56, '6M': 7.56, '1Y': 15.16}
- excess_returns: {'1M': 6.02, '3M': 23.82, '6M': -4.14, '1Y': -27.94}
- latest_volume: 53,090,200.0000
- average_volume_30d: 36,735,870.0000

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
