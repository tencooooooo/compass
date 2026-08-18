# ORCL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Oracle Corporation
- Total Score: 58 / 100
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

- データが確認できた 100 点満点のうち 58 点を獲得し、シグナル充足率は 58.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 13.61% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 33.37% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +7.44pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より -66.40pt 低く、成長の減速に注意が必要です。
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
- revenue_yoy_growth: 21.6600
- eps_yoy_growth: 24.5100
- revenue_yoy_growth_avg: 13.6100
- eps_yoy_growth_avg: 33.3700
- revenue_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']

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

12点

理由

- PER はセクター内 35.71 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 26.67 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 40.00 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 60.00 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 24.4503
- forward_pe: 13.0821
- peg_ratio: 0.8500
- price_to_book: 10.9502
- sector_peer_count: 16
- trailing_pe_percentile: 35.7100
- trailing_pe_peer_count: 15
- forward_pe_percentile: 26.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 40.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 60.0000
- price_to_book_peer_count: 16

## Momentum

5点

理由

- 1M の対SPY超過リターンが +14.22pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -27.38pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -19.60pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -62.43pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.50 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 17.6388
- 3M: -23.2159
- 6M: -6.6135
- 1Y: -41.8328
- benchmark: SPY
- benchmark_returns: {'1M': 3.42, '3M': 4.17, '6M': 12.99, '1Y': 20.59}
- excess_returns: {'1M': 14.22, '3M': -27.38, '6M': -19.6, '1Y': -62.43}
- latest_volume: 17,107,649.0000
- average_volume_30d: 34,451,198.3000

## News

11点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 1 件(純比率 +0.67)で、センチメントは 6.7 点です。
- イベント後の平均株価反応が -2.63% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 5
- negative_count: 1
- sentiment_net_ratio: 0.6700
- event_count: 10
- events_with_price_reaction: 8

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
