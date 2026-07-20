# MSFT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Microsoft Corporation
- Total Score: 68 / 100
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

- データが確認できた 100 点満点のうち 68 点を獲得し、シグナル充足率は 68.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

18点

理由

- revenue_growth(直近4四半期平均) は 16.68% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 28.39% で、+15%以上の成長です。
- eps_growth は直近四半期が前四半期より -36.34pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 281,724,000,000.0000
- eps: 13.7000
- net_income: 101,832,000,000.0000
- operating_income: 128,528,000,000.0000
- research_and_development: 32,488,000,000.0000
- revenue_yoy_growth: 18.3000
- eps_yoy_growth: 23.4100
- revenue_yoy_growth_avg: 16.6800
- eps_yoy_growth_avg: 28.3900
- revenue_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']

## Financial Health

18点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.80 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.35 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 30,242,000,000.0000
- total_liabilities: 275,524,000,000.0000
- shareholders_equity: 343,479,000,000.0000
- long_term_debt: 40,152,000,000.0000
- current_ratio: 1.3534

## Valuation

12点

理由

- PER はセクター内 42.86 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 26.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 23.9744
- forward_pe: 20.7569
- peg_ratio: 1.2100
- price_to_book: 7.2125
- sector_peer_count: 16
- trailing_pe_percentile: 42.8600
- trailing_pe_peer_count: 15
- forward_pe_percentile: 53.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 26.6700
- price_to_book_peer_count: 16

## Momentum

4点

理由

- 1M の対SPY超過リターンは +5.76pt で、市場並み以上です。
- 3M の対SPY超過リターンは -9.41pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -19.28pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -40.22pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.65 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 6.1703
- 3M: -4.6427
- 6M: -11.5137
- 1Y: -20.7537
- benchmark: SPY
- benchmark_returns: {'1M': 0.41, '3M': 4.77, '6M': 7.77, '1Y': 19.47}
- excess_returns: {'1M': 5.76, '3M': -9.41, '6M': -19.28, '1Y': -40.22}
- latest_volume: 27,729,614.0000
- average_volume_30d: 42,912,823.8000

## News

16点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 6 件、悪材料 1 件(純比率 +0.71)で、センチメントは 6.8 点です。
- イベント後の平均株価反応が 2.15% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 6
- negative_count: 1
- sentiment_net_ratio: 0.7100
- event_count: 10
- events_with_price_reaction: 3

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
