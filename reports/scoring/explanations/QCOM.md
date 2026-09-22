# QCOM Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: QUALCOMM Incorporated
- Total Score: 76 / 100
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

- データが確認できた 100 点満点のうち 76 点を獲得し、シグナル充足率は 76.0% です。
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

- total_revenue: 44,284,000,000.0000
- eps: 5.0500
- net_income: 5,541,000,000.0000
- operating_income: 12,394,000,000.0000
- research_and_development: 9,042,000,000.0000
- revenue_yoy_growth: -4.0300
- eps_yoy_growth: -23.0500
- revenue_yoy_growth_avg: 1.9600
- eps_yoy_growth_avg: 44.3600
- revenue_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q4', '2025-Q2']
- eps_growth_quarters: ['2026-Q2', '2026-Q1', '2025-Q4', '2025-Q2']

## Financial Health

17点

理由

- 現金 がプラスで確認できるため加点しています。
- 自己資本がプラスで、財務基盤を確認できます。
- 総負債/自己資本が 1.36 倍で、負債負担は中程度です。
- 長期債務が確認できるため、返済負担の継続確認が必要です。
- Current Ratio が 2.82 で、短期支払余力が確認できます。

Evidence

- Financials
- Knowledge

使用データ

- cash: 5,520,000,000.0000
- total_liabilities: 28,937,000,000.0000
- shareholders_equity: 21,206,000,000.0000
- long_term_debt: 14,811,000,000.0000
- current_ratio: 2.8165

## Valuation

14点

理由

- PER はセクター内 21.43 パーセンタイル / 母数 15 で、相対的に割安寄りです。
- Forward PER はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 26.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 22.6854
- forward_pe: 19.4306
- peg_ratio: 0.8600
- price_to_book: 7.5771
- sector_peer_count: 16
- trailing_pe_percentile: 21.4300
- trailing_pe_peer_count: 15
- forward_pe_percentile: 53.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 46.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 26.6700
- price_to_book_peer_count: 16

## Momentum

15点

理由

- 1M の対SPY超過リターンが +22.76pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -8.03pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンが +37.29pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは +3.52pt で、市場並み以上です。
- 直近出来高が30日平均の 0.92 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 24.0119
- 3M: -2.3421
- 6M: 55.8904
- 1Y: 21.3059
- benchmark: SPY
- benchmark_returns: {'1M': 1.25, '3M': 5.69, '6M': 18.6, '1Y': 17.78}
- excess_returns: {'1M': 22.76, '3M': -8.03, '6M': 37.29, '1Y': 3.52}
- latest_volume: 11,465,322.0000
- average_volume_30d: 12,493,450.7333

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 2 件(純比率 +0.00)で、センチメントは 4.0 点です。
- イベント後の平均株価反応が 2.08% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 2
- negative_count: 2
- sentiment_net_ratio: 0.0000
- event_count: 10
- events_with_price_reaction: 6

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
