# Research Notebook

Knowledgeが現在の結論であるのに対し、Notebookはそこへ至った検証過程の記録です。

[← README に戻る](../../README.md)

## Research Notebook

Compass Research 01 adds a Research Notebook for recording the reasoning process behind Compass improvements.

Knowledge is the current accepted rule set. Research Notebook is the historical path that explains how Compass reached those rules.

Files:

```text
research/notebook/notebook_engine.py
research/notebook/notebook_entry.py
research/notebook/experiment_logger.py
research/notebook/hypothesis_tracker.py
```

Notebook entry fields:

```text
Date
Author
Version
Category
Title
Hypothesis
Experiment
Result
Conclusion
Related Knowledge
Related Experiment
```

Standard categories:

```text
Discovery
Theme
Pattern
Data Source
Learning
Strategy
Experiment
Time Machine
Performance
Data Quality
General
```

Storage:

```text
research/entries/YYYY/YYYY-MM-DD/notebook.md
research/entries/YYYY/YYYY-MM-DD/metadata.json
research/notebook_index.json
```

Search API:

```python
Notebook.search("ETF")
Notebook.search(category="Experiment")
```

Reports and Workspace data:

```text
reports/research/monthly_summary.md
reports/research/yearly_summary.md
reports/research/hypothesis_status.md
reports/research/notebook_dashboard.json
```

Notebook generation is not automated by GitHub Actions. It is written by humans or by explicit tools such as `ExperimentLogger` after review.
