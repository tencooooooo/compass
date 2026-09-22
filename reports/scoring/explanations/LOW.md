# LOW Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Lowe's Companies, Inc.
- Total Score: 47 / 100
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

- データが確認できた 100 点満点のうち 47 点を獲得し、シグナル充足率は 47.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

8点

理由

- revenue_growth(直近4四半期平均) は 5.84% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は -0.49% で、前年同期比ではマイナスです。
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
- revenue_yoy_growth: 8.3400
- eps_yoy_growth: 0.0000
- revenue_yoy_growth_avg: 5.8400
- eps_yoy_growth_avg: -0.4900
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2025-Q4', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2025-Q4', '2025-Q3']

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

13点

理由

- PER はセクター内 0.00 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- Forward PER はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PEG はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PBR は -14.41 で、指標がマイナスのため加点対象外です。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 16.1301
- forward_pe: 14.6591
- peg_ratio: 2.2800
- price_to_book: -14.4060
- sector_peer_count: 10
- trailing_pe_percentile: 0
- trailing_pe_peer_count: 10
- forward_pe_percentile: 11.1100
- forward_pe_peer_count: 10
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 10
- price_to_book_percentile: N/A
- price_to_book_peer_count: 0

## Momentum

4点

理由

- 1M の対SPY超過リターンは -11.79pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -15.09pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -31.62pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -43.81pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.91 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -12.5045
- 3M: -12.8355
- 6M: -15.2804
- 1Y: -26.6862
- benchmark: SPY
- benchmark_returns: {'1M': -0.71, '3M': 2.26, '6M': 16.34, '1Y': 17.12}
- excess_returns: {'1M': -11.79, '3M': -15.09, '6M': -31.62, '1Y': -43.81}
- latest_volume: 5,881,200.0000
- average_volume_30d: 3,083,830.0000

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 1 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベント後の平均株価反応が -0.49% と中立圏です。

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
- events_with_price_reaction: 8

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
