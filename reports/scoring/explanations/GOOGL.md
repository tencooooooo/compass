# GOOGL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Alphabet Inc.
- Total Score: 64 / 100
- Confidence: High
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 64 点を獲得し、シグナル充足率は 64.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 15.89% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 47.03% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +5.84pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +46.47pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 402,836,000,000.0000
- eps: 10.9100
- net_income: 132,170,000,000.0000
- operating_income: 129,039,000,000.0000
- research_and_development: 61,087,000,000.0000
- revenue_yoy_growth: 21.7900
- eps_yoy_growth: 81.8500
- revenue_yoy_growth_avg: 15.8900
- eps_yoy_growth_avg: 47.0300
- revenue_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.43 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.01 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 30,708,000,000.0000
- total_liabilities: 180,016,000,000.0000
- shareholders_equity: 415,265,000,000.0000
- long_term_debt: 46,547,000,000.0000
- current_ratio: 2.0053

## Valuation

3点

理由

- PER はセクター内 88.89 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 88.89 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 26.8490
- forward_pe: 24.0284
- peg_ratio: 1.3700
- price_to_book: 8.9080
- sector_peer_count: 10
- trailing_pe_percentile: 88.8900
- trailing_pe_peer_count: 10
- forward_pe_percentile: 100
- forward_pe_peer_count: 10
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 10
- price_to_book_percentile: 88.8900
- price_to_book_peer_count: 10

## Momentum

7点

理由

- 1M の対SPY超過リターンは -3.65pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -1.69pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -1.86pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンが +72.81pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.74 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -3.2436
- 3M: 3.0790
- 6M: 5.9103
- 1Y: 92.2835
- benchmark: SPY
- benchmark_returns: {'1M': 0.41, '3M': 4.77, '6M': 7.77, '1Y': 19.47}
- excess_returns: {'1M': -3.65, '3M': -1.69, '6M': -1.86, '1Y': 72.81}
- latest_volume: 24,606,836.0000
- average_volume_30d: 33,213,917.8667

## News

14点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 2 件(純比率 +0.33)で、センチメントは 5.3 点です。
- イベント後の平均株価反応が 1.51% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 2
- sentiment_net_ratio: 0.3300
- event_count: 10
- events_with_price_reaction: 6

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
