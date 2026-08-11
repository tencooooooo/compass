# NVDA Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: NVIDIA Corporation
- Total Score: 63 / 100
- Confidence: Medium
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 1 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 100 点満点のうち 63 点を獲得し、シグナル充足率は 63.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

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

14点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債が取得できないため、負債項目は加点していません。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 3.91 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 10,605,000,000.0000
- total_liabilities: N/A
- shareholders_equity: 157,293,000,000.0000
- long_term_debt: 7,469,000,000.0000
- current_ratio: 3.9053

欠損・計算不可

- total_liabilities

## Valuation

11点

理由

- PER はセクター内 50.00 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 40.00 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 13.33 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PBR はセクター内 93.33 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 33.3078
- forward_pe: 16.8730
- peg_ratio: 0.6000
- price_to_book: 26.9517
- sector_peer_count: 16
- trailing_pe_percentile: 50.0000
- trailing_pe_peer_count: 15
- forward_pe_percentile: 40.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 13.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 93.3300
- price_to_book_peer_count: 16

## Momentum

8点

理由

- 1M の対SPY超過リターンは +4.01pt で、市場並み以上です。
- 3M の対SPY超過リターンは -5.27pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは +2.96pt で、市場並み以上です。
- 1Y の対SPY超過リターンは -3.07pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 0.74 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 6.8639
- 3M: -0.7685
- 6M: 14.5892
- 1Y: 19.2062
- benchmark: SPY
- benchmark_returns: {'1M': 2.86, '3M': 4.5, '6M': 11.63, '1Y': 22.27}
- excess_returns: {'1M': 4.01, '3M': -5.27, '6M': 2.96, '1Y': -3.07}
- latest_volume: 95,707,655.0000
- average_volume_30d: 129,058,421.8333

## News

10点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 2 件(純比率 -0.33)で、センチメントは 2.7 点です。
- イベント後の平均株価反応が -0.02% と中立圏です。

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
- events_with_price_reaction: 2

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
