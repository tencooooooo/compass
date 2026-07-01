from datasources.base.datasource import ScaffoldDataSource


class FinnhubProvider(ScaffoldDataSource):
    """Scaffold provider for Finnhub market and company data."""

    name = "finnhub"
    source_label = "Finnhub"
    requires_api_key = True
    api_key_env = "FINNHUB_API_KEY"
