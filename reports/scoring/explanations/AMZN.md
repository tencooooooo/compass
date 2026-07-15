# AMZN Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Amazon.com, Inc.
- Total Score: 70 / 100
- Confidence: Medium
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 1 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。

## Growth

15点

理由

- revenue_growth(直近4四半期平均) は 12.99% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 51.69% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より +38.48pt 高く、成長の加速がみられます。
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
- revenue_yoy_growth: 16.6100
- eps_yoy_growth: 74.8400
- revenue_yoy_growth_avg: 12.9900
- eps_yoy_growth_avg: 51.6900
- revenue_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']

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

14点

理由

- セクター比較対象が 2 社のため、PER は固定閾値で評価しています。
- PER は 30.46 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 2 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 25.79 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 2 社のため、PEG は固定閾値で評価しています。
- PEG は 1.41 で、バリュエーション面は中立から注意寄りです。
- セクター比較対象が 2 社のため、PBR は固定閾値で評価しています。
- PBR は 6.20 で、評価ルール上は過度な割高さが抑えられています。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 30.4612
- forward_pe: 25.7892
- peg_ratio: 1.4100
- price_to_book: 6.2045
- sector_peer_count: 2

## Momentum

6点

理由

- 1M の対SPY超過リターンは +4.86pt で、市場並み以上です。
- 3M の対SPY超過リターンは -6.58pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンは -5.71pt と、市場を小幅に下回っています。
- 1Y の対SPY超過リターンは -9.18pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 0.77 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 6.8791
- 3M: 2.3854
- 6M: 3.4446
- 1Y: 12.9691
- benchmark: SPY
- benchmark_returns: {'1M': 2.02, '3M': 8.97, '6M': 9.16, '1Y': 22.14}
- excess_returns: {'1M': 4.86, '3M': -6.58, '6M': -5.71, '1Y': -9.18}
- latest_volume: 42,296,511.0000
- average_volume_30d: 54,978,693.7000

## News

17点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 6 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が 3.02% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 6
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 4

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
