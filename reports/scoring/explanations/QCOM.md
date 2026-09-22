# QCOM Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: QUALCOMM Incorporated
- Total Score: 74 / 100
- Confidence: Medium
- Signal Strength: Strong
- Evidence: Company, Events, Financials, Knowledge, News, Prices

## Confidence

Medium

理由

- 利用可能な主要データ領域は5領域中 5 領域です。
- 欠損または計算不可の項目数は 1 件です。
- 主要データは一定程度ありますが、欠損や未取得項目が残っています。
- イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。
- Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。

## Signal Strength

Strong

理由

- データが確認できた 100 点満点のうち 74 点を獲得し、シグナル充足率は 74.0% です。
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
- Forward PER はセクター内 42.86 パーセンタイル / 母数 15 で、中位レンジです。
- PEG はセクター内 36.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 26.67 パーセンタイル / 母数 16 で、中位レンジです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 22.2231
- forward_pe: 19.0347
- peg_ratio: 0.7900
- price_to_book: 7.4227
- sector_peer_count: 16
- trailing_pe_percentile: 21.4300
- trailing_pe_peer_count: 15
- forward_pe_percentile: 42.8600
- forward_pe_peer_count: 15
- peg_ratio_percentile: 36.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 26.6700
- price_to_book_peer_count: 16

## Momentum

13点

理由

- 1M の対SPY超過リターンが +11.07pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -23.23pt と、市場を大きく下回っています。
- 6M の対SPY超過リターンが +20.27pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは -7.34pt と、市場を小幅に下回っています。
- 直近出来高が30日平均の 4.49 倍で、市場関心の高まりが確認できます。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 10.3621
- 3M: -20.9733
- 6M: 36.6143
- 1Y: 9.7791
- benchmark: SPY
- benchmark_returns: {'1M': -0.71, '3M': 2.26, '6M': 16.34, '1Y': 17.12}
- excess_returns: {'1M': 11.07, '3M': -23.23, '6M': 20.27, '1Y': -7.34}
- latest_volume: 54,427,700.0000
- average_volume_30d: 12,127,476.6667

## News

13点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 4 件、悪材料 0 件(純比率 +1.00)で、センチメントは 8.0 点です。
- イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 4
- negative_count: 0
- sentiment_net_ratio: 1.0000
- event_count: 10
- events_with_price_reaction: 0

欠損・計算不可

- event_price_reaction

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
