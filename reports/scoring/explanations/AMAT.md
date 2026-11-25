# AMAT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Applied Materials, Inc.
- Total Score: 53 / 100
- Confidence: Medium
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 4 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 53 点を獲得し、シグナル充足率は 53.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

7点

理由

- revenue_growth(直近4四半期平均) は 10.45% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 39.93% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +13.42pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +9.33pt 高く、成長の加速がみられます。
- 純利益 が取得できないため、この項目は加点していません。
- 営業利益 が取得できないため、この項目は加点していません。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上規模データが取得できないため、規模項目は加点していません。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: N/A
- eps: 12.7100
- net_income: N/A
- operating_income: N/A
- research_and_development: N/A
- revenue_yoy_growth: 24.8300
- eps_yoy_growth: 42.7900
- revenue_yoy_growth_avg: 10.4500
- eps_yoy_growth_avg: 39.9300
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

欠損・計算不可

- 純利益
- 営業利益
- research_and_development
- total_revenue

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

- PER はセクター内 64.29 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 33.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 57.14 パーセンタイル / 母数 15 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 27.4839
- forward_pe: 13.1915
- peg_ratio: 1.6500
- price_to_book: 9.8345
- sector_peer_count: 16
- trailing_pe_percentile: 64.2900
- trailing_pe_peer_count: 15
- forward_pe_percentile: 33.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 57.1400
- peg_ratio_peer_count: 15
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 16

## Momentum

7点

理由

- 1M の対SPY超過リターンは -10.26pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -26.47pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -23.85pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンが +35.02pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.97 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -16.3426
- 3M: -32.4146
- 6M: -27.5863
- 1Y: 45.2629
- benchmark: SPY
- benchmark_returns: {'1M': -6.09, '3M': -5.94, '6M': -3.74, '1Y': 10.24}
- excess_returns: {'1M': -10.26, '3M': -26.47, '6M': -23.85, '1Y': 35.02}
- latest_volume: 8,402,200.0000
- average_volume_30d: 8,681,590.0000

## News

7点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 2 件(純比率 -0.33)で、センチメントは 2.7 点です。
- イベント後の平均株価反応が -6.66% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 2
- sentiment_net_ratio: -0.3300
- event_count: 10
- events_with_price_reaction: 8

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
