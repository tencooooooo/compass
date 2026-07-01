# Daily Report Definition

Morning Research Briefは、Compassが毎朝届ける短い市場・候補サマリーです。

## Purpose

- GitHub Actionsを開かなくても処理結果を把握する。
- 今日確認すべきDiscovery候補を把握する。
- 市場とセクターの雰囲気を短く確認する。
- Validation結果の変化を継続的に見る。

## Sections

### 実行結果

- 実行日時
- 処理成功または失敗
- 対象銘柄数

### Discovery Summary

- 新しいDiscovery候補数
- Top Candidates
- Discovery Score
- Confidence

### Score Changes

- 前回スコアと比較できる場合のみ表示する。
- 比較データがない場合は初回実行として扱う。

### Market Summary

- Market Intelligenceのセクター要約を表示する。

### Important News

- 重要ニュースのタイトルのみを最大5件表示する。

### Validation Summary

- Excellent
- Good
- Neutral
- Poor

### Artifact

- GitHub Actions Artifact名を表示する。

## Tone

簡潔に、事実中心に、投資判断を避ける。
