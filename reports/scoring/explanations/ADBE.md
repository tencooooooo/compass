# ADBE Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Adobe Inc.
- Total Score: 66 / 100
- Confidence: High
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 100 点満点のうち 66 点を獲得し、シグナル充足率は 66.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

14点

理由

- revenue_growth(直近4四半期平均) は 12.07% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 10.17% で、プラス成長を維持しています。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 23,769,000,000.0000
- eps: 16.7300
- net_income: 7,130,000,000.0000
- operating_income: 8,706,000,000.0000
- research_and_development: 4,294,000,000.0000
- revenue_yoy_growth: 12.8900
- eps_yoy_growth: 10.5300
- revenue_yoy_growth_avg: 12.0700
- eps_yoy_growth_avg: 10.1700
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

## Financial Health

14点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.54 倍で、負債負担は中程度です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.00 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 5,431,000,000.0000
- total_liabilities: 17,873,000,000.0000
- shareholders_equity: 11,623,000,000.0000
- long_term_debt: 6,210,000,000.0000
- current_ratio: 0.9964

## Valuation

18点

理由

- PER はセクター内 0.00 パーセンタイル / 母数 15 で、相対的に割安寄りです。
- Forward PER はセクター内 6.67 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PEG はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PBR はセクター内 26.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 13.4314
- forward_pe: 8.6976
- peg_ratio: 0.5800
- price_to_book: 8.0817
- sector_peer_count: 16
- trailing_pe_percentile: 0
- trailing_pe_peer_count: 15
- forward_pe_percentile: 6.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 20.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 26.6700
- price_to_book_peer_count: 16

## Momentum

8点

理由

- 1M の対SPY超過リターンは -14.71pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンが +14.99pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンは -22.39pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -52.67pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.42 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -13.4580
- 3M: 20.6757
- 6M: -3.7918
- 1Y: -34.8866
- benchmark: SPY
- benchmark_returns: {'1M': 1.25, '3M': 5.69, '6M': 18.6, '1Y': 17.78}
- excess_returns: {'1M': -14.71, '3M': 14.99, '6M': -22.39, '1Y': -52.67}
- latest_volume: 7,368,200.0000
- average_volume_30d: 5,202,820.0000

## News

12点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が -4.52% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 2
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 2

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
