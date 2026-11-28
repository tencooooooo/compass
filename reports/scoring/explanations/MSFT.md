# MSFT Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Microsoft Corporation
- Total Score: 73 / 100
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

- データが確認できた 100 点満点のうち 73 点を獲得し、シグナル充足率は 73.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 18.06% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 32.04% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +8.85pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 331,839,000,000.0000
- eps: 18.0000
- net_income: 133,749,000,000.0000
- operating_income: 155,237,000,000.0000
- research_and_development: 35,562,000,000.0000
- revenue_yoy_growth: 18.8000
- eps_yoy_growth: 32.2600
- revenue_yoy_growth_avg: 18.0600
- eps_yoy_growth_avg: 32.0400
- revenue_growth_quarters: ['2026-Q3', '2026-Q1', '2025-Q4', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q1', '2025-Q4', '2025-Q3']

## Financial Health

18点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.71 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.23 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 20,935,000,000.0000
- total_liabilities: 315,989,000,000.0000
- shareholders_equity: 442,387,000,000.0000
- long_term_debt: 31,067,000,000.0000
- current_ratio: 1.2303

## Valuation

12点

理由

- PER はセクター内 57.14 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 50.00 パーセンタイル / 母数 15 で、中位レンジです。
- PBR はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 25.7229
- forward_pe: 20.3625
- peg_ratio: 1.5600
- price_to_book: 7.7797
- sector_peer_count: 16
- trailing_pe_percentile: 57.1400
- trailing_pe_peer_count: 15
- forward_pe_percentile: 73.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 50.0000
- peg_ratio_peer_count: 15
- price_to_book_percentile: 53.3300
- price_to_book_peer_count: 16

## Momentum

10点

理由

- 1M の対SPY超過リターンは -1.31pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは +1.26pt で、市場並み以上です。
- 6M の対SPY超過リターンが +13.12pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -4.88pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 0.47 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -7.0070
- 3M: -3.8416
- 6M: 9.8818
- 1Y: 4.1814
- benchmark: SPY
- benchmark_returns: {'1M': -5.7, '3M': -5.1, '6M': -3.23, '1Y': 9.06}
- excess_returns: {'1M': -1.31, '3M': 1.26, '6M': 13.12, '1Y': -4.88}
- latest_volume: 12,489,400.0000
- average_volume_30d: 26,640,376.6667

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 1 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベント後の平均株価反応が 0.60% と中立圏です。

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
- events_with_price_reaction: 7

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
