# AMAT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Applied Materials, Inc.
- Total Score: 77 / 100
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

- データが確認できた 100 点満点のうち 77 点を獲得し、シグナル充足率は 77.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 10.45% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 39.93% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +13.42pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +9.33pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 28,368,000,000.0000
- eps: 8.7100
- net_income: 6,998,000,000.0000
- operating_income: 8,470,000,000.0000
- research_and_development: 3,570,000,000.0000
- revenue_yoy_growth: 24.8300
- eps_yoy_growth: 42.7900
- revenue_yoy_growth_avg: 10.4500
- eps_yoy_growth_avg: 39.9300
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.78 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.61 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 7,241,000,000.0000
- total_liabilities: 15,884,000,000.0000
- shareholders_equity: 20,415,000,000.0000
- long_term_debt: 6,455,000,000.0000
- current_ratio: 2.6105

## Valuation

12点

理由

- PER はセクター内 71.43 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 64.29 パーセンタイル / 母数 15 で、中位レンジです。
- PEG はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 40.0207
- forward_pe: 25.1555
- peg_ratio: 0.8800
- price_to_book: 14.3768
- sector_peer_count: 16
- trailing_pe_percentile: 71.4300
- trailing_pe_peer_count: 15
- forward_pe_percentile: 64.2900
- forward_pe_peer_count: 15
- peg_ratio_percentile: 53.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 73.3300
- price_to_book_peer_count: 16

## Momentum

12点

理由

- 1M の対SPY超過リターンは -9.59pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -30.14pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは +8.40pt で、市場並み以上です。
- 1Y の対SPY超過リターンが +133.83pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 2.01 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -10.3039
- 3M: -27.8823
- 6M: 24.7442
- 1Y: 150.9565
- benchmark: SPY
- benchmark_returns: {'1M': -0.71, '3M': 2.26, '6M': 16.34, '1Y': 17.12}
- excess_returns: {'1M': -9.59, '3M': -30.14, '6M': 8.4, '1Y': 133.83}
- latest_volume: 14,276,700.0000
- average_volume_30d: 7,105,666.6667

## News

16点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 1 件(純比率 +0.67)で、センチメントは 6.7 点です。
- イベント後の平均株価反応が 6.51% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 5
- negative_count: 1
- sentiment_net_ratio: 0.6700
- event_count: 10
- events_with_price_reaction: 2

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
