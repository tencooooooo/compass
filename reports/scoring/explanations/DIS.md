# DIS Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: The Walt Disney Company
- Total Score: 52 / 100
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

- データが確認できた 100 点満点のうち 52 点を獲得し、シグナル充足率は 52.0% です。
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

- trailing_pe: 22.2887
- forward_pe: 14.5220
- peg_ratio: 2.7600
- price_to_book: 1.6996
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

6点

理由

- 1M の対SPY超過リターンは +8.69pt で、市場並み以上です。
- 3M の対SPY超過リターンは +5.01pt で、市場並み以上です。
- 6M の対SPY超過リターンは -10.02pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -27.43pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 0.53 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 12.4168
- 3M: 6.9707
- 6M: 2.7238
- 1Y: -7.1341
- benchmark: SPY
- benchmark_returns: {'1M': 3.73, '3M': 1.96, '6M': 12.75, '1Y': 20.3}
- excess_returns: {'1M': 8.69, '3M': 5.01, '6M': -10.02, '1Y': -27.43}
- latest_volume: 5,440,769.0000
- average_volume_30d: 10,332,838.9667

## News

14点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 7 件、悪材料 1 件(純比率 +0.75)で、センチメントは 7.0 点です。
- イベント後の平均株価反応が 0.07% と中立圏です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 7
- negative_count: 1
- sentiment_net_ratio: 0.7500
- event_count: 10
- events_with_price_reaction: 9

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
