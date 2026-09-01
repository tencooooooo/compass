# QCOM Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: QUALCOMM Incorporated
- Total Score: 72 / 100
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

- データが確認できた 100 点満点のうち 72 点を獲得し、シグナル充足率は 72.0% です。
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

16点

理由

- PER はセクター内 14.29 パーセンタイル / 母数 15 で、相対的に割安寄りです。
- Forward PER はセクター内 40.00 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 26.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 19.4834
- forward_pe: 16.7105
- peg_ratio: 0.7200
- price_to_book: 6.5151
- sector_peer_count: 16
- trailing_pe_percentile: 14.2900
- trailing_pe_peer_count: 15
- forward_pe_percentile: 40.0000
- forward_pe_peer_count: 16
- peg_ratio_percentile: 26.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 20.0000
- price_to_book_peer_count: 16

## Momentum

10点

理由

- 1M の対SPY超過リターンが +12.81pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -26.66pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンは +9.76pt で、市場並み以上です。
- 1Y の対SPY超過リターンは -11.26pt と、市場を大きく下回っています。
- 直近出来高が30日平均の 1.14 倍で、通常水準の流動性があります。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 15.4935
- 3M: -25.2764
- 6M: 22.1075
- 1Y: 8.2545
- benchmark: SPY
- benchmark_returns: {'1M': 2.68, '3M': 1.38, '6M': 12.35, '1Y': 19.51}
- excess_returns: {'1M': 12.81, '3M': -26.66, '6M': 9.76, '1Y': -11.26}
- latest_volume: 12,726,310.0000
- average_volume_30d: 11,152,317.0000

## News

12点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 2 件、悪材料 3 件(純比率 -0.20)で、センチメントは 3.2 点です。
- イベント後の平均株価反応が 3.83% とプラスです。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 2
- negative_count: 3
- sentiment_net_ratio: -0.2000
- event_count: 10
- events_with_price_reaction: 8

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
