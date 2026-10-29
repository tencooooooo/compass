# TXN Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Texas Instruments Incorporated
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

19点

理由

- revenue_growth(直近4四半期平均) は 20.83% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 40.18% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +25.26pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 27.6900
- eps_yoy_growth: 77.0300
- revenue_yoy_growth_avg: 20.8300
- eps_yoy_growth_avg: 40.1800
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

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

6点

理由

- PER はセクター内 78.57 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 60.00 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 80.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 40.0815
- forward_pe: 26.8890
- peg_ratio: 0.9400
- price_to_book: 14.7608
- sector_peer_count: 16
- trailing_pe_percentile: 78.5700
- trailing_pe_peer_count: 15
- forward_pe_percentile: 73.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 60.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 80.0000
- price_to_book_peer_count: 16

## Momentum

17点

理由

- 1M の対SPY超過リターンが +10.47pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは +8.67pt で、市場並み以上です。
- 6M の対SPY超過リターンは +9.07pt で、市場並み以上です。
- 1Y の対SPY超過リターンが +72.51pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 1.23 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 10.9949
- 3M: 14.4459
- 6M: 17.7620
- 1Y: 87.3765
- benchmark: SPY
- benchmark_returns: {'1M': 0.53, '3M': 5.77, '6M': 8.69, '1Y': 14.87}
- excess_returns: {'1M': 10.47, '3M': 8.67, '6M': 9.07, '1Y': 72.51}
- latest_volume: 8,160,900.0000
- average_volume_30d: 6,619,166.6667

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
