# NFLX Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Netflix, Inc.
- Total Score: 48 / 100
- Confidence: High
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 48 点を獲得し、シグナル充足率は 48.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

16点

理由

- revenue_growth(直近4四半期平均) は 15.65% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 5.23% で、プラス成長を維持しています。
- eps_growth は直近四半期が前四半期より -75.25pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 45,183,036,000.0000
- eps: 2.5800
- net_income: 10,981,201,000.0000
- operating_income: 13,326,603,000.0000
- research_and_development: 3,391,390,000.0000
- revenue_yoy_growth: 13.3700
- eps_yoy_growth: 11.1100
- revenue_yoy_growth_avg: 15.6500
- eps_yoy_growth_avg: 5.2300
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

16点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.09 倍で、負債負担は中程度です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.19 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 9,033,681,000.0000
- total_liabilities: 28,981,505,000.0000
- shareholders_equity: 26,615,488,000.0000
- long_term_debt: 13,463,971,000.0000
- current_ratio: 1.1857

## Valuation

6点

理由

- PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 22.5755
- forward_pe: 18.7887
- peg_ratio: 1.4100
- price_to_book: 9.9144
- sector_peer_count: 10
- trailing_pe_percentile: 77.7800
- trailing_pe_peer_count: 10
- forward_pe_percentile: 66.6700
- forward_pe_peer_count: 10
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 10
- price_to_book_percentile: 100
- price_to_book_peer_count: 10

## Momentum

6点

理由

- 1M の対SPY超過リターンは -9.55pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -9.23pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -37.80pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -58.39pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 3.74 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -10.5086
- 3M: -7.2241
- 6M: -21.7462
- 1Y: -41.5629
- benchmark: SPY
- benchmark_returns: {'1M': -0.96, '3M': 2.0, '6M': 16.06, '1Y': 16.83}
- excess_returns: {'1M': -9.55, '3M': -9.23, '6M': -37.8, '1Y': -58.39}
- latest_volume: 113,606,170.0000
- average_volume_30d: 30,359,279.0000

## News

4点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 0 件、悪材料 7 件(純比率 -1.00)で、センチメントは 0.0 点です。
- イベント後の平均株価反応が -4.67% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 0
- negative_count: 7
- sentiment_net_ratio: -1.0000
- event_count: 10
- events_with_price_reaction: 3

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
