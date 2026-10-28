# GOOGL Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Alphabet Inc.
- Total Score: 49 / 100
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

- データが確認できた 80 点満点のうち 49 点を獲得し、シグナル充足率は 61.2% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 18.94% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 108.46% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +212.52pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 402,836,000,000.0000
- eps: 10.9100
- net_income: 132,170,000,000.0000
- operating_income: 129,039,000,000.0000
- research_and_development: 61,087,000,000.0000
- revenue_yoy_growth: 24.2300
- eps_yoy_growth: 294.3700
- revenue_yoy_growth_avg: 18.9400
- eps_yoy_growth_avg: 108.4600
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

14点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債が取得できないため、負債項目は加点していません。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 2.01 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 30,708,000,000.0000
- total_liabilities: N/A
- shareholders_equity: 415,265,000,000.0000
- long_term_debt: 46,547,000,000.0000
- current_ratio: 2.0053

欠損・計算不可

- total_liabilities

## Valuation

6点

理由

- PER はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- Forward PER はセクター内 88.89 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 16.0853
- forward_pe: 20.8729
- peg_ratio: 1.1100
- price_to_book: 6.2987
- sector_peer_count: 10
- trailing_pe_percentile: 55.5600
- trailing_pe_peer_count: 10
- forward_pe_percentile: 88.8900
- forward_pe_peer_count: 10
- peg_ratio_percentile: 55.5600
- peg_ratio_peer_count: 10
- price_to_book_percentile: 77.7800
- price_to_book_peer_count: 10

## Momentum

9点

理由

- 1M の対SPY超過リターンは -7.11pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは -8.57pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -17.02pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンが +10.34pt と、市場を大きく上回っています。
- 直近出来高が30日平均の 0.96 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -7.8856
- 3M: -5.0063
- 6M: -9.4614
- 1Y: 25.5034
- benchmark: SPY
- benchmark_returns: {'1M': -0.78, '3M': 3.56, '6M': 7.56, '1Y': 15.16}
- excess_returns: {'1M': -7.11, '3M': -8.57, '6M': -17.02, '1Y': 10.34}
- latest_volume: 23,991,800.0000
- average_volume_30d: 24,897,650.0000

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
