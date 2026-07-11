# Evaluation Policy

Compass evaluation must be separate from Feedback and Learning.

Rules:

- Performance Evaluation does not update Knowledge.
- Performance Evaluation does not approve or reject proposals.
- Performance Evaluation does not rewrite scoring rules.
- Pending rows must be visible instead of forced into incomplete metrics.
- Historical performance should be saved in `memory/performance/history.json`.
- Every dated Discovery Memory snapshot must remain eligible for later evaluation.
- Scheduled evaluation must fail clearly when prices or signal inputs are missing; an empty scorecard is not a successful evaluation.
- Validation rows are keyed by Discovery date, ticker, and period, and are refreshed until the period is complete.
- Evaluation reports are evidence for humans, not automatic self-improvement.

Performance Evaluation is designed to show success rate, reproducibility, and improvement areas over time.
