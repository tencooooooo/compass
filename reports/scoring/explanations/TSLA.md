# TSLA Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: Tesla, Inc.
- Total Score: 56 / 100
- Confidence: High
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。

## Growth

12点

理由

- revenue_growth(直近4四半期平均) は 1.59% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は -29.25% で、前年同期比ではマイナスです。
- eps_growth は直近四半期が前四半期より +45.43pt 高く、成長の加速がみられます。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 94,827,000,000.0000
- eps: 1.1765
- net_income: 3,794,000,000.0000
- operating_income: 4,849,000,000.0000
- research_and_development: 6,411,000,000.0000
- revenue_yoy_growth: 15.7800
- eps_yoy_growth: 8.3300
- revenue_yoy_growth_avg: 1.5900
- eps_yoy_growth_avg: -29.2500
- revenue_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']
- eps_growth_quarters: ['2026-Q1', '2025-Q3', '2025-Q2', '2025-Q1']

## Financial Health

20点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 0.67 倍で、負債負担は相対的に抑えられています。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 2.16 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 16,513,000,000.0000
- total_liabilities: 54,941,000,000.0000
- shareholders_equity: 82,137,000,000.0000
- long_term_debt: 6,584,000,000.0000
- current_ratio: 2.1644

## Valuation

3点

理由

- セクター比較対象が 2 社のため、PER は固定閾値で評価しています。
- PER は 356.92 で、バリュエーション面の加点は抑えています。
- セクター比較対象が 2 社のため、Forward PER は固定閾値で評価しています。
- Forward PER は 152.83 で、バリュエーション面の加点は抑えています。
- セクター比較対象が 2 社のため、PEG は固定閾値で評価しています。
- PEG は 5.11 で、バリュエーション面の加点は抑えています。
- セクター比較対象が 2 社のため、PBR は固定閾値で評価しています。
- PBR は 18.09 で、バリュエーション面は中立から注意寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 356.9189
- forward_pe: 152.8295
- peg_ratio: 5.1100
- price_to_book: 18.0929
- sector_peer_count: 2

## Momentum

6点

理由

- 1M の対SPY超過リターンは -2.91pt と、市場を小幅に下回っています。
- 3M の対SPY超過リターンは +2.55pt で、市場並み以上です。
- 6M の対SPY超過リターンは -19.87pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは +4.47pt で、市場並み以上です。
- 直近出来高が30日平均の 0.50 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -0.7441
- 3M: 12.4170
- 6M: -10.9728
- 1Y: 26.3692
- benchmark: SPY
- benchmark_returns: {'1M': 2.17, '3M': 9.86, '6M': 8.9, '1Y': 21.89}
- excess_returns: {'1M': -2.91, '3M': 2.55, '6M': -19.87, '1Y': 4.47}
- latest_volume: 22,670,942.0000
- average_volume_30d: 45,653,178.0667

## News

15点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 1 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が 0.36% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 1
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 4

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
