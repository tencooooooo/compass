# Release Strategy

Compass uses milestones to mark project maturity.

## Alpha

Alpha releases are research and foundation milestones.

Characteristics:

- Core architecture may still change
- Data formats may evolve
- Reports are useful but experimental
- Documentation and philosophy are actively shaped

`v1.0-alpha` marks the first project milestone: Phase1 is complete, Phase2 has started, and the Compass rebranding milestone is complete.

## Beta

Beta releases should have stable workflows and clearer output expectations.

Characteristics:

- Core collectors and analyzers are stable
- Scoring and screening are explainable
- Backtesting foundation exists
- Generated reports are easier to validate

## Stable

Stable releases should be usable as a reliable research assistant.

Characteristics:

- Data model is documented and stable
- Dashboard or API access may be available
- Report quality checks are in place
- Documentation is complete enough for new users

## LTS

Long-term support releases should prioritize reliability, reproducibility, and compatibility.

Characteristics:

- Minimal breaking changes
- Migration notes for data model changes
- Strong release notes
- Clear operational guidance for GitHub Actions and cloud use

## Release Notes

Every release should update:

- `CHANGELOG.md`
- `README.md` when user-facing behavior changes
- `knowledge/project_history.md` for major project milestones
- Related docs when architecture or operation changes
