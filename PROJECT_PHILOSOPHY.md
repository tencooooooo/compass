# Project Philosophy

Compass is built around the idea that useful investment AI should explain companies, not simply output predictions.

## Why Knowledge Exists

`knowledge/` is the human-maintained memory of the project.

It stores investment rules, analysis principles, definitions, event patterns, scoring ideas, brand rules, and design decisions. This keeps important assumptions visible and editable instead of burying them inside prompts or Python code.

Knowledge is not model training data. It is reference material that future analysis systems can read when generating reports or scoring companies.

## Why Explainable AI

Investment research requires trust, context, and review. A result is not useful if the user cannot understand how it was reached.

Compass should therefore:

- Show the facts it used
- Separate facts from interpretation
- Avoid unsupported certainty
- Preserve uncertainty and missing data
- Explain why a company may deserve more research

Explainability is more important than a visually impressive answer.

## Why Long-term Investing

Short-term stock movement is noisy and often driven by factors outside company fundamentals.

Compass focuses on long-term research because durable growth companies are usually understood through business quality, financial progress, competitive position, innovation, and market expectations over time.

The project may analyze price momentum and market reaction, but those signals are treated as context, not as standalone investment conclusions.

## Why Reasons Matter More Than Rankings

Rankings can be useful for sorting candidates, but they can also hide important tradeoffs.

Compass prioritizes reasons because humans need to understand:

- What looks strong
- What looks weak
- What changed recently
- What is uncertain
- What deserves follow-up research

Future scoring and ranking features should always remain explainable.

## AI and Human Roles

AI is responsible for:

- Collecting and organizing available data
- Summarizing company facts
- Comparing peer groups
- Highlighting strengths, risks, and questions
- Drafting research reports

Humans are responsible for:

- Maintaining Knowledge
- Reviewing AI output
- Checking source quality
- Making final investment decisions
- Updating strategy and project direction

Compass works best when AI scales the research process and humans provide judgment.
