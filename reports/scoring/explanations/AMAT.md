# AMAT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Applied Materials, Inc.
- Total Score: 66 / 100
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

- データが確認できた 100 点満点のうち 66 点を獲得し、シグナル充足率は 66.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 5.96% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 36.15% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +13.56pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より -41.71pt 低く、成長の減速に注意が必要です。
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
- revenue_yoy_growth: 11.4100
- eps_yoy_growth: 33.4600
- revenue_yoy_growth_avg: 5.9600
- eps_yoy_growth_avg: 36.1500
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

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

3点

理由

- PER はセクター内 78.57 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 80.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PEG はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 80.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 42.8842
- forward_pe: 27.0522
- peg_ratio: 1.0900
- price_to_book: 15.3732
- sector_peer_count: 16
- trailing_pe_percentile: 78.5700
- trailing_pe_peer_count: 15
- forward_pe_percentile: 80.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 46.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 80.0000
- price_to_book_peer_count: 16

## Momentum

15点

理由

- 1M の対SPY超過リターンは -14.89pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンが +17.00pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +22.03pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +184.76pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.81 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -12.1123
- 3M: 22.0876
- 6M: 34.6890
- 1Y: 205.6380
- benchmark: SPY
- benchmark_returns: {'1M': 2.78, '3M': 5.09, '6M': 12.66, '1Y': 20.87}
- excess_returns: {'1M': -14.89, '3M': 17.0, '6M': 22.03, '1Y': 184.76}
- latest_volume: 6,538,091.0000
- average_volume_30d: 8,028,089.7000

## News

11点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 1 件(純比率 +0.67)で、センチメントは 6.7 点です。
- イベント後の平均株価反応が -3.79% と弱く、注意が必要です。

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
- events_with_price_reaction: 9

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
