# AAPL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Apple Inc.
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

17点

理由

- revenue_growth(直近4四半期平均) は 11.74% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 15.03% で、+15%以上の成長です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 416,161,000,000.0000
- eps: 7.4900
- net_income: 112,010,000,000.0000
- operating_income: 133,050,000,000.0000
- research_and_development: 34,550,000,000.0000
- revenue_yoy_growth: 16.6000
- eps_yoy_growth: 21.8200
- revenue_yoy_growth_avg: 11.7400
- eps_yoy_growth_avg: 15.0300
- revenue_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q4', '2025-Q2', '2025-Q1']

## Financial Health

12点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 3.87 倍で、負債負担の確認が必要です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 0.89 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 35,934,000,000.0000
- total_liabilities: 285,508,000,000.0000
- shareholders_equity: 73,733,000,000.0000
- long_term_debt: 78,328,000,000.0000
- current_ratio: 0.8933

## Valuation

3点

理由

- PER はセクター内 64.29 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 86.67 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PEG はセクター内 100.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- PBR はセクター内 100.00 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 40.2684
- forward_pe: 34.5412
- peg_ratio: 2.5900
- price_to_book: 45.8705
- sector_peer_count: 16
- trailing_pe_percentile: 64.2900
- trailing_pe_peer_count: 15
- forward_pe_percentile: 86.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 100
- peg_ratio_peer_count: 16
- price_to_book_percentile: 100
- price_to_book_peer_count: 16

## Momentum

13点

理由

- 1M の対SPY超過リターンが +12.85pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +17.33pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +26.52pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +38.32pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.80 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 13.6277
- 3M: 21.9057
- 6M: 34.3421
- 1Y: 56.1247
- benchmark: SPY
- benchmark_returns: {'1M': 0.78, '3M': 4.57, '6M': 7.82, '1Y': 17.8}
- excess_returns: {'1M': 12.85, '3M': 17.33, '6M': 26.52, '1Y': 38.32}
- latest_volume: 47,402,209.0000
- average_volume_30d: 59,327,700.3000

## News

14点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 3 件(純比率 +0.14)で、センチメントは 4.6 点です。
- イベント後の平均株価反応が 3.53% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 3
- sentiment_net_ratio: 0.1400
- event_count: 10
- events_with_price_reaction: 3

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
