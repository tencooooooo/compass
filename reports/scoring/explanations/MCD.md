# MCD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: MCD
- Total Score: 41 / 100
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

- データが確認できた 100 点満点のうち 41 点を獲得し、シグナル充足率は 41.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

10点

理由

- revenue_growth(直近4四半期平均) は 5.40% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 6.60% で、プラス成長を維持しています。
- revenue_growth は直近四半期が前四半期より -5.68pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 26,885,000,000.0000
- eps: 12.0504
- net_income: 8,563,000,000.0000
- operating_income: 12,394,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: 3.7400
- eps_yoy_growth: 5.7300
- revenue_yoy_growth_avg: 5.4000
- eps_yoy_growth_avg: 6.6000
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

欠損・計算不可

- research_and_development

## Financial Health

7点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスではないため、財務健全性の加点を抑えています。
- 総負債は取得できていますが、自己資本との比較が不十分です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 0.95 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 774,000,000.0000
- total_liabilities: 61,306,000,000.0000
- shareholders_equity: -1,790,000,000.0000
- long_term_debt: 39,973,000,000.0000
- current_ratio: 0.9546

## Valuation

6点

理由

- PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR は -186.12 で、指標がマイナスのため加点対象外です。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.8805
- forward_pe: 19.2258
- peg_ratio: 2.4900
- price_to_book: -186.1203
- sector_peer_count: 10
- trailing_pe_percentile: 33.3300
- trailing_pe_peer_count: 10
- forward_pe_percentile: 33.3300
- forward_pe_peer_count: 10
- peg_ratio_percentile: 77.7800
- peg_ratio_peer_count: 10
- price_to_book_percentile: N/A
- price_to_book_peer_count: 0

## Momentum

5点

理由

- 1M の対SPY超過リターンは +0.08pt で、市場並み以上です。
- 3M の対SPY超過リターンは -6.47pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -28.71pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -31.86pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.79 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 2.1095
- 3M: -3.3235
- 6M: -16.7042
- 1Y: -11.3434
- benchmark: SPY
- benchmark_returns: {'1M': 2.03, '3M': 3.15, '6M': 12.01, '1Y': 20.51}
- excess_returns: {'1M': 0.08, '3M': -6.47, '6M': -28.71, '1Y': -31.86}
- latest_volume: 3,525,079.0000
- average_volume_30d: 4,452,515.9667

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 1 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベント後の平均株価反応が 0.58% と中立圏です。

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
