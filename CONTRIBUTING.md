# Contributing

Compass is designed as a long-term research assistant project. Please keep changes simple, readable, and easy to operate on GitHub.

## Branch Workflow

- Use `main` for stable code.
- Use feature branches such as `feature/scoring-v0.8` or `docs/update-roadmap`.
- Keep pull requests focused on one topic.

## Commit Rules

- Use short, descriptive commit messages.
- Prefer prefixes such as `feat:`, `fix:`, `docs:`, `refactor:`, and `chore:`.
- Do not commit generated data, logs, reports, `.env`, or virtual environments.

## Folder Structure

- `collectors/`: Data collection scripts.
- `analyzers/`: Analysis and report generation scripts.
- `knowledge/`: Human-maintained rules, principles, and project knowledge.
- `prompts/`: Prompt templates separated from Python code.
- `docs/`: Project documentation.
- `storage/`: Runtime/generated data. Generated raw data is not tracked by Git.
- `reports/`: Runtime/generated reports. Reports are not tracked by Git.

## Coding Style

- Keep implementations simple and explicit.
- Prefer small helper functions over large monolithic scripts.
- Use logging instead of `print()` for pipeline scripts.
- Do not add investment advice, buy/sell calls, or target prices.

## Knowledge Update Rules

- Update `knowledge/` when analysis rules, scoring principles, terminology, or project history changes.
- Treat Knowledge as human-maintained reference material, not model training data.
- Record important design decisions in `knowledge/decisions.md`.

## README Update Rules

- Update `README.md` when workflows, folder structure, setup steps, or generated outputs change.
- Keep README understandable for a first-time GitHub visitor.
- Link deeper technical details to `docs/` when README would become too long.
