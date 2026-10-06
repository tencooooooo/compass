# DIS Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: The Walt Disney Company
- Total Score: 40 / 100
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

- データが確認できた 80 点満点のうち 40 点を獲得し、シグナル充足率は 50.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

10点

理由

- revenue_growth(直近4四半期平均) は 5.17% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 5.45% で、プラス成長を維持しています。
- eps_growth は直近四半期が前四半期より -18.46pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 94,425,000,000.0000
- eps: 6.8800
- net_income: 12,404,000,000.0000
- operating_income: 13,832,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: 6.7600
- eps_yoy_growth: -48.2900
- revenue_yoy_growth_avg: 5.1700
- eps_yoy_growth_avg: 5.4500
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q4', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q4', '2025-Q2']

欠損・計算不可

- research_and_development

## Financial Health

16点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.75 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 0.71 で、短期支払余力は追加確認が必要です。

Evidence

- Financials
- Knowledge

使用データ

- cash: 5,695,000,000.0000
- total_liabilities: 82,902,000,000.0000
- shareholders_equity: 109,869,000,000.0000
- long_term_debt: 35,315,000,000.0000
- current_ratio: 0.7104

## Valuation

6点

理由

- PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- Forward PER はセクター内 55.56 パーセンタイル / 母数 10 で、中位レンジです。
- PEG はセクター内 88.89 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR はセクター内 33.33 パーセンタイル / 母数 10 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.3629
- forward_pe: 13.8414
- peg_ratio: 3.3300
- price_to_book: 1.6290
- sector_peer_count: 10
- trailing_pe_percentile: 77.7800
- trailing_pe_peer_count: 10
- forward_pe_percentile: 55.5600
- forward_pe_peer_count: 10
- peg_ratio_percentile: 88.8900
- peg_ratio_peer_count: 10
- price_to_book_percentile: 33.3300
- price_to_book_peer_count: 10

## Momentum

8点

理由

- 1M の対SPY超過リターンは -3.78pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは +2.40pt で、市場並み以上です。
- 6M の対SPY超過リターンは -9.75pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -23.30pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.84 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -3.3128
- 3M: 6.2885
- 6M: 8.4378
- 1Y: -6.2687
- benchmark: SPY
- benchmark_returns: {'1M': 0.46, '3M': 3.88, '6M': 18.18, '1Y': 17.03}
- excess_returns: {'1M': -3.78, '3M': 2.4, '6M': -9.75, '1Y': -23.3}
- latest_volume: 7,037,600.0000
- average_volume_30d: 8,398,186.6667

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
