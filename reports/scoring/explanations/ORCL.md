# ORCL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Oracle Corporation
- Total Score: 61 / 100
- Confidence: Medium
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 1 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 61 点を獲得し、シグナル充足率は 61.0% です。
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

16点

理由

- PER はセクター内 21.43 パーセンタイル / 母数 15 で、相対的に割安寄りです。
- Forward PER はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PEG はセクター内 33.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.4890
- forward_pe: 12.4668
- peg_ratio: 0.7800
- price_to_book: 10.5138
- sector_peer_count: 16
- trailing_pe_percentile: 21.4300
- trailing_pe_peer_count: 15
- forward_pe_percentile: 20.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 33.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 46.6700
- price_to_book_peer_count: 16

## Momentum

5点

理由

- 1M の対SPY超過リターンは -4.02pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -12.89pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -21.16pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -71.95pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.96 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -3.6060
- 3M: -8.1559
- 6M: -3.7704
- 1Y: -55.0297
- benchmark: SPY
- benchmark_returns: {'1M': 0.41, '3M': 4.74, '6M': 17.39, '1Y': 16.92}
- excess_returns: {'1M': -4.02, '3M': -12.89, '6M': -21.16, '1Y': -71.95}
- latest_volume: 56,629,400.0000
- average_volume_30d: 28,947,076.6667

## News

8点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 2 件(純比率 -0.33)で、センチメントは 2.7 点です。
- イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。

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
- events_with_price_reaction: 0

欠損・計算不可

- event_price_reaction

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
