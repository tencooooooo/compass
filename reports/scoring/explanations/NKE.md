# NKE Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: NIKE, Inc.
- Total Score: 55 / 100
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

- データが確認できた 100 点満点のうち 55 点を獲得し、シグナル充足率は 55.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

6点

理由

- revenue_growth(直近4四半期平均) は -0.63% で、前年同期比ではマイナスです。
- eps_growth(直近4四半期平均) は -24.82% で、前年同期比ではマイナスです。
- eps_growth は直近四半期が前四半期より +33.15pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 46,398,000,000.0000
- eps: 2.1000
- net_income: 3,108,000,000.0000
- operating_income: 3,797,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: -4.3300
- eps_yoy_growth: -2.0400
- revenue_yoy_growth_avg: -0.6300
- eps_yoy_growth_avg: -24.8200
- revenue_growth_quarters: ['2026-Q3', '2026-Q1', '2025-Q4', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q1', '2025-Q4', '2025-Q3']

欠損・計算不可

- research_and_development

## Financial Health

18点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.58 倍で、負債負担は中程度です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.96 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 7,563,000,000.0000
- total_liabilities: 23,545,000,000.0000
- shareholders_equity: 14,865,000,000.0000
- long_term_debt: 5,942,000,000.0000
- current_ratio: 1.9609

## Valuation

13点

理由

- PER はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- Forward PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 0.00 パーセンタイル / 母数 5 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 17.6250
- forward_pe: 26.3760
- peg_ratio: 5.5900
- price_to_book: 3.5721
- sector_peer_count: 10
- trailing_pe_percentile: 11.1100
- trailing_pe_peer_count: 10
- forward_pe_percentile: 77.7800
- forward_pe_peer_count: 10
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 10
- price_to_book_percentile: 0
- price_to_book_peer_count: 5

## Momentum

8点

理由

- 1M の対SPY超過リターンは +4.48pt で、市場並み以上です。
- 3M の対SPY超過リターンは +3.21pt で、市場並み以上です。
- 6M の対SPY超過リターンは -16.55pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -47.18pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.09 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -2.3962
- 3M: -3.6189
- 6M: -21.0884
- 1Y: -38.8523
- benchmark: SPY
- benchmark_returns: {'1M': -6.88, '3M': -6.82, '6M': -4.54, '1Y': 8.33}
- excess_returns: {'1M': 4.48, '3M': 3.21, '6M': -16.55, '1Y': -47.18}
- latest_volume: 27,945,300.0000
- average_volume_30d: 25,670,770.0000

## News

10点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 6 件(純比率 -0.71)で、センチメントは 1.2 点です。
- イベント後の平均株価反応が 2.55% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 6
- sentiment_net_ratio: -0.7100
- event_count: 10
- events_with_price_reaction: 8

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
