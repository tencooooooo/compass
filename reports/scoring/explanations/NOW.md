# NOW Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: ServiceNow, Inc.
- Total Score: 53 / 100
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

- データが確認できた 100 点満点のうち 53 点を獲得し、シグナル充足率は 53.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

14点

理由

- revenue_growth(直近4四半期平均) は 22.11% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は -34.98% で、前年同期比ではマイナスです。
- eps_growth は直近四半期が前四半期より -22.13pt 低く、成長の減速に注意が必要です。
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
- revenue_yoy_growth: 20.5200
- eps_yoy_growth: -43.7500
- revenue_yoy_growth_avg: 22.1100
- eps_yoy_growth_avg: -34.9800
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

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
- PEG はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 63.0288
- forward_pe: 18.2433
- peg_ratio: 0.7000
- price_to_book: 6.9433
- sector_peer_count: 16
- trailing_pe_percentile: 92.8600
- trailing_pe_peer_count: 15
- forward_pe_percentile: 66.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 46.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 46.6700
- price_to_book_peer_count: 16

## Momentum

4点

理由

- 1M の対SPY超過リターンは -34.49pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -22.16pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -7.20pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -51.57pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.05 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -44.1975
- 3M: -31.5814
- 6M: -14.2172
- 1Y: -46.3470
- benchmark: SPY
- benchmark_returns: {'1M': -9.71, '3M': -9.42, '6M': -7.02, '1Y': 5.22}
- excess_returns: {'1M': -34.49, '3M': -22.16, '6M': -7.2, '1Y': -51.57}
- latest_volume: 19,612,800.0000
- average_volume_30d: 18,757,783.3333

## News

10点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 1 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベント後の平均株価反応が -1.63% と弱く、注意が必要です。

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
- events_with_price_reaction: 9

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
