# Folder Structure

```text
compass/
├── analyzers/
├── backtests/
├── collectors/
├── config/
├── core/
├── docs/
├── engines/
├── integrations/
├── knowledge/
├── prompts/
├── reports/
├── screeners/
├── storage/
├── tests/
├── utils/
├── .github/workflows/
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── MANIFEST.md
├── PROJECT_PHILOSOPHY.md
├── README.md
└── requirements.txt
```

## Main Folders

- `collectors/`: Scripts that collect market, company, financial, and news data.
- `analyzers/`: Scripts that generate company and comparative analysis reports.
- `engines/`: Explainable engines such as scoring, market intelligence, discovery, validation, and notification.
- `integrations/`: External notification and delivery integrations such as Slack.
- `config/`: Ticker list and project settings.
- `core/`: Core platform layers such as Memory.
- `knowledge/`: Human-maintained analysis rules and project knowledge.
- `prompts/`: Prompt templates separated from Python code.
- `docs/`: Documentation for architecture, roadmap, folder structure, and data model.
- `storage/`: Generated runtime data. Raw data and events are not tracked by Git.
- `reports/`: Generated Markdown reports. Reports are not tracked by Git.
- `utils/`: Shared helper code.
- `.github/workflows/`: GitHub Actions pipeline.
- `MANIFEST.md`: Project values, purpose, prohibited uses, and long-term goal.
- `PROJECT_PHILOSOPHY.md`: Explanation of Knowledge, explainability, long-term thinking, and human review.
