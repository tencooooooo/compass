# TSLA Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Tesla, Inc.
- Total Score: 45 / 100
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

- データが確認できた 100 点満点のうち 45 点を獲得し、シグナル充足率は 45.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

12点

理由

- revenue_growth(直近4四半期平均) は 10.27% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は -12.32% で、前年同期比ではマイナスです。
- revenue_growth は直近四半期が前四半期より +9.74pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より -11.36pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 94,827,000,000.0000
- eps: 1.1765
- net_income: 3,794,000,000.0000
- operating_income: 4,849,000,000.0000
- research_and_development: 6,411,000,000.0000
- revenue_yoy_growth: 25.5200
- eps_yoy_growth: -3.0300
- revenue_yoy_growth_avg: 10.2700
- eps_yoy_growth_avg: -12.3200
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.67 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.16 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 16,513,000,000.0000
- total_liabilities: 54,941,000,000.0000
- shareholders_equity: 82,137,000,000.0000
- long_term_debt: 6,584,000,000.0000
- current_ratio: 2.1644

## Valuation

3点

理由

- PER はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR はセクター内 50.00 パーセンタイル / 母数 5 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 308.9717
- forward_pe: 150.2664
- peg_ratio: 4.8100
- price_to_book: 14.8902
- sector_peer_count: 10
- trailing_pe_percentile: 100
- trailing_pe_peer_count: 10
- forward_pe_percentile: 100
- forward_pe_peer_count: 10
- peg_ratio_percentile: 100
- peg_ratio_peer_count: 10
- price_to_book_percentile: 50.0000
- price_to_book_peer_count: 5

## Momentum

1点

理由

- 1M の対SPY超過リターンは -20.08pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -29.36pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -35.18pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -26.22pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.71 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -17.3330
- 3M: -24.4411
- 6M: -22.9769
- 1Y: -3.3979
- benchmark: SPY
- benchmark_returns: {'1M': 2.75, '3M': 4.92, '6M': 12.21, '1Y': 22.82}
- excess_returns: {'1M': -20.08, '3M': -29.36, '6M': -35.18, '1Y': -26.22}
- latest_volume: 27,695,899.0000
- average_volume_30d: 39,189,919.9667

## News

9点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 1 件(純比率 +0.33)で、センチメントは 5.3 点です。
- イベント後の平均株価反応が -1.59% と弱く、注意が必要です。

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
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
