# AMZN Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Amazon.com, Inc.
- Total Score: 54 / 100
- Confidence: Medium
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 4 領域です。
- 欠損または計算不可の項目数は 3 件です。
- データが不足している領域: News。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 80 点満点のうち 54 点を獲得し、シグナル充足率は 67.5% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

16点

理由

- revenue_growth(直近4四半期平均) は 15.43% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 87.59% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より -7.53pt 低く、成長の減速に注意が必要です。
- eps_growth は直近四半期が前四半期より -245.34pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 716,924,000,000.0000
- eps: 7.2900
- net_income: 77,670,000,000.0000
- operating_income: 79,975,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: 12.0900
- eps_yoy_growth: -3.0800
- revenue_yoy_growth_avg: 15.4300
- eps_yoy_growth_avg: 87.5900
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

欠損・計算不可

- research_and_development

## Financial Health

18点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.99 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.05 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 86,810,000,000.0000
- total_liabilities: 406,977,000,000.0000
- shareholders_equity: 411,065,000,000.0000
- long_term_debt: 65,648,000,000.0000
- current_ratio: 1.0508

## Valuation

14点

理由

- PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 25.00 パーセンタイル / 母数 5 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 19.3363
- forward_pe: 22.7667
- peg_ratio: 1.4100
- price_to_book: 6.2745
- sector_peer_count: 10
- trailing_pe_percentile: 33.3300
- trailing_pe_peer_count: 10
- forward_pe_percentile: 44.4400
- forward_pe_peer_count: 10
- peg_ratio_percentile: 33.3300
- peg_ratio_peer_count: 10
- price_to_book_percentile: 25.0000
- price_to_book_peer_count: 5

## Momentum

6点

理由

- 1M の対SPY超過リターンは -3.03pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -13.48pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -15.62pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -6.84pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 2.22 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -2.1513
- 3M: -10.2327
- 6M: -8.0246
- 1Y: 6.3424
- benchmark: SPY
- benchmark_returns: {'1M': 0.88, '3M': 3.24, '6M': 7.6, '1Y': 13.19}
- excess_returns: {'1M': -3.03, '3M': -13.48, '6M': -15.62, '1Y': -6.84}
- latest_volume: 85,234,400.0000
- average_volume_30d: 38,414,530.0000

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
