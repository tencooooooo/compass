# META Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Meta Platforms, Inc.
- Total Score: 49 / 100
- Confidence: Medium
- Signal Strength: Moderate
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 4 領域です。
- 欠損または計算不可の項目数は 2 件です。
- データが不足している領域: News。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Moderate

理由

- データが確認できた 80 点満点のうち 49 点を獲得し、シグナル充足率は 61.2% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 27.22% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 1.17% で、プラス成長を維持しています。
- revenue_growth は直近四半期が前四半期より -5.12pt 低く、成長の減速に注意が必要です。
- eps_growth は直近四半期が前四半期より -75.81pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 200,966,000,000.0000
- eps: 23.9800
- net_income: 60,458,000,000.0000
- operating_income: 83,276,000,000.0000
- research_and_development: 57,372,000,000.0000
- revenue_yoy_growth: 27.9600
- eps_yoy_growth: -13.4500
- revenue_yoy_growth_avg: 27.2200
- eps_yoy_growth_avg: 1.1700
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.68 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.60 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 35,873,000,000.0000
- total_liabilities: 148,778,000,000.0000
- shareholders_equity: 217,243,000,000.0000
- long_term_debt: 58,744,000,000.0000
- current_ratio: 2.5988

## Valuation

3点

理由

- PER はセクター内 88.89 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- PBR はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 27.1624
- forward_pe: 20.8679
- peg_ratio: 0.9800
- price_to_book: 7.0317
- sector_peer_count: 10
- trailing_pe_percentile: 88.8900
- trailing_pe_peer_count: 10
- forward_pe_percentile: 77.7800
- forward_pe_peer_count: 10
- peg_ratio_percentile: 33.3300
- peg_ratio_peer_count: 10
- price_to_book_percentile: 77.7800
- price_to_book_peer_count: 10

## Momentum

9点

理由

- 1M の対SPY超過リターンは +8.60pt で、市場並み以上です。
- 3M の対SPY超過リターンは +5.04pt で、市場並み以上です。
- 6M の対SPY超過リターンは +0.51pt で、市場並み以上です。
- 1Y の対SPY超過リターンは -15.47pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.77 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 10.3671
- 3M: 7.8075
- 6M: 14.9171
- 1Y: 1.4382
- benchmark: SPY
- benchmark_returns: {'1M': 1.76, '3M': 2.77, '6M': 14.4, '1Y': 16.91}
- excess_returns: {'1M': 8.6, '3M': 5.04, '6M': 0.51, '1Y': -15.47}
- latest_volume: 16,008,000.0000
- average_volume_30d: 20,902,326.6667

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
