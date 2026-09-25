# NOW Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: ServiceNow, Inc.
- Total Score: 58 / 100
- Confidence: Medium
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 1 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 58 点を獲得し、シグナル充足率は 58.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

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

6点

理由

- PER はセクター内 92.86 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 80.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PEG はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 86.1125
- forward_pe: 27.5257
- peg_ratio: 1.0100
- price_to_book: 11.3811
- sector_peer_count: 16
- trailing_pe_percentile: 92.8600
- trailing_pe_peer_count: 15
- forward_pe_percentile: 80.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 73.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 53.3300
- price_to_book_peer_count: 16

## Momentum

12点

理由

- 1M の対SPY超過リターンは +9.12pt で、市場並み以上です。
- 3M の対SPY超過リターンが +45.11pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +16.38pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -42.12pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.72 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 9.9414
- 3M: 50.0853
- 6M: 34.5246
- 1Y: -25.7317
- benchmark: SPY
- benchmark_returns: {'1M': 0.82, '3M': 4.97, '6M': 18.15, '1Y': 16.38}
- excess_returns: {'1M': 9.12, '3M': 45.11, '6M': 16.38, '1Y': -42.12}
- latest_volume: 11,366,200.0000
- average_volume_30d: 15,864,493.3333

## News

10点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 2 件(純比率 +0.20)で、センチメントは 4.8 点です。
- イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 3
- negative_count: 2
- sentiment_net_ratio: 0.2000
- event_count: 10
- events_with_price_reaction: 0

欠損・計算不可

- event_price_reaction

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
