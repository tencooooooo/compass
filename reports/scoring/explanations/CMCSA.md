# CMCSA Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Comcast Corporation
- Total Score: 44 / 100
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

- データが確認できた 80 点満点のうち 44 点を獲得し、シグナル充足率は 55.0% です。
- シグナル強度は Moderate(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

8点

理由

- revenue_growth(直近4四半期平均) は -1.20% で、前年同期比ではマイナスです。
- eps_growth(直近4四半期平均) は -23.96% で、前年同期比ではマイナスです。
- eps_growth は直近四半期が前四半期より +74.56pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: -6.0900
- eps_yoy_growth: 7.7800
- revenue_yoy_growth_avg: -1.2000
- eps_yoy_growth_avg: -23.9600
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

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

- PER はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- Forward PER はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PEG はセクター内 100.00 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PBR はセクター内 11.11 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 7.3677
- forward_pe: 6.3976
- peg_ratio: 142.9800
- price_to_book: 0.8495
- sector_peer_count: 10
- trailing_pe_percentile: 11.1100
- trailing_pe_peer_count: 10
- forward_pe_percentile: 11.1100
- forward_pe_peer_count: 10
- peg_ratio_percentile: 100
- peg_ratio_peer_count: 10
- price_to_book_percentile: 11.1100
- price_to_book_peer_count: 10

## Momentum

8点

理由

- 1M の対SPY超過リターンは +0.05pt で、市場並み以上です。
- 3M の対SPY超過リターンは -2.69pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -31.86pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -32.47pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.26 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 0.0143
- 3M: 2.2957
- 6M: -22.6124
- 1Y: -16.0597
- benchmark: SPY
- benchmark_returns: {'1M': -0.04, '3M': 4.99, '6M': 9.25, '1Y': 16.41}
- excess_returns: {'1M': 0.05, '3M': -2.69, '6M': -31.86, '1Y': -32.47}
- latest_volume: 40,201,400.0000
- average_volume_30d: 31,819,250.0000

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
