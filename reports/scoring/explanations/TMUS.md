# TMUS Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: T-Mobile US, Inc.
- Total Score: 56 / 100
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

- データが確認できた 100 点満点のうち 56 点を獲得し、シグナル充足率は 56.0% です。
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
- PEG はセクター内 0.00 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PBR はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 19.5921
- forward_pe: 12.9722
- peg_ratio: 0.6400
- price_to_book: 3.5780
- sector_peer_count: 10
- trailing_pe_percentile: 55.5600
- trailing_pe_peer_count: 10
- forward_pe_percentile: 44.4400
- forward_pe_peer_count: 10
- peg_ratio_percentile: 0
- peg_ratio_peer_count: 10
- price_to_book_percentile: 55.5600
- price_to_book_peer_count: 10

## Momentum

8点

理由

- 1M の対SPY超過リターンは +7.10pt で、市場並み以上です。
- 3M の対SPY超過リターンは +2.11pt で、市場並み以上です。
- 6M の対SPY超過リターンは -26.07pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -46.09pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.14 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 6.3038
- 3M: 3.8198
- 6M: -13.7940
- 1Y: -25.2582
- benchmark: SPY
- benchmark_returns: {'1M': -0.8, '3M': 1.71, '6M': 12.27, '1Y': 20.83}
- excess_returns: {'1M': 7.1, '3M': 2.11, '6M': -26.07, '1Y': -46.09}
- latest_volume: 5,351,532.0000
- average_volume_30d: 4,674,107.7333

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が -0.04% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 7

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
