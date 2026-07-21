# AAPL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Apple Inc.
- Total Score: 58 / 100
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

- データが確認できた 100 点満点のうち 58 点を獲得し、シグナル充足率は 58.0% です。
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

- trailing_pe: 39.6780
- forward_pe: 34.0009
- peg_ratio: 2.6900
- price_to_book: 45.1433
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

12点

理由

- 1M の対SPY超過リターンは +9.77pt で、市場並み以上です。
- 3M の対SPY超過リターンが +14.29pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +19.74pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンが +35.26pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.66 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 9.9762
- 3M: 20.1399
- 6M: 28.4972
- 1Y: 55.8103
- benchmark: SPY
- benchmark_returns: {'1M': 0.21, '3M': 5.85, '6M': 8.76, '1Y': 20.55}
- excess_returns: {'1M': 9.77, '3M': 14.29, '6M': 19.74, '1Y': 35.26}
- latest_volume: 40,800,631.0000
- average_volume_30d: 61,771,501.0333

## News

14点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 5 件、悪材料 1 件(純比率 +0.67)で、センチメントは 6.7 点です。
- イベント後の平均株価反応が 0.35% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 5
- negative_count: 1
- sentiment_net_ratio: 0.6700
- event_count: 10
- events_with_price_reaction: 3

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
