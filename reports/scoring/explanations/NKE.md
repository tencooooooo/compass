# NKE Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: NIKE, Inc.
- Total Score: 56 / 100
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

- データが確認できた 100 点満点のうち 56 点を獲得し、シグナル充足率は 56.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

6点

理由

- revenue_growth(直近4四半期平均) は -1.88% で、前年同期比ではマイナスです。
- eps_growth(直近4四半期平均) は -31.78% で、前年同期比ではマイナスです。
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
- revenue_yoy_growth: 0.0900
- eps_yoy_growth: -35.1900
- revenue_yoy_growth_avg: -1.8800
- eps_yoy_growth_avg: -31.7800
- revenue_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']

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

18点

理由

- PER はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- Forward PER はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PEG はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 0.00 パーセンタイル / 母数 5 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 19.5476
- forward_pe: 17.8735
- peg_ratio: 1.5100
- price_to_book: 4.0952
- sector_peer_count: 10
- trailing_pe_percentile: 11.1100
- trailing_pe_peer_count: 10
- forward_pe_percentile: 22.2200
- forward_pe_peer_count: 10
- peg_ratio_percentile: 44.4400
- peg_ratio_peer_count: 10
- price_to_book_percentile: 0
- price_to_book_peer_count: 5

## Momentum

5点

理由

- 1M の対SPY超過リターンは -7.22pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -7.45pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -49.05pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -66.40pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.81 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -4.4460
- 3M: -2.3637
- 6M: -36.3963
- 1Y: -45.5296
- benchmark: SPY
- benchmark_returns: {'1M': 2.78, '3M': 5.09, '6M': 12.66, '1Y': 20.87}
- excess_returns: {'1M': -7.22, '3M': -7.45, '6M': -49.05, '1Y': -66.4}
- latest_volume: 17,413,960.0000
- average_volume_30d: 21,603,812.0000

## News

9点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 0 件、悪材料 3 件(純比率 -1.00)で、センチメントは 0.0 点です。
- イベント後の平均株価反応が 2.47% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 0
- negative_count: 3
- sentiment_net_ratio: -1.0000
- event_count: 10
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
