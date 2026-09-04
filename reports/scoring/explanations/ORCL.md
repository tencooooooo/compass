# ORCL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Oracle Corporation
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

17点

理由

- revenue_growth(直近4四半期平均) は 13.61% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 33.37% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +7.44pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より -66.40pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 67,357,000,000.0000
- eps: 5.9400
- net_income: 17,087,000,000.0000
- operating_income: 22,444,000,000.0000
- research_and_development: 10,272,000,000.0000
- revenue_yoy_growth: 21.6600
- eps_yoy_growth: 24.5100
- revenue_yoy_growth_avg: 13.6100
- eps_yoy_growth_avg: 33.3700
- revenue_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q3', '2025-Q1']

## Financial Health

13点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 5.14 倍で、負債負担の確認が必要です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 1.12 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 31,289,000,000.0000
- total_liabilities: 218,703,000,000.0000
- shareholders_equity: 42,508,000,000.0000
- long_term_debt: 122,342,000,000.0000
- current_ratio: 1.1150

## Valuation

14点

理由

- PER はセクター内 35.71 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PEG はセクター内 43.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 66.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 27.2818
- forward_pe: 14.4771
- peg_ratio: 0.8700
- price_to_book: 12.1764
- sector_peer_count: 16
- trailing_pe_percentile: 35.7100
- trailing_pe_peer_count: 15
- forward_pe_percentile: 20.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 43.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 66.6700
- price_to_book_peer_count: 16

## Momentum

7点

理由

- 1M の対SPY超過リターンが +10.46pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -30.13pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -10.63pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -47.95pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.99 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 10.6712
- 3M: -25.4341
- 6M: 4.5299
- 1Y: -27.9867
- benchmark: SPY
- benchmark_returns: {'1M': 0.21, '3M': 4.69, '6M': 15.16, '1Y': 19.97}
- excess_returns: {'1M': 10.46, '3M': -30.13, '6M': -10.63, '1Y': -47.95}
- latest_volume: 26,162,395.0000
- average_volume_30d: 26,348,516.5000

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 2 件(純比率 +0.00)で、センチメントは 4.0 点です。
- イベント後の平均株価反応が 3.08% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 2
- negative_count: 2
- sentiment_net_ratio: 0.0000
- event_count: 10
- events_with_price_reaction: 6

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
