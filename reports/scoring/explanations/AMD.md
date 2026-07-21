# AMD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Advanced Micro Devices, Inc.
- Total Score: 75 / 100
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

- データが確認できた 100 点満点のうち 75 点を獲得し、シグナル充足率は 75.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 35.26% で、+30%以上の高成長です。
- eps_growth(直近4四半期平均) は 229.14% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +31.34pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 34,639,000,000.0000
- eps: 2.6700
- net_income: 4,335,000,000.0000
- operating_income: 3,694,000,000.0000
- research_and_development: 8,091,000,000.0000
- revenue_yoy_growth: 37.8500
- eps_yoy_growth: 90.9100
- revenue_yoy_growth_avg: 35.2600
- eps_yoy_growth_avg: 229.1400
- revenue_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.22 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.85 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 5,539,000,000.0000
- total_liabilities: 13,927,000,000.0000
- shareholders_equity: 62,999,000,000.0000
- long_term_debt: 2,348,000,000.0000
- current_ratio: 2.8500

## Valuation

6点

理由

- PER はセクター内 100.00 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 93.33 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PEG はセクター内 60.00 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 180.2748
- forward_pe: 40.4338
- peg_ratio: 1.1600
- price_to_book: 13.7667
- sector_peer_count: 16
- trailing_pe_percentile: 100
- trailing_pe_peer_count: 15
- forward_pe_percentile: 93.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 60.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 16

## Momentum

14点

理由

- 1M の対SPY超過リターンは +1.11pt で、市場並み以上です。
- 3M の対SPY超過リターンが +92.16pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +126.08pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +226.24pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.93 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 1.3138
- 3M: 98.0105
- 6M: 134.8402
- 1Y: 246.7928
- benchmark: SPY
- benchmark_returns: {'1M': 0.21, '3M': 5.85, '6M': 8.76, '1Y': 20.55}
- excess_returns: {'1M': 1.11, '3M': 92.16, '6M': 126.08, '1Y': 226.24}
- latest_volume: 27,221,951.0000
- average_volume_30d: 29,290,425.0333

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 6 件、悪材料 2 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベント後の平均株価反応が 6.81% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 6
- negative_count: 2
- sentiment_net_ratio: 0.5000
- event_count: 10
- events_with_price_reaction: 5

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
