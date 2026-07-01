# Simulation Rules

Simulation rules:

- No real orders are created.
- No brokerage integration is used.
- Initial capital defaults to 100000 USD.
- Position sizing defaults to equal weight.
- Holding period defaults to 180 days.
- Strategy rules are loaded from `config/strategy.yaml`.
- Price data comes from local Compass storage.
- Missing benchmark data must be shown as missing.
- Results must be reproducible from stored data and configuration.

Simulation output should include:

- holdings
- trade history
- equity curve
- strategy metrics
- benchmark comparison
- ranking
- dashboard JSON

The purpose is algorithm research, not investment advice.
