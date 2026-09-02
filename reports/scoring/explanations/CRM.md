# CRM Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Salesforce, Inc.
- Total Score: 74 / 100
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

- データが確認できた 100 点満点のうち 74 点を獲得し、シグナル充足率は 74.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 10.62% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 60.75% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +66.68pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 41,525,000,000.0000
- eps: 7.8500
- net_income: 7,457,000,000.0000
- operating_income: 8,917,000,000.0000
- research_and_development: 5,993,000,000.0000
- revenue_yoy_growth: 10.8300
- eps_yoy_growth: 118.8800
- revenue_yoy_growth_avg: 10.6200
- eps_yoy_growth_avg: 60.7500
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2025-Q4', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2025-Q4', '2025-Q3']

## Financial Health

16点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.90 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 0.76 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 7,327,000,000.0000
- total_liabilities: 53,163,000,000.0000
- shareholders_equity: 59,142,000,000.0000
- long_term_debt: 10,439,000,000.0000
- current_ratio: 0.7603

## Valuation

14点

理由

- PER はセクター内 28.57 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 33.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 13.33 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 23.5284
- forward_pe: 16.1312
- peg_ratio: 1.0700
- price_to_book: 5.5097
- sector_peer_count: 16
- trailing_pe_percentile: 28.5700
- trailing_pe_peer_count: 15
- forward_pe_percentile: 33.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 73.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 13.3300
- price_to_book_peer_count: 16

## Momentum

15点

理由

- 1M の対SPY超過リターンが +35.33pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +33.43pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +21.47pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -18.36pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.88 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 34.5254
- 3M: 35.1415
- 6M: 33.7463
- 1Y: 2.4696
- benchmark: SPY
- benchmark_returns: {'1M': -0.8, '3M': 1.71, '6M': 12.27, '1Y': 20.83}
- excess_returns: {'1M': 35.33, '3M': 33.43, '6M': 21.47, '1Y': -18.36}
- latest_volume: 13,359,403.0000
- average_volume_30d: 15,194,233.4333

## News

12点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 1 件(純比率 +0.33)で、センチメントは 5.3 点です。
- イベント後の平均株価反応が -0.46% と中立圏です。

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
- events_with_price_reaction: 9

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
