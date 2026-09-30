# MCD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: McDonald's Corporation
- Total Score: 30 / 100
- Confidence: Medium
- Signal Strength: Weak
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 4 領域です。
- 欠損または計算不可の項目数は 3 件です。
- データが不足している領域: News。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Weak

理由

- データが確認できた 80 点満点のうち 30 点を獲得し、シグナル充足率は 37.5% です。
- シグナル強度は Weak(Strong: 65%以上 / Moderate: 40%以上)です。

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

9点

理由

- PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- PBR は -161.81 で、指標がマイナスのため加点対象外です。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 19.0073
- forward_pe: 16.8784
- peg_ratio: 2.0200
- price_to_book: -161.8119
- sector_peer_count: 10
- trailing_pe_percentile: 33.3300
- trailing_pe_peer_count: 10
- forward_pe_percentile: 33.3300
- forward_pe_peer_count: 10
- peg_ratio_percentile: 55.5600
- peg_ratio_peer_count: 10
- price_to_book_percentile: N/A
- price_to_book_peer_count: 0

## Momentum

4点

理由

- 1M の対SPY超過リターンは -9.07pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -15.52pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -43.92pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -38.34pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.01 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -9.5361
- 3M: -11.9468
- 6M: -22.5708
- 1Y: -20.7382
- benchmark: SPY
- benchmark_returns: {'1M': -0.47, '3M': 3.58, '6M': 21.35, '1Y': 17.6}
- excess_returns: {'1M': -9.07, '3M': -15.52, '6M': -43.92, '1Y': -38.34}
- latest_volume: 5,365,000.0000
- average_volume_30d: 5,326,076.6667

## News

0点

理由

- ニュースが取得できないため、News項目は評価を控えています。
- イベントDBが取得できないため、イベント項目は加点していません。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 0
- positive_count: 0
- negative_count: 0
- sentiment_net_ratio: N/A
- event_count: 0
- events_with_price_reaction: 0

欠損・計算不可

- news
- events

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
