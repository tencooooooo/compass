# TMUS Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: T-Mobile US, Inc.
- Total Score: 45 / 100
- Confidence: Medium
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 1 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 45 点を獲得し、シグナル充足率は 45.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

8点

理由

- revenue_growth(直近4四半期平均) は 8.57% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は -0.08% で、前年同期比ではマイナスです。
- eps_growth は直近四半期が前四半期より +17.30pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 88,309,000,000.0000
- eps: 9.7500
- net_income: 10,992,000,000.0000
- operating_income: 18,557,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: 7.8500
- eps_yoy_growth: 5.2800
- revenue_yoy_growth_avg: 8.5700
- eps_yoy_growth_avg: -0.0800
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

欠損・計算不可

- research_and_development

## Financial Health

11点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 2.70 倍で、負債負担の確認が必要です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 1.00 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 5,598,000,000.0000
- total_liabilities: 160,034,000,000.0000
- shareholders_equity: 59,203,000,000.0000
- long_term_debt: 81,147,000,000.0000
- current_ratio: 0.9984

## Valuation

14点

理由

- PER はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PBR はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 19.0168
- forward_pe: 12.5781
- peg_ratio: 0.8400
- price_to_book: 3.4693
- sector_peer_count: 10
- trailing_pe_percentile: 55.5600
- trailing_pe_peer_count: 10
- forward_pe_percentile: 44.4400
- forward_pe_peer_count: 10
- peg_ratio_percentile: 11.1100
- peg_ratio_peer_count: 10
- price_to_book_percentile: 55.5600
- price_to_book_peer_count: 10

## Momentum

3点

理由

- 1M の対SPY超過リターンは -1.15pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -6.76pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -29.37pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -46.56pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.69 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 2.4829
- 3M: -4.4554
- 6M: -17.3469
- 1Y: -26.5599
- benchmark: SPY
- benchmark_returns: {'1M': 3.63, '3M': 2.3, '6M': 12.02, '1Y': 20.0}
- excess_returns: {'1M': -1.15, '3M': -6.76, '6M': -29.37, '1Y': -46.56}
- latest_volume: 3,210,492.0000
- average_volume_30d: 4,664,609.7333

## News

9点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 4 件(純比率 -0.60)で、センチメントは 1.6 点です。
- イベント後の平均株価反応が 0.59% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 4
- sentiment_net_ratio: -0.6000
- event_count: 10
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
