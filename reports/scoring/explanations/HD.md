# HD Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: The Home Depot, Inc.
- Total Score: 59 / 100
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

- データが確認できた 100 点満点のうち 59 点を獲得し、シグナル充足率は 59.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

12点

理由

- revenue_growth(直近4四半期平均) は 4.57% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 0.41% で、プラス成長を維持しています。
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
- revenue_yoy_growth: 4.9500
- eps_yoy_growth: 2.7600
- revenue_yoy_growth_avg: 4.5700
- eps_yoy_growth_avg: 0.4100
- revenue_growth_quarters: ['2026-Q4', '2026-Q3', '2026-Q2', '2025-Q4']
- eps_growth_quarters: ['2026-Q4', '2026-Q3', '2026-Q2', '2025-Q4']

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
- Forward PER はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR はセクター内 100.00 パーセンタイル / 母数 5 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 24.5618
- forward_pe: 22.5015
- peg_ratio: 239.5200
- price_to_book: 19.4656
- sector_peer_count: 10
- trailing_pe_percentile: 55.5600
- trailing_pe_peer_count: 10
- forward_pe_percentile: 33.3300
- forward_pe_peer_count: 10
- peg_ratio_percentile: 100
- peg_ratio_peer_count: 10
- price_to_book_percentile: 100
- price_to_book_peer_count: 5

## Momentum

16点

理由

- 1M の対SPY超過リターンが +16.83pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンが +12.35pt と、市場を大きく上回っています。
- 6M の対SPY超過リターンが +16.67pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -4.31pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 0.98 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 10.7427
- 3M: 6.4048
- 6M: 12.9366
- 1Y: 5.9379
- benchmark: SPY
- benchmark_returns: {'1M': -6.09, '3M': -5.94, '6M': -3.74, '1Y': 10.24}
- excess_returns: {'1M': 16.83, '3M': 12.35, '6M': 16.67, '1Y': -4.31}
- latest_volume: 4,841,500.0000
- average_volume_30d: 4,955,960.0000

## News

12点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 2 件(純比率 -0.33)で、センチメントは 2.7 点です。
- イベント後の平均株価反応が 2.13% とプラスです。

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
- events_with_price_reaction: 9

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
