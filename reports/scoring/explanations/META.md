# META Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Meta Platforms, Inc.
- Total Score: 70 / 100
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

- データが確認できた 100 点満点のうち 70 点を獲得し、シグナル充足率は 70.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 27.22% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 1.17% で、プラス成長を維持しています。
- revenue_growth は直近四半期が前四半期より -5.12pt 低く、成長の減速に注意が必要です。
- eps_growth は直近四半期が前四半期より -75.81pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 200,966,000,000.0000
- eps: 23.9800
- net_income: 60,458,000,000.0000
- operating_income: 83,276,000,000.0000
- research_and_development: 57,372,000,000.0000
- revenue_yoy_growth: 27.9600
- eps_yoy_growth: -13.4500
- revenue_yoy_growth_avg: 27.2200
- eps_yoy_growth_avg: 1.1700
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.68 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.60 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 35,873,000,000.0000
- total_liabilities: 148,778,000,000.0000
- shareholders_equity: 217,243,000,000.0000
- long_term_debt: 58,744,000,000.0000
- current_ratio: 2.5988

## Valuation

14点

理由

- PER はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PBR はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.7628
- forward_pe: 16.5931
- peg_ratio: 0.8500
- price_to_book: 5.6381
- sector_peer_count: 10
- trailing_pe_percentile: 66.6700
- trailing_pe_peer_count: 10
- forward_pe_percentile: 66.6700
- forward_pe_peer_count: 10
- peg_ratio_percentile: 11.1100
- peg_ratio_peer_count: 10
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 10

## Momentum

6点

理由

- 1M の対SPY超過リターンは +3.50pt で、市場並み以上です。
- 3M の対SPY超過リターンは -10.49pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -23.41pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -42.70pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.95 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 7.2334
- 3M: -8.5302
- 6M: -10.6651
- 1Y: -22.4070
- benchmark: SPY
- benchmark_returns: {'1M': 3.73, '3M': 1.96, '6M': 12.75, '1Y': 20.3}
- excess_returns: {'1M': 3.5, '3M': -10.49, '6M': -23.41, '1Y': -42.7}
- latest_volume: 15,573,685.0000
- average_volume_30d: 16,318,512.8333

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 3 件(純比率 +0.00)で、センチメントは 4.0 点です。
- イベント後の平均株価反応が 1.21% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 3
- negative_count: 3
- sentiment_net_ratio: 0.0000
- event_count: 10
- events_with_price_reaction: 4

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
