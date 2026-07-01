# Memory Schema

Memory LayerのJSON構造を整理します。

## companies

Path:

```text
memory/companies/{ticker}.json
```

Fields:

```text
Company
History
Scores
Discovery
Validation
Events
News
Confidence
Timestamp
```

`History` は日次スナップショットを時系列で蓄積します。

## sectors

Path:

```text
memory/sectors/{sector}.json
```

Fields:

```text
Sector
History
AverageScore
AverageMomentum
MajorNews
DiscoveryCount
ValidationResults
Timestamp
```

## discoveries

Path:

```text
memory/discoveries/YYYY-MM-DD.json
```

Fields:

```text
date
timestamp
generated_at
candidates
```

## validations

Path:

```text
memory/validations/YYYY-MM.json
```

Fields:

```text
month
timestamp
Excellent
Good
Neutral
Poor
average_return
rows
```

## market

Path:

```text
memory/market/YYYY-MM-DD.json
```

Fields:

```text
date
timestamp
market
sectors
top_events
summary
```

## lessons

Path:

```text
memory/lessons/lessons.json
```

Learning Engineが将来更新する知見の保存場所です。
