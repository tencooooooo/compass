# NOW Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: ServiceNow, Inc.
- Total Score: 68 / 100
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

- データが確認できた 100 点満点のうち 68 点を獲得し、シグナル充足率は 68.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

14点

理由

- revenue_growth(直近4四半期平均) は 22.57% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は -18.51% で、前年同期比ではマイナスです。
- eps_growth は直近四半期が前四半期より -23.89pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 13,278,000,000.0000
- eps: 1.6900
- net_income: 1,748,000,000.0000
- operating_income: 1,824,000,000.0000
- research_and_development: 2,960,000,000.0000
- revenue_yoy_growth: 24.0100
- eps_yoy_growth: -21.6200
- revenue_yoy_growth_avg: 22.5700
- eps_yoy_growth_avg: -18.5100
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

16点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.01 倍で、負債負担は中程度です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.00 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 3,726,000,000.0000
- total_liabilities: 13,074,000,000.0000
- shareholders_equity: 12,964,000,000.0000
- long_term_debt: 1,491,000,000.0000
- current_ratio: 1.0027

## Valuation

9点

理由

- PER はセクター内 92.86 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 79.5000
- forward_pe: 25.4085
- peg_ratio: 1.1100
- price_to_book: 10.5072
- sector_peer_count: 16
- trailing_pe_percentile: 92.8600
- trailing_pe_peer_count: 15
- forward_pe_percentile: 66.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 53.3300
- price_to_book_peer_count: 16

## Momentum

14点

理由

- 1M の対SPY超過リターンが +21.86pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +19.83pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンは +5.33pt で、市場並み以上です。
- 1Y の対SPY超過リターンは -49.58pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.99 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 24.6326
- 3M: 24.9141
- 6M: 17.9853
- 1Y: -28.7036
- benchmark: SPY
- benchmark_returns: {'1M': 2.78, '3M': 5.09, '6M': 12.66, '1Y': 20.87}
- excess_returns: {'1M': 21.86, '3M': 19.83, '6M': 5.33, '1Y': -49.58}
- latest_volume: 22,396,381.0000
- average_volume_30d: 22,609,149.3667

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 1 件(純比率 +0.60)で、センチメントは 6.4 点です。
- イベント後の平均株価反応が 4.97% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 1
- sentiment_net_ratio: 0.6000
- event_count: 10
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
