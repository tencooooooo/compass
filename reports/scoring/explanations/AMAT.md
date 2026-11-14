# AMAT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Applied Materials, Inc.
- Total Score: 57 / 100
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

- データが確認できた 100 点満点のうち 57 点を獲得し、シグナル充足率は 57.0% です。
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
- Forward PER はセクター内 40.00 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 29.3582
- forward_pe: 15.0938
- peg_ratio: 0.8100
- price_to_book: 11.2542
- sector_peer_count: 16
- trailing_pe_percentile: 64.2900
- trailing_pe_peer_count: 15
- forward_pe_percentile: 40.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 53.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 16

## Momentum

8点

理由

- 1M の対SPY超過リターンは -11.58pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -28.59pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -17.52pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンが +49.89pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 1.51 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -13.8392
- 3M: -30.7138
- 6M: -14.9473
- 1Y: 61.4655
- benchmark: SPY
- benchmark_returns: {'1M': -2.26, '3M': -2.13, '6M': 2.57, '1Y': 11.58}
- excess_returns: {'1M': -11.58, '3M': -28.59, '6M': -17.52, '1Y': 49.89}
- latest_volume: 11,937,400.0000
- average_volume_30d: 7,928,906.6667

## News

10点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 6 件、悪材料 2 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベント後の平均株価反応が -2.74% と弱く、注意が必要です。

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
- events_with_price_reaction: 7

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
