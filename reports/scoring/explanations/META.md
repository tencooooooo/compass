# META Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Meta Platforms, Inc.
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

20点

理由

- revenue_growth(直近4四半期平均) は 28.34% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 57.77% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +278.21pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 200,966,000,000.0000
- eps: 23.9800
- net_income: 60,458,000,000.0000
- operating_income: 83,276,000,000.0000
- research_and_development: 57,372,000,000.0000
- revenue_yoy_growth: 26.0700
- eps_yoy_growth: 264.7600
- revenue_yoy_growth_avg: 28.3400
- eps_yoy_growth_avg: 57.7700
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.68 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.60 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 35,873,000,000.0000
- total_liabilities: 148,778,000,000.0000
- shareholders_equity: 217,243,000,000.0000
- long_term_debt: 58,744,000,000.0000
- current_ratio: 2.5988

## Valuation

5点

理由

- PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PBR はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.8932
- forward_pe: 18.0312
- peg_ratio: 0.8100
- price_to_book: 6.0215
- sector_peer_count: 10
- trailing_pe_percentile: 77.7800
- trailing_pe_peer_count: 10
- forward_pe_percentile: 77.7800
- forward_pe_peer_count: 10
- peg_ratio_percentile: 22.2200
- peg_ratio_peer_count: 10
- price_to_book_percentile: 77.7800
- price_to_book_peer_count: 10

## Momentum

5点

理由

- 1M の対SPY超過リターンは -13.19pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは +7.93pt で、市場並み以上です。
- 6M の対SPY超過リターンは -1.56pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -11.80pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.48 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -15.4473
- 3M: 5.8069
- 6M: 1.0107
- 1Y: -0.2160
- benchmark: SPY
- benchmark_returns: {'1M': -2.26, '3M': -2.13, '6M': 2.57, '1Y': 11.58}
- excess_returns: {'1M': -13.19, '3M': 7.93, '6M': -1.56, '1Y': -11.8}
- latest_volume: 10,341,800.0000
- average_volume_30d: 21,468,896.6667

## News

11点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 1 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 3
- negative_count: 1
- sentiment_net_ratio: 0.5000
- event_count: 10
- events_with_price_reaction: 0

欠損・計算不可

- event_price_reaction

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
