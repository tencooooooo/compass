# Memory Architecture

Memory Layerは、Compassが毎日の分析結果を長期的に蓄積するための中核です。

Compass最大の資産はコードではなく、蓄積されたMemoryです。

## Purpose

- 企業、セクター、市場、Discovery、Validationの履歴を保存する。
- 将来Learning Engineが過去の結果を参照できるようにする。
- AnalyzerやEngineが保存先を意識しない構造にする。

## Provider Structure

Memory EngineはProvider Interfaceを通じて保存先を扱います。

Current:

- LocalProvider

Future:

- S3Provider
- PostgresProvider
- SupabaseProvider
- Cloud Storage Provider

## API

他Engineは以下のAPIを使います。

```text
Memory.save()
Memory.load()
Memory.update()
Memory.delete()
Memory.exists()
Memory.list()
Memory.search()
```

## Current Storage

現在はLocal JSONのみです。

```text
memory/
```

GitHub Actionsでは `memory/` をcacheで復元し、Artifactへ含めます。

## Design Principle

保存先がLocalからS3やDatabaseへ変わっても、AnalyzerやEngineの呼び出し側を変更しない設計を優先します。
