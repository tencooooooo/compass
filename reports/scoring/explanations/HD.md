# HD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: The Home Depot, Inc.
- Total Score: 38 / 100
- Confidence: Medium
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 4 領域です。
- 欠損または計算不可の項目数は 3 件です。
- データが不足している領域: News。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 80 点満点のうち 38 点を獲得し、シグナル充足率は 47.5% です。
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

12点

理由

- PER はセクター内 44.44 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 50.00 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 75.00 パーセンタイル / 母数 5 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 20.0623
- forward_pe: 17.8904
- peg_ratio: 1.4900
- price_to_book: 17.2186
- sector_peer_count: 10
- trailing_pe_percentile: 44.4400
- trailing_pe_peer_count: 10
- forward_pe_percentile: 33.3300
- forward_pe_peer_count: 10
- peg_ratio_percentile: 50.0000
- peg_ratio_peer_count: 10
- price_to_book_percentile: 75.0000
- price_to_book_peer_count: 5

## Momentum

3点

理由

- 1M の対SPY超過リターンは -12.11pt と、市場を大きく下回っています。
- 3M の対SPY超過リターンは -18.88pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは -27.50pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -43.05pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.97 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -10.7024
- 3M: -14.1005
- 6M: -8.7214
- 1Y: -25.3762
- benchmark: SPY
- benchmark_returns: {'1M': 1.41, '3M': 4.78, '6M': 18.78, '1Y': 17.68}
- excess_returns: {'1M': -12.11, '3M': -18.88, '6M': -27.5, '1Y': -43.05}
- latest_volume: 4,502,100.0000
- average_volume_30d: 4,631,190.0000

## News

0点

理由

- ニュースが取得できないため、News項目は評価を控えています。
- イベントDBが取得できないため、イベント項目は加点していません。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 0
- positive_count: 0
- negative_count: 0
- sentiment_net_ratio: N/A
- event_count: 0
- events_with_price_reaction: 0

欠損・計算不可

- news
- events

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
