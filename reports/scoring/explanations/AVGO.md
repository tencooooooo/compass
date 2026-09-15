# AVGO Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Broadcom Inc.
- Total Score: 56 / 100
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

- データが確認できた 100 点満点のうち 56 点を獲得し、シグナル充足率は 56.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 46.22% で、+30%以上の高成長です。
- eps_growth(直近4四半期平均) は 161.20% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +37.63pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +129.85pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 85.5000
- eps_yoy_growth: 215.2900
- revenue_yoy_growth_avg: 46.2200
- eps_yoy_growth_avg: 161.2000
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

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
- Forward PER はセクター内 40.00 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 6.67 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PBR はセクター内 86.67 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 43.3295
- forward_pe: 17.5027
- peg_ratio: 0.3400
- price_to_book: 16.2470
- sector_peer_count: 16
- trailing_pe_percentile: 85.7100
- trailing_pe_peer_count: 15
- forward_pe_percentile: 40.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 6.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 86.6700
- price_to_book_peer_count: 16

## Momentum

4点

理由

- 1M の対SPY超過リターンは -11.23pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -14.34pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -9.01pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -21.52pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.00 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -13.6696
- 3M: -13.7414
- 6M: 4.8011
- 1Y: -5.0335
- benchmark: SPY
- benchmark_returns: {'1M': -2.44, '3M': 0.6, '6M': 13.81, '1Y': 16.48}
- excess_returns: {'1M': -11.23, '3M': -14.34, '6M': -9.01, '1Y': -21.52}
- latest_volume: 23,370,886.0000
- average_volume_30d: 23,392,316.2000

## News

7点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 2 件(純比率 -0.33)で、センチメントは 2.7 点です。
- イベント後の平均株価反応が -1.58% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 2
- sentiment_net_ratio: -0.3300
- event_count: 10
- events_with_price_reaction: 7

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
