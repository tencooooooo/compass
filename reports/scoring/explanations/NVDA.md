# NVDA Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: NVIDIA Corporation
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

20点

理由

- revenue_growth(直近4四半期平均) は 68.12% で、+30%以上の高成長です。
- eps_growth(直近4四半期平均) は 92.25% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +22.74pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +147.80pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 215,938,000,000.0000
- eps: 4.9300
- net_income: 120,067,000,000.0000
- operating_income: 130,387,000,000.0000
- research_and_development: 18,497,000,000.0000
- revenue_yoy_growth: 85.2300
- eps_yoy_growth: 214.4700
- revenue_yoy_growth_avg: 68.1200
- eps_yoy_growth_avg: 92.2500
- revenue_growth_quarters: ['2026-Q2', '2025-Q4', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2025-Q4', '2025-Q3', '2025-Q2']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.31 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 3.91 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 10,605,000,000.0000
- total_liabilities: 49,510,000,000.0000
- shareholders_equity: 157,293,000,000.0000
- long_term_debt: 7,469,000,000.0000
- current_ratio: 3.9053

## Valuation

11点

理由

- PER はセクター内 50.00 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 40.00 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PBR はセクター内 93.33 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 31.1302
- forward_pe: 15.8273
- peg_ratio: 0.5600
- price_to_book: 25.1896
- sector_peer_count: 16
- trailing_pe_percentile: 50.0000
- trailing_pe_peer_count: 15
- forward_pe_percentile: 40.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 20.0000
- peg_ratio_peer_count: 16
- price_to_book_percentile: 93.3300
- price_to_book_peer_count: 16

## Momentum

6点

理由

- 1M の対SPY超過リターンは -1.08pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -3.86pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは +1.04pt で、市場並み以上です。
- 1Y の対SPY超過リターンは -1.81pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 0.61 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -0.6694
- 3M: 0.9108
- 6M: 8.8094
- 1Y: 17.6594
- benchmark: SPY
- benchmark_returns: {'1M': 0.41, '3M': 4.77, '6M': 7.77, '1Y': 19.47}
- excess_returns: {'1M': -1.08, '3M': -3.86, '6M': 1.04, '1Y': -1.81}
- latest_volume: 88,271,631.0000
- average_volume_30d: 145,443,011.0333

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 1 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベント後の平均株価反応が 0.23% と中立圏です。

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
- events_with_price_reaction: 2

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
