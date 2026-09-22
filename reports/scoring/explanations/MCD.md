# MCD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: McDonald's Corporation
- Total Score: 44 / 100
- Confidence: Medium
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 2 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 44 点を獲得し、シグナル充足率は 44.0% です。
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

9点

理由

- PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- PBR は -171.42 で、指標がマイナスのため加点対象外です。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 20.1365
- forward_pe: 17.7739
- peg_ratio: 2.1400
- price_to_book: -171.4246
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

5点

理由

- 1M の対SPY超過リターンは -5.81pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -12.52pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -35.04pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -33.63pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 2.11 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -6.5229
- 3M: -10.2672
- 6M: -18.6963
- 1Y: -16.5082
- benchmark: SPY
- benchmark_returns: {'1M': -0.71, '3M': 2.26, '6M': 16.34, '1Y': 17.12}
- excess_returns: {'1M': -5.81, '3M': -12.52, '6M': -35.04, '1Y': -33.63}
- latest_volume: 9,565,500.0000
- average_volume_30d: 4,544,120.0000

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 0

欠損・計算不可

- event_price_reaction

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
