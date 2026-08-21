# TXN Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Texas Instruments Incorporated
- Total Score: 69 / 100
- Confidence: High
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 100 点満点のうち 69 点を獲得し、シグナル充足率は 69.0% です。
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
- Forward PER はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 40.1153
- forward_pe: 25.1484
- peg_ratio: 1.1800
- price_to_book: 13.4036
- sector_peer_count: 16
- trailing_pe_percentile: 71.4300
- trailing_pe_peer_count: 15
- forward_pe_percentile: 66.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 73.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 73.3300
- price_to_book_peer_count: 16

## Momentum

8点

理由

- 1M の対SPY超過リターンは -10.49pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -14.31pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは +9.89pt で、市場並み以上です。
- 1Y の対SPY超過リターンが +13.76pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.74 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -6.7639
- 3M: -10.9509
- 6M: 21.5417
- 1Y: 35.0830
- benchmark: SPY
- benchmark_returns: {'1M': 3.73, '3M': 3.36, '6M': 11.66, '1Y': 21.33}
- excess_returns: {'1M': -10.49, '3M': -14.31, '6M': 9.89, '1Y': 13.76}
- latest_volume: 5,457,981.0000
- average_volume_30d: 7,342,839.3667

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が -0.58% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
