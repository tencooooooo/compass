# MCD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: McDonald's Corporation
- Total Score: 52 / 100
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

- データが確認できた 100 点満点のうち 52 点を獲得し、シグナル充足率は 52.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

10点

理由

- revenue_growth(直近4四半期平均) は 4.32% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 6.16% で、プラス成長を維持しています。
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
- revenue_yoy_growth: 1.1200
- eps_yoy_growth: 10.3800
- revenue_yoy_growth_avg: 4.3200
- eps_yoy_growth_avg: 6.1600
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

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

8点

理由

- PER はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PEG はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR は -579.09 で、指標がマイナスのため加点対象外です。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.8849
- forward_pe: 20.5816
- peg_ratio: 2.9400
- price_to_book: -579.0947
- sector_peer_count: 10
- trailing_pe_percentile: 44.4400
- trailing_pe_peer_count: 10
- forward_pe_percentile: 22.2200
- forward_pe_peer_count: 10
- peg_ratio_percentile: 77.7800
- peg_ratio_peer_count: 10
- price_to_book_percentile: N/A
- price_to_book_peer_count: 0

## Momentum

12点

理由

- 1M の対SPY超過リターンが +22.97pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは +5.47pt で、市場並み以上です。
- 6M の対SPY超過リターンは +1.59pt で、市場並み以上です。
- 1Y の対SPY超過リターンは -16.76pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.85 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 19.6446
- 3M: 3.3888
- 6M: 3.9194
- 1Y: -3.2610
- benchmark: SPY
- benchmark_returns: {'1M': -3.32, '3M': -2.08, '6M': 2.33, '1Y': 13.5}
- excess_returns: {'1M': 22.97, '3M': 5.47, '6M': 1.59, '1Y': -16.76}
- latest_volume: 4,951,600.0000
- average_volume_30d: 5,828,586.6667

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 2 件(純比率 +0.43)で、センチメントは 5.7 点です。
- イベント後の平均株価反応が 1.78% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 5
- negative_count: 2
- sentiment_net_ratio: 0.4300
- event_count: 10
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
