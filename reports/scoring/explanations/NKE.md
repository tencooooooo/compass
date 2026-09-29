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
- 欠損または計算不可の項目数は 2 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 55 点を獲得し、シグナル充足率は 55.0% です。
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

20点

理由

- PER はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- Forward PER はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PEG はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PBR はセクター内 0.00 パーセンタイル / 母数 5 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 17.3286
- forward_pe: 16.7574
- peg_ratio: 1.4000
- price_to_book: 3.6303
- sector_peer_count: 10
- trailing_pe_percentile: 11.1100
- trailing_pe_peer_count: 10
- forward_pe_percentile: 22.2200
- forward_pe_peer_count: 10
- peg_ratio_percentile: 22.2200
- peg_ratio_peer_count: 10
- price_to_book_percentile: 0
- price_to_book_peer_count: 5

## Momentum

4点

理由

- 1M の対SPY超過リターンは -7.31pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -17.41pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -50.17pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -66.08pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.20 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -6.3767
- 3M: -11.3393
- 6M: -29.9932
- 1Y: -48.1483
- benchmark: SPY
- benchmark_returns: {'1M': 0.94, '3M': 6.07, '6M': 20.18, '1Y': 17.94}
- excess_returns: {'1M': -7.31, '3M': -17.41, '6M': -50.17, '1Y': -66.08}
- latest_volume: 38,219,700.0000
- average_volume_30d: 31,960,053.3333

## News

7点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 3 件(純比率 -0.50)で、センチメントは 2.0 点です。
- イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 3
- sentiment_net_ratio: -0.5000
- event_count: 10
- events_with_price_reaction: 0

欠損・計算不可

- event_price_reaction

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
