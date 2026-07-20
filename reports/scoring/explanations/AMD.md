# AMD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Advanced Micro Devices, Inc.
- Total Score: 72 / 100
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

- データが確認できた 100 点満点のうち 72 点を獲得し、シグナル充足率は 72.0% です。
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

- trailing_pe: 166.7450
- forward_pe: 37.3992
- peg_ratio: 1.1600
- price_to_book: 12.7335
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

11点

理由

- 1M の対SPY超過リターンは -2.15pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンが +76.12pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +113.17pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +194.46pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.78 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -1.7386
- 3M: 80.8865
- 6M: 120.9416
- 1Y: 213.9268
- benchmark: SPY
- benchmark_returns: {'1M': 0.41, '3M': 4.77, '6M': 7.77, '1Y': 19.47}
- excess_returns: {'1M': -2.15, '3M': 76.12, '6M': 113.17, '1Y': 194.46}
- latest_volume: 23,212,955.0000
- average_volume_30d: 29,937,231.8333

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 1 件(純比率 +0.60)で、センチメントは 6.4 点です。
- イベント後の平均株価反応が 1.58% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 1
- sentiment_net_ratio: 0.6000
- event_count: 10
- events_with_price_reaction: 5

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
