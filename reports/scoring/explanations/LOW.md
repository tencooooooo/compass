# LOW Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Lowe's Companies, Inc.
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
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 58 点を獲得し、シグナル充足率は 58.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

8点

理由

- revenue_growth(直近4四半期平均) は 7.78% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は -0.22% で、前年同期比ではマイナスです。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 86,286,000,000.0000
- eps: 11.8700
- net_income: 6,654,000,000.0000
- operating_income: 10,153,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: 9.3400
- eps_yoy_growth: 3.4700
- revenue_yoy_growth_avg: 7.7800
- eps_yoy_growth_avg: -0.2200
- revenue_growth_quarters: ['2026-Q4', '2026-Q3', '2026-Q2', '2025-Q4']
- eps_growth_quarters: ['2026-Q4', '2026-Q3', '2026-Q2', '2025-Q4']

欠損・計算不可

- research_and_development

## Financial Health

9点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスではないため、財務健全性の加点を抑えています。
- 総負債は取得できていますが、自己資本との比較が不十分です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 1.08 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 982,000,000.0000
- total_liabilities: 64,061,000,000.0000
- shareholders_equity: -9,917,000,000.0000
- long_term_debt: 37,490,000,000.0000
- current_ratio: 1.0767

## Valuation

10点

理由

- PER はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- Forward PER はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PEG はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR は -20.70 で、指標がマイナスのため加点対象外です。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 19.8372
- forward_pe: 18.5704
- peg_ratio: 29.9900
- price_to_book: -20.7022
- sector_peer_count: 10
- trailing_pe_percentile: 22.2200
- trailing_pe_peer_count: 10
- forward_pe_percentile: 11.1100
- forward_pe_peer_count: 10
- peg_ratio_percentile: 77.7800
- peg_ratio_peer_count: 10
- price_to_book_percentile: N/A
- price_to_book_peer_count: 0

## Momentum

14点

理由

- 1M の対SPY超過リターンが +24.88pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +19.47pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +14.93pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -7.57pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 0.31 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 19.1835
- 3M: 14.3755
- 6M: 11.6948
- 1Y: 1.4946
- benchmark: SPY
- benchmark_returns: {'1M': -5.7, '3M': -5.1, '6M': -3.23, '1Y': 9.06}
- excess_returns: {'1M': 24.88, '3M': 19.47, '6M': 14.93, '1Y': -7.57}
- latest_volume: 1,068,300.0000
- average_volume_30d: 3,460,493.3333

## News

17点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が 1.74% とプラスです。

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
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
