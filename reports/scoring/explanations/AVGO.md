# AVGO Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Broadcom Inc.
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

19点

理由

- revenue_growth(直近4四半期平均) は 29.88% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 140.90% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +18.40pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +53.86pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 63,887,000,000.0000
- eps: 4.9100
- net_income: 23,126,000,000.0000
- operating_income: 26,075,000,000.0000
- research_and_development: 10,977,000,000.0000
- revenue_yoy_growth: 47.8700
- eps_yoy_growth: 85.4400
- revenue_yoy_growth_avg: 29.8800
- eps_yoy_growth_avg: 140.9000
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

17点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.10 倍で、負債負担は中程度です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 1.71 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 16,178,000,000.0000
- total_liabilities: 89,800,000,000.0000
- shareholders_equity: 81,292,000,000.0000
- long_term_debt: 61,984,000,000.0000
- current_ratio: 1.7054

## Valuation

8点

理由

- PER はセクター内 85.71 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 6.67 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PBR はセクター内 86.67 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 60.9022
- forward_pe: 18.7628
- peg_ratio: 0.4200
- price_to_book: 19.9262
- sector_peer_count: 16
- trailing_pe_percentile: 85.7100
- trailing_pe_peer_count: 15
- forward_pe_percentile: 46.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 6.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 86.6700
- price_to_book_peer_count: 16

## Momentum

9点

理由

- 1M の対SPY超過リターンは -11.38pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -24.96pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは +3.81pt で、市場並み以上です。
- 1Y の対SPY超過リターンは +3.21pt で、市場並み以上です。
- 直近出来高が30日平均の 1.55 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -12.1772
- 3M: -23.2475
- 6M: 16.0813
- 1Y: 24.0379
- benchmark: SPY
- benchmark_returns: {'1M': -0.8, '3M': 1.71, '6M': 12.27, '1Y': 20.83}
- excess_returns: {'1M': -11.38, '3M': -24.96, '6M': 3.81, '1Y': 3.21}
- latest_volume: 30,822,042.0000
- average_volume_30d: 19,869,398.0667

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 1 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベント後の平均株価反応が -0.66% と中立圏です。

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
- events_with_price_reaction: 1

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
