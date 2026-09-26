# HD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: The Home Depot, Inc.
- Total Score: 43 / 100
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

- データが確認できた 100 点満点のうち 43 点を獲得し、シグナル充足率は 43.0% です。
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

6点

理由

- PER はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR はセクター内 100.00 パーセンタイル / 母数 5 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 20.5035
- forward_pe: 18.2966
- peg_ratio: 2.4700
- price_to_book: 17.6096
- sector_peer_count: 10
- trailing_pe_percentile: 55.5600
- trailing_pe_peer_count: 10
- forward_pe_percentile: 44.4400
- forward_pe_peer_count: 10
- peg_ratio_percentile: 77.7800
- peg_ratio_peer_count: 10
- price_to_book_percentile: 100
- price_to_book_peer_count: 5

## Momentum

4点

理由

- 1M の対SPY超過リターンは -13.30pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -19.42pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -28.21pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -43.81pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.66 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -12.8883
- 3M: -14.6860
- 6M: -10.8175
- 1Y: -26.8808
- benchmark: SPY
- benchmark_returns: {'1M': 0.41, '3M': 4.74, '6M': 17.39, '1Y': 16.92}
- excess_returns: {'1M': -13.3, '3M': -19.42, '6M': -28.21, '1Y': -43.81}
- latest_volume: 7,053,800.0000
- average_volume_30d: 4,262,026.6667

## News

10点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 1 件(純比率 +0.60)で、センチメントは 6.4 点です。
- イベント後の平均株価反応が -1.53% と弱く、注意が必要です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 1
- sentiment_net_ratio: 0.6000
- event_count: 10
- events_with_price_reaction: 4

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
