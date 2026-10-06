# AVGO Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Broadcom Inc.
- Total Score: 54 / 100
- Confidence: Medium
- Signal Strength: Strong
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

Strong

理由

- データが確認できた 80 点満点のうち 54 点を獲得し、シグナル充足率は 67.5% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

20点

理由

- revenue_growth(直近4四半期平均) は 46.22% で、+30%以上の高成長です。
- eps_growth(直近4四半期平均) は 161.20% で、+30%以上の高成長です。
- revenue_growth は直近四半期が前四半期より +37.63pt 高く、成長の加速がみられます。
- eps_growth は直近四半期が前四半期より +129.85pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 63,887,000,000.0000
- eps: 4.9100
- net_income: 23,126,000,000.0000
- operating_income: 26,075,000,000.0000
- research_and_development: 10,977,000,000.0000
- revenue_yoy_growth: 85.5000
- eps_yoy_growth: 215.2900
- revenue_yoy_growth_avg: 46.2200
- eps_yoy_growth_avg: 161.2000
- revenue_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']
- eps_growth_quarters: ['2026-Q3', '2026-Q2', '2026-Q1', '2025-Q3']

## Financial Health

17点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.10 倍で、負債負担は中程度です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 1.71 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 16,178,000,000.0000
- total_liabilities: 89,800,000,000.0000
- shareholders_equity: 81,292,000,000.0000
- long_term_debt: 61,984,000,000.0000
- current_ratio: 1.7054

## Valuation

8点

理由

- PER はセクター内 78.57 パーセンタイル / 母数 15 で、相対的な加点は抑えています。
- Forward PER はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 13.33 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- PBR はセクター内 86.67 パーセンタイル / 母数 16 で、相対的な加点は抑えています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 46.2976
- forward_pe: 18.6920
- peg_ratio: 0.3500
- price_to_book: 17.3599
- sector_peer_count: 16
- trailing_pe_percentile: 78.5700
- trailing_pe_peer_count: 15
- forward_pe_percentile: 46.6700
- forward_pe_peer_count: 16
- peg_ratio_percentile: 13.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 86.6700
- price_to_book_peer_count: 16

## Momentum

9点

理由

- 1M の対SPY超過リターンは +1.22pt で、市場並み以上です。
- 3M の対SPY超過リターンは -5.94pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -2.50pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -9.04pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 0.85 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 1.6828
- 3M: -2.0524
- 6M: 15.6839
- 1Y: 7.9914
- benchmark: SPY
- benchmark_returns: {'1M': 0.46, '3M': 3.88, '6M': 18.18, '1Y': 17.03}
- excess_returns: {'1M': 1.22, '3M': -5.94, '6M': -2.5, '1Y': -9.04}
- latest_volume: 21,428,100.0000
- average_volume_30d: 25,213,286.6667

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
