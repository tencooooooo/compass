# Benchmark Methodology

Initial benchmarks:

- S&P500
- Nasdaq100
- Russell2000

Default ticker mapping:

- S&P500: SPY
- Nasdaq100: QQQ
- Russell2000: IWM

If benchmark price data is unavailable, benchmark fields must remain `N/A` rather than inventing values.

Future benchmark additions may include sector ETFs, theme ETFs, equal-weight indexes, or custom portfolios.

Alpha is calculated as:

```text
Compass signal return - benchmark return
```
