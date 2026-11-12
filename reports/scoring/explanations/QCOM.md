# QCOM Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: QUALCOMM Incorporated
- Total Score: 77 / 100
- Confidence: High
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

High

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 0 件です。
- 主要データが比較的そろっており、説明可能性は高めです。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 100 点満点のうち 77 点を獲得し、シグナル充足率は 77.0% です。
- シグナル強度は Strong(Strong: 65%以上 / Moderate: 40%以上)です。

## Growth

17点

理由

- revenue_growth(直近4四半期平均) は 1.96% で、プラス成長を維持しています。
- eps_growth(直近4四半期平均) は 44.36% で、+30%以上の高成長です。
- eps_growth は直近四半期が前四半期より -196.07pt 低く、成長の減速に注意が必要です。
- 純利益 がプラスで確認できるため加点しています。
- 営業利益 がプラスで確認できるため加点しています。
- 研究開発費が確認でき、将来成長への投資が続いています。
- 売上がプラスで確認できます。

Evidence

- Financials
- Knowledge

使用データ

- total_revenue: 43,120,000,000.0000
- eps: 12.8100
- net_income: 13,628,000,000.0000
- operating_income: 8,658,000,000.0000
- research_and_development: 10,207,000,000.0000
- revenue_yoy_growth: -4.0300
- eps_yoy_growth: -23.0500
- revenue_yoy_growth_avg: 1.9600
- eps_yoy_growth_avg: 44.3600
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q4', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q4', '2025-Q2']

## Financial Health

18点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.00 倍で、負債負担は中程度です。
- 長期債務が総負債に対して過度に大きくないため加点しています。
- Current Ratio が 1.86 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 4,636,000,000.0000
- total_liabilities: 30,428,000,000.0000
- shareholders_equity: 30,401,000,000.0000
- long_term_debt: 12,620,000,000.0000
- current_ratio: 1.8594

## Valuation

16点

理由

- PER はセクター内 14.29 パーセンタイル / 母数 15 で、相対的に割安寄りです。
- Forward PER はセクター内 33.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 73.33 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 13.9032
- forward_pe: 14.4607
- peg_ratio: 1.0200
- price_to_book: 6.2262
- sector_peer_count: 16
- trailing_pe_percentile: 14.2900
- trailing_pe_peer_count: 15
- forward_pe_percentile: 33.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 73.3300
- peg_ratio_peer_count: 16
- price_to_book_percentile: 20.0000
- price_to_book_peer_count: 16

## Momentum

9点

理由

- 1M の対SPY超過リターンは +2.18pt で、市場並み以上です。
- 3M の対SPY超過リターンは +9.81pt で、市場並み以上です。
- 6M の対SPY超過リターンは -19.29pt と、市場を大きく下回っています。
- 1Y の対SPY超過リターンは -7.65pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 1.14 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: -0.1640
- 3M: 7.7317
- 6M: -16.4110
- 1Y: 5.0574
- benchmark: SPY
- benchmark_returns: {'1M': -2.34, '3M': -2.08, '6M': 2.88, '1Y': 12.7}
- excess_returns: {'1M': 2.18, '3M': 9.81, '6M': -19.29, '1Y': -7.65}
- latest_volume: 14,342,200.0000
- average_volume_30d: 12,565,376.6667

## News

17点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベント後の平均株価反応が 1.75% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 3
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 9

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
