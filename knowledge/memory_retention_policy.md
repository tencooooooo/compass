# Memory Retention Policy

Memoryは現在、無期限で保持します。

## Current Policy

- Company Memory: 無期限
- Sector Memory: 無期限
- Discovery Memory: 無期限
- Validation Memory: 無期限
- Market Memory: 無期限
- Lessons Memory: 無期限

## Storage

現在はLocal JSONで保存します。

GitHub Actionsでは `memory/` をcacheで復元し、Artifactにも含めます。

## Future Policy

将来、データ量が増えた場合は以下を検討します。

- Archiveディレクトリ追加
- 年単位の圧縮
- S3への移行
- Databaseへの移行
- 古い日次スナップショットの集約

## Principle

MemoryはCompassの学習基盤です。短期的な容量削減より、検証可能性と長期参照性を優先します。
