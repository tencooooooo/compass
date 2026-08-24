# AMZN Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Amazon.com, Inc.
- Total Score: 72 / 100
- Confidence: Medium
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 1 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 100 点満点のうち 72 点を獲得し、シグナル充足率は 72.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

16点

理由

- revenue_growth(直近4四半期平均) は 15.74% で、+15%以上の成長です。
- eps_growth(直近4四半期平均) は 96.70% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +167.42pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が取得できないため、R&D項目は加点していません。
- 売上規模が大きく、事業規模の強さが確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 716,924,000,000.0000
- eps: 7.2900
- net_income: 77,670,000,000.0000
- operating_income: 79,975,000,000.0000
- research_and_development: N/A
- revenue_yoy_growth: 19.6200
- eps_yoy_growth: 242.2600
- revenue_yoy_growth_avg: 15.7400
- eps_yoy_growth_avg: 96.7000
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q3', '2025-Q2']

欠損・計算不可

- research_and_development

## Financial Health

18点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.99 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.05 で、最低限の短期支払余力があります。

Evidence

- Financials
- Knowledge

使用データ

- cash: 86,810,000,000.0000
- total_liabilities: 406,977,000,000.0000
- shareholders_equity: 411,065,000,000.0000
- long_term_debt: 65,648,000,000.0000
- current_ratio: 1.0508

## Valuation

15点

理由

- PER はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- Forward PER はセクター内 77.78 パーセンタイル / 母数 10 で、相対的な加点は抑えています。
- PEG はセクター内 22.22 パーセンタイル / 母数 10 で、相対的に割安寄りです。
- PBR はセクター内 25.00 パーセンタイル / 母数 5 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 21.0667
- forward_pe: 25.2221
- peg_ratio: 1.3800
- price_to_book: 5.1230
- sector_peer_count: 10
- trailing_pe_percentile: 22.2200
- trailing_pe_peer_count: 10
- forward_pe_percentile: 77.7800
- forward_pe_peer_count: 10
- peg_ratio_percentile: 22.2200
- peg_ratio_peer_count: 10
- price_to_book_percentile: 25.0000
- price_to_book_peer_count: 5

## Momentum

10点

理由

- 1M の対SPY超過リターンは +9.59pt で、市場並み以上です。
- 3M の対SPY超過リターンは -4.25pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンが +15.19pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -3.38pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 0.63 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 12.9077
- 3M: -1.5958
- 6M: 27.6709
- 1Y: 18.0761
- benchmark: SPY
- benchmark_returns: {'1M': 3.32, '3M': 2.66, '6M': 12.48, '1Y': 21.46}
- excess_returns: {'1M': 9.59, '3M': -4.25, '6M': 15.19, '1Y': -3.38}
- latest_volume: 27,975,466.0000
- average_volume_30d: 44,280,922.2000

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 1 件(純比率 +0.00)で、センチメントは 4.0 点です。
- イベント後の平均株価反応が 1.33% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 1
- sentiment_net_ratio: 0.0000
- event_count: 10
- events_with_price_reaction: 6

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
