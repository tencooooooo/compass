# META Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Meta Platforms, Inc.
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

17点

理由

- revenue_growth(直近4四半期平均) は 24.25% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 13.66% で、プラス成長を維持しています。
- revenue_growth は直近四半期が前四半期より +6.83pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +144.95pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 33.0800
- eps_yoy_growth: 62.3600
- revenue_yoy_growth_avg: 24.2500
- eps_yoy_growth_avg: 13.6600
- revenue_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']

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

9点

理由

- PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.6275
- forward_pe: 16.0810
- peg_ratio: 0.8800
- price_to_book: 6.1991
- sector_peer_count: 10
- trailing_pe_percentile: 77.7800
- trailing_pe_peer_count: 10
- forward_pe_percentile: 66.6700
- forward_pe_peer_count: 10
- peg_ratio_percentile: 33.3300
- peg_ratio_peer_count: 10
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 10

## Momentum

3点

理由

- 1M の対SPY超過リターンは +5.95pt で、市場並み以上です。
- 3M の対SPY超過リターンは -14.19pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -15.75pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -34.12pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.61 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 6.7280
- 3M: -9.6197
- 6M: -7.9333
- 1Y: -16.3176
- benchmark: SPY
- benchmark_returns: {'1M': 0.78, '3M': 4.57, '6M': 7.82, '1Y': 17.8}
- excess_returns: {'1M': 5.95, '3M': -14.19, '6M': -15.75, '1Y': -34.12}
- latest_volume: 11,309,789.0000
- average_volume_30d: 18,560,816.3000

## News

10点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 2 件(純比率 +0.43)で、センチメントは 5.7 点です。
- イベント後の平均株価反応が -1.80% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 5
- negative_count: 2
- sentiment_net_ratio: 0.4300
- event_count: 10
- events_with_price_reaction: 5

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
