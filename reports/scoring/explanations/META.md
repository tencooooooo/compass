# META Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Meta Platforms, Inc.
- Total Score: 59 / 100
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

- データが確認できた 100 点満点のうち 59 点を獲得し、シグナル充足率は 59.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 28.34% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 57.77% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +278.21pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 26.0700
- eps_yoy_growth: 264.7600
- revenue_yoy_growth_avg: 28.3400
- eps_yoy_growth_avg: 57.7700
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

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

5点

理由

- PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PBR はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.4524
- forward_pe: 17.6681
- peg_ratio: 0.8300
- price_to_book: 5.9002
- sector_peer_count: 10
- trailing_pe_percentile: 77.7800
- trailing_pe_peer_count: 10
- forward_pe_percentile: 77.7800
- forward_pe_peer_count: 10
- peg_ratio_percentile: 22.2200
- peg_ratio_peer_count: 10
- price_to_book_percentile: 77.7800
- price_to_book_peer_count: 10

## Momentum

5点

理由

- 1M の対SPY超過リターンは -15.20pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは +7.84pt で、市場並み以上です。
- 6M の対SPY超過リターンは -0.73pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -12.84pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.72 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -17.5384
- 3M: 5.7644
- 6M: 2.1438
- 1Y: -0.1357
- benchmark: SPY
- benchmark_returns: {'1M': -2.34, '3M': -2.08, '6M': 2.88, '1Y': 12.7}
- excess_returns: {'1M': -15.2, '3M': 7.84, '6M': -0.73, '1Y': -12.84}
- latest_volume: 15,533,900.0000
- average_volume_30d: 21,534,626.6667

## News

9点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 1 件(純比率 +0.33)で、センチメントは 5.3 点です。
- イベント後の平均株価反応が -1.97% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 2
- negative_count: 1
- sentiment_net_ratio: 0.3300
- event_count: 10
- events_with_price_reaction: 4

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
