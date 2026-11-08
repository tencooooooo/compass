# TXN Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Texas Instruments Incorporated
- Total Score: 67 / 100
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

- データが確認できた 100 点満点のうち 67 点を獲得し、シグナル充足率は 67.0% です。
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

- PER はセクター内 71.43 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 80.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PEG はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 80.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 35.9741
- forward_pe: 23.9852
- peg_ratio: 0.8400
- price_to_book: 13.2139
- sector_peer_count: 16
- trailing_pe_percentile: 71.4300
- trailing_pe_peer_count: 15
- forward_pe_percentile: 80.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 80.0000
- price_to_book_peer_count: 16

## Momentum

14点

理由

- 1M の対SPY超過リターンは +1.70pt で、市場並み以上です。
- 3M の対SPY超過リターンは +4.03pt で、市場並み以上です。
- 6M の対SPY超過リターンは -2.85pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンが +63.57pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 1.34 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -3.2916
- 3M: -0.6156
- 6M: -2.6613
- 1Y: 73.2604
- benchmark: SPY
- benchmark_returns: {'1M': -4.99, '3M': -4.65, '6M': 0.19, '1Y': 9.69}
- excess_returns: {'1M': 1.7, '3M': 4.03, '6M': -2.85, '1Y': 63.57}
- latest_volume: 10,094,200.0000
- average_volume_30d: 7,558,396.6667

## News

11点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 1 件(純比率 +0.00)で、センチメントは 4.0 点です。
- イベント後の平均株価反応が -0.28% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 1
- sentiment_net_ratio: 0.0000
- event_count: 10
- events_with_price_reaction: 7

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
