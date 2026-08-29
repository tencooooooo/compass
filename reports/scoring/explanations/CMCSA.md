# CMCSA Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Comcast Corporation
- Total Score: 64 / 100
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

- データが確認できた 100 点満点のうち 64 点を獲得し、シグナル充足率は 64.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

13点

理由

- revenue_growth(直近4四半期平均) は 0.85% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 23.59% で、+15%以上の成長です。
- revenue_growth は直近四半期が前四半期より -6.48pt 低く、成長の減速に注意が必要です。
- eps_growth は直近四半期が前四半期より -34.20pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 123,707,000,000.0000
- eps: 5.5485
- net_income: 19,998,000,000.0000
- operating_income: 20,670,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: -1.2300
- eps_yoy_growth: -66.7800
- revenue_yoy_growth_avg: 0.8500
- eps_yoy_growth_avg: 23.5900
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

欠損・計算不可

- research_and_development

## Financial Health

13点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.81 倍で、負債負担は中程度です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 0.88 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 9,481,000,000.0000
- total_liabilities: 175,255,000,000.0000
- shareholders_equity: 96,903,000,000.0000
- long_term_debt: 92,979,000,000.0000
- current_ratio: 0.8820

## Valuation

15点

理由

- PER はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- Forward PER はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PEG はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR はセクター内 0.00 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 8.6731
- forward_pe: 7.4705
- peg_ratio: 142.9800
- price_to_book: 1.0691
- sector_peer_count: 10
- trailing_pe_percentile: 22.2200
- trailing_pe_peer_count: 10
- forward_pe_percentile: 11.1100
- forward_pe_peer_count: 10
- peg_ratio_percentile: 100
- peg_ratio_peer_count: 10
- price_to_book_percentile: 0
- price_to_book_peer_count: 10

## Momentum

8点

理由

- 1M の対SPY超過リターンが +10.59pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは +8.32pt で、市場並み以上です。
- 6M の対SPY超過リターンは -23.12pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -30.76pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.75 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 14.3219
- 3M: 10.2883
- 6M: -10.3759
- 1Y: -10.4651
- benchmark: SPY
- benchmark_returns: {'1M': 3.73, '3M': 1.96, '6M': 12.75, '1Y': 20.3}
- excess_returns: {'1M': 10.59, '3M': 8.32, '6M': -23.12, '1Y': -30.76}
- latest_volume: 20,584,595.0000
- average_volume_30d: 27,565,069.8333

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 6 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が -0.52% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 6
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 10

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
