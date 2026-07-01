# Knowledge Versioning

Knowledge Version管理は、Compassの学習履歴を追跡可能にするための仕組みです。

## Current Structure

```text
knowledge/versions/v1.json
knowledge/versions/v2.json
```

`v1` は現在の初期Knowledge Versionです。

`v2` は将来のHuman Approved Learning後に使うための雛形です。

## Change History

Versionファイルには、変更内容、承認者、関連Proposal、Rollback先を記録します。

## Rollback

すべてのKnowledge変更はRollback可能であるべきです。

Learning EngineはRollback対象を記録しますが、Knowledgeを直接変更しません。
