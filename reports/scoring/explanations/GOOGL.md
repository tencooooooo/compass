# GOOGL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Alphabet Inc.
- Total Score: 69 / 100
- Confidence: Medium
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 2 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 100 点満点のうち 69 点を獲得し、シグナル充足率は 69.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 18.94% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 108.46% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +212.52pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 402,836,000,000.0000
- eps: 10.9100
- net_income: 132,170,000,000.0000
- operating_income: 129,039,000,000.0000
- research_and_development: 61,087,000,000.0000
- revenue_yoy_growth: 24.2300
- eps_yoy_growth: 294.3700
- revenue_yoy_growth_avg: 18.9400
- eps_yoy_growth_avg: 108.4600
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

14点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債が取得できないため、負債項目は加点していません。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 2.01 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 30,708,000,000.0000
- total_liabilities: N/A
- shareholders_equity: 415,265,000,000.0000
- long_term_debt: 46,547,000,000.0000
- current_ratio: 2.0053

欠損・計算不可

- total_liabilities

## Valuation

9点

理由

- PER はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 17.8198
- forward_pe: 23.8525
- peg_ratio: 1.2700
- price_to_book: 6.9744
- sector_peer_count: 10
- trailing_pe_percentile: 55.5600
- trailing_pe_peer_count: 10
- forward_pe_percentile: 100
- forward_pe_peer_count: 10
- peg_ratio_percentile: 55.5600
- peg_ratio_peer_count: 10
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 10

## Momentum

13点

理由

- 1M の対SPY超過リターンは +2.18pt で、市場並み以上です。
- 3M の対SPY超過リターンは -7.22pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -2.39pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンが +23.32pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 2.00 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 1.4634
- 3M: -4.9630
- 6M: 13.9497
- 1Y: 40.4436
- benchmark: SPY
- benchmark_returns: {'1M': -0.71, '3M': 2.26, '6M': 16.34, '1Y': 17.12}
- excess_returns: {'1M': 2.18, '3M': -7.22, '6M': -2.39, '1Y': 23.32}
- latest_volume: 47,526,100.0000
- average_volume_30d: 23,755,206.6667

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 2
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 0

欠損・計算不可

- event_price_reaction

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
