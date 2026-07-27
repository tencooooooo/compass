# Core Engines

Memory・Feedback・Decision・Learning からなる、人間のレビューを前提とした学習ループです。

[← README に戻る](../../README.md)

## Memory Engine

Compass Core 01 adds a provider-based Memory Layer.

Files:

```text
core/memory/memory_engine.py
core/memory/memory_provider.py
core/memory/local_provider.py
```

Memory API:

```text
Memory.save()
Memory.load()
Memory.update()
Memory.delete()
Memory.exists()
Memory.list()
Memory.search()
```

Current provider:

```text
LocalProvider
```

Future providers:

```text
S3Provider
PostgresProvider
SupabaseProvider
```

Current local output:

```text
memory/companies/
memory/sectors/
memory/discoveries/
memory/validations/
memory/market/
memory/lessons/
memory/feedback/
memory/decision/
```

`memory/` is ignored by the main Git branch, restored from the dedicated `compass-data` branch, committed back at the end of data-producing workflows, and included in workflow artifacts. Company Memory accumulates deduplicated News and Event history instead of retaining only the latest batch. GitHub Actions cache remains a migration fallback, not the system of record. This keeps Memory as durable operational data while allowing future migration to S3 or a database without changing Analyzer or Engine callers.

## Feedback Engine

Compass Core 02 adds a Feedback Layer.

Files:

```text
core/feedback/feedback_engine.py
core/feedback/feedback_analyzer.py
core/feedback/improvement_detector.py
```

Output:

```text
reports/feedback/feedback_summary.md
reports/feedback/improvement_candidates.md
reports/feedback/feedback_history.json
```

Feedback Engine compares Discovery results with Validation results and summarizes:

- Discovery Accuracy
- Score Accuracy
- Confidence Accuracy
- Sector Accuracy
- Event Accuracy
- Success patterns
- Failure patterns

Feedback Engine is not the Learning Engine. It does not automatically update Knowledge, scoring rules, or investment rules.

Its role is to generate Knowledge update candidates for human review. Learning Engine should be built later on top of accumulated Feedback History and reviewed Knowledge changes.

## Decision Engine

Compass Core 03 adds a Decision Layer.

Files:

```text
core/decision/decision_engine.py
core/decision/proposal_generator.py
core/decision/review_manager.py
```

Output:

```text
reports/proposals/proposal_YYYY-MM-DD.md
reports/proposals/proposal_index.json
reports/knowledge_updates/candidate_YYYY-MM-DD.md
```

Decision Engine converts Feedback improvement candidates into human-reviewable proposals. Each proposal includes:

- Proposal ID
- Target
- Reason
- Evidence
- Impact scope
- Expected effect
- Risk
- Recommendation
- Approve / Reject / Review Later options

Proposal status is tracked in JSON with:

```text
Pending
Approved
Rejected
Deferred
```

Decision Engine protects Knowledge. It generates proposal and Knowledge update candidate files, but it does not change Knowledge, Scoring, Rules, or prompts automatically.

## Learning Engine

Compass Core 04 adds a Human Approved Learning Layer.

Files:

```text
core/learning/learning_engine.py
core/learning/proposal_loader.py
core/learning/learning_package_builder.py
core/learning/learning_history.py
```

Output:

```text
reports/learning/learning_package_YYYY-MM-DD.md
reports/learning/learning_summary.md
reports/learning/learning_metrics.json
memory/learning/learning_history.json
```

Knowledge version templates:

```text
knowledge/versions/v1.json
knowledge/versions/v2.json
```

Learning Engine only loads proposals with:

```text
Approved
```

Rejected, Deferred, and Pending proposals are ignored.

Learning Engine does not rewrite Knowledge, Scoring, Rules, or prompts. It builds a Learning Package that summarizes approved proposals, adoption reasons, expected effects, impact scope, Knowledge candidates, Scoring candidates, and review history.

This keeps Compass explainable, traceable, and rollbackable. Knowledge changes remain human-owned.
