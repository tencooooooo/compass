# A/B Testing Policy

Compass A/B testing compares baseline and candidate behavior without changing production rules automatically.

Policy:

- Baseline and candidate versions must be named.
- Metrics must be recorded before declaring a winner.
- Inconclusive results are valid outcomes.
- Missing metrics must stay visible as `N/A`.
- Experiments do not update Knowledge, Scoring, Learning, or Strategy rules automatically.
- Human review is required before any candidate becomes the new baseline.

Candidate wins should require explainable metric improvements, not isolated anecdotes.
