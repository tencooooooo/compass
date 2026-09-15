# ORCL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Oracle Corporation
- Total Score: 59 / 100
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

- データが確認できた 100 点満点のうち 59 点を獲得し、シグナル充足率は 59.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

19点

理由

- revenue_growth(直近4四半期平均) は 19.41% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 41.98% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +7.95pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +29.95pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 67,357,000,000.0000
- eps: 5.9400
- net_income: 17,087,000,000.0000
- operating_income: 22,444,000,000.0000
- research_and_development: 10,272,000,000.0000
- revenue_yoy_growth: 29.6100
- eps_yoy_growth: 54.4600
- revenue_yoy_growth_avg: 19.4100
- eps_yoy_growth_avg: 41.9800
- revenue_growth_quarters: ['2026-Q3', '2026-Q1', '2025-Q4', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q1', '2025-Q4', '2025-Q3']

## Financial Health

13点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 5.14 倍で、負債負担の確認が必要です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 1.12 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 31,289,000,000.0000
- total_liabilities: 218,703,000,000.0000
- shareholders_equity: 42,508,000,000.0000
- long_term_debt: 122,342,000,000.0000
- current_ratio: 1.1150

## Valuation

14点

理由

- PER はセクター内 28.57 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 13.33 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PEG はセクター内 40.00 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.9640
- forward_pe: 12.7662
- peg_ratio: 0.8500
- price_to_book: 10.7630
- sector_peer_count: 16
- trailing_pe_percentile: 28.5700
- trailing_pe_peer_count: 15
- forward_pe_percentile: 13.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 40.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 53.3300
- price_to_book_peer_count: 16

## Momentum

4点

理由

- 1M の対SPY超過リターンは -4.32pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -27.49pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -23.20pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -67.90pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.11 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -6.7566
- 3M: -26.8904
- 6M: -9.3863
- 1Y: -51.4170
- benchmark: SPY
- benchmark_returns: {'1M': -2.44, '3M': 0.6, '6M': 13.81, '1Y': 16.48}
- excess_returns: {'1M': -4.32, '3M': -27.49, '6M': -23.2, '1Y': -67.9}
- latest_volume: 31,159,828.0000
- average_volume_30d: 28,112,560.9333

## News

9点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 1 件(純比率 +0.33)で、センチメントは 5.3 点です。
- イベント後の平均株価反応が -3.07% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 2
- negative_count: 1
- sentiment_net_ratio: 0.3300
- event_count: 10
- events_with_price_reaction: 6

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
