# LOW Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Lowe's Companies, Inc.
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

8点

理由

- revenue_growth(直近4四半期平均) は 3.25% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は -1.64% で、前年同期比ではマイナスです。
- revenue_growth は直近四半期が前四半期より +7.07pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 10.2600
- eps_yoy_growth: -0.6800
- revenue_yoy_growth_avg: 3.2500
- eps_yoy_growth_avg: -1.6400
- revenue_growth_quarters: ['2026-Q2', '2025-Q4', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2025-Q4', '2025-Q3', '2025-Q2']

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
- Forward PER はセクター内 0.00 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PEG はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PBR は -13.06 で、指標がマイナスのため加点対象外です。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 18.2580
- forward_pe: 16.0777
- peg_ratio: 1.4300
- price_to_book: -13.0604
- sector_peer_count: 10
- trailing_pe_percentile: 0
- trailing_pe_peer_count: 10
- forward_pe_percentile: 0
- forward_pe_peer_count: 10
- peg_ratio_percentile: 33.3300
- peg_ratio_peer_count: 10
- price_to_book_percentile: N/A
- price_to_book_peer_count: 0

## Momentum

7点

理由

- 1M の対SPY超過リターンは +0.08pt で、市場並み以上です。
- 3M の対SPY超過リターンは -5.39pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -38.02pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -34.09pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.84 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 4.0309
- 3M: -0.5843
- 6M: -24.0802
- 1Y: -12.9644
- benchmark: SPY
- benchmark_returns: {'1M': 3.95, '3M': 4.8, '6M': 13.94, '1Y': 21.13}
- excess_returns: {'1M': 0.08, '3M': -5.39, '6M': -38.02, '1Y': -34.09}
- latest_volume: 2,390,629.0000
- average_volume_30d: 2,858,690.9667

## News

4点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 0 件、悪材料 2 件(純比率 -1.00)で、センチメントは 0.0 点です。
- イベント後の平均株価反応が -1.22% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 0
- negative_count: 2
- sentiment_net_ratio: -1.0000
- event_count: 10
- events_with_price_reaction: 9

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
