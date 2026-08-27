# CRM Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Salesforce, Inc.
- Total Score: 72 / 100
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

- データが確認できた 100 点満点のうち 72 点を獲得し、シグナル充足率は 72.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 9.82% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 31.52% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +13.59pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 13.2700
- eps_yoy_growth: 52.2000
- revenue_yoy_growth_avg: 9.8200
- eps_yoy_growth_avg: 31.5200
- revenue_growth_quarters: ['2026-Q2', '2025-Q4', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2025-Q4', '2025-Q3', '2025-Q2']

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

16点

理由

- PER はセクター内 28.57 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PEG はセクター内 40.00 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 6.67 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 23.7986
- forward_pe: 13.2478
- peg_ratio: 0.8500
- price_to_book: 4.9190
- sector_peer_count: 16
- trailing_pe_percentile: 28.5700
- trailing_pe_peer_count: 15
- forward_pe_percentile: 20.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 40.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 6.6700
- price_to_book_peer_count: 16

## Momentum

11点

理由

- 1M の対SPY超過リターンは +9.89pt で、市場並み以上です。
- 3M の対SPY超過リターンが +13.79pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンは -3.33pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -36.90pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.13 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 13.2893
- 3M: 16.1347
- 6M: 7.7790
- 1Y: -16.3431
- benchmark: SPY
- benchmark_returns: {'1M': 3.4, '3M': 2.34, '6M': 11.11, '1Y': 20.56}
- excess_returns: {'1M': 9.89, '3M': 13.79, '6M': -3.33, '1Y': -36.9}
- latest_volume: 14,051,371.0000
- average_volume_30d: 12,469,422.3667

## News

12点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 7 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が -1.61% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 7
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 1

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
