# HD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: The Home Depot, Inc.
- Total Score: 50 / 100
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

- データが確認できた 100 点満点のうち 50 点を獲得し、シグナル充足率は 50.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

10点

理由

- revenue_growth(直近4四半期平均) は 4.55% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は -0.39% で、前年同期比ではマイナスです。
- eps_growth は直近四半期が前四半期より +8.94pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 164,683,000,000.0000
- eps: 14.2600
- net_income: 14,156,000,000.0000
- operating_income: 20,890,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: 5.7100
- eps_yoy_growth: 4.5900
- revenue_yoy_growth_avg: 4.5500
- eps_yoy_growth_avg: -0.3900
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2025-Q4', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2025-Q4', '2025-Q3']

欠損・計算不可

- research_and_development

## Financial Health

13点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 7.20 倍で、負債負担の確認が必要です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 1.06 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 1,389,000,000.0000
- total_liabilities: 92,282,000,000.0000
- shareholders_equity: 12,813,000,000.0000
- long_term_debt: 46,341,000,000.0000
- current_ratio: 1.0607

## Valuation

9点

理由

- PER はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 66.67 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 100.00 パーセンタイル / 母数 5 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 22.4825
- forward_pe: 20.0184
- peg_ratio: 1.7700
- price_to_book: 19.2823
- sector_peer_count: 10
- trailing_pe_percentile: 55.5600
- trailing_pe_peer_count: 10
- forward_pe_percentile: 44.4400
- forward_pe_peer_count: 10
- peg_ratio_percentile: 66.6700
- peg_ratio_peer_count: 10
- price_to_book_percentile: 100
- price_to_book_peer_count: 5

## Momentum

3点

理由

- 1M の対SPY超過リターンは -7.68pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -0.63pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -23.51pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -39.77pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.60 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -7.4686
- 3M: 4.0659
- 6M: -8.3538
- 1Y: -19.8082
- benchmark: SPY
- benchmark_returns: {'1M': 0.21, '3M': 4.69, '6M': 15.16, '1Y': 19.97}
- excess_returns: {'1M': -7.68, '3M': -0.63, '6M': -23.51, '1Y': -39.77}
- latest_volume: 2,259,444.0000
- average_volume_30d: 3,753,671.4667

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が 0.49% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 3
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 9

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
