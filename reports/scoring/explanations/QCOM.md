# QCOM Scoring Explanation

> このスコアは投資判断ではありません。Compassが追加調査の論点を整理するための説明可能な評価です。

## Summary

- Company: QUALCOMM Incorporated
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
- イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。
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

14点

理由

- PER はセクター内 28.57 パーセンタイル / 母数 15 で、中位レンジです。
- Forward PER はセクター内 53.33 パーセンタイル / 母数 16 で、中位レンジです。
- PEG はセクター内 46.67 パーセンタイル / 母数 16 で、中位レンジです。
- PBR はセクター内 20.00 パーセンタイル / 母数 16 で、相対的に割安寄りです。
- バリュエーションは割安判断ではなく、追加調査のための相対評価です。

Evidence

- Company
- Knowledge

使用データ

- trailing_pe: 23.1087
- forward_pe: 19.7932
- peg_ratio: 0.8600
- price_to_book: 7.7185
- sector_peer_count: 16
- trailing_pe_percentile: 28.5700
- trailing_pe_peer_count: 15
- forward_pe_percentile: 53.3300
- forward_pe_peer_count: 16
- peg_ratio_percentile: 46.6700
- peg_ratio_peer_count: 16
- price_to_book_percentile: 20.0000
- price_to_book_peer_count: 16

## Momentum

13点

理由

- 1M の対SPY超過リターンが +21.23pt と、市場を大きく上回っています。
- 3M の対SPY超過リターンは -9.41pt と、市場を小幅に下回っています。
- 6M の対SPY超過リターンが +33.00pt と、市場を大きく上回っています。
- 1Y の対SPY超過リターンは +0.05pt で、市場並み以上です。
- 直近出来高が30日平均の 0.72 倍で、市場関心はやや弱めです。

Evidence

- Prices
- Knowledge

使用データ

- 1M: 21.6475
- 3M: -4.6768
- 6M: 50.3940
- 1Y: 16.9737
- benchmark: SPY
- benchmark_returns: {'1M': 0.41, '3M': 4.74, '6M': 17.39, '1Y': 16.92}
- excess_returns: {'1M': 21.23, '3M': -9.41, '6M': 33.0, '1Y': 0.05}
- latest_volume: 9,089,000.0000
- average_volume_30d: 12,654,730.0000

## News

11点

理由

- ニュース件数は 10 件で、情報量に応じて 3.0 点を加点しています。
- ニュース見出し・要約の簡易分類では、好材料 3 件、悪材料 1 件(純比率 +0.50)で、センチメントは 6.0 点です。
- イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。

Evidence

- News
- Events
- Knowledge

使用データ

- news_count: 10
- positive_count: 3
- negative_count: 1
- sentiment_net_ratio: 0.5000
- event_count: 10
- events_with_price_reaction: 0

欠損・計算不可

- event_price_reaction

## Note

CompassはランキングAIではありません。点数は調査候補を整理するための補助情報であり、理由・根拠・欠損状況と一緒に確認してください。
