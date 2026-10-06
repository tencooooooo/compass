# TXN Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Texas Instruments Incorporated
- Total Score: 60 / 100
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

- データが確認できた 80 点満点のうち 60 点を獲得し、シグナル充足率は 75.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 18.00% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 24.82% で、+15%以上の成長です。
- eps_growth は直近四半期が前四半期より +20.52pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 17,682,000,000.0000
- eps: 5.5016
- net_income: 5,001,000,000.0000
- operating_income: 6,140,000,000.0000
- research_and_development: 2,083,000,000.0000
- revenue_yoy_growth: 22.8200
- eps_yoy_growth: 51.7700
- revenue_yoy_growth_avg: 18.0000
- eps_yoy_growth_avg: 24.8200
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

17点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.13 倍で、負債負担は中程度です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 4.35 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 3,225,000,000.0000
- total_liabilities: 18,312,000,000.0000
- shareholders_equity: 16,273,000,000.0000
- long_term_debt: 13,548,000,000.0000
- current_ratio: 4.3526

## Valuation

12点

理由

- PER はセクター内 71.43 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 44.8858
- forward_pe: 27.7035
- peg_ratio: 1.0500
- price_to_book: 14.9521
- sector_peer_count: 16
- trailing_pe_percentile: 71.4300
- trailing_pe_peer_count: 15
- forward_pe_percentile: 73.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 16

## Momentum

14点

理由

- 1M の対SPY超過リターンが +15.72pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -2.82pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンが +31.21pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +48.91pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.67 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 16.1801
- 3M: 1.0603
- 6M: 49.3912
- 1Y: 65.9374
- benchmark: SPY
- benchmark_returns: {'1M': 0.46, '3M': 3.88, '6M': 18.18, '1Y': 17.03}
- excess_returns: {'1M': 15.72, '3M': -2.82, '6M': 31.21, '1Y': 48.91}
- latest_volume: 3,778,300.0000
- average_volume_30d: 5,610,110.0000

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
