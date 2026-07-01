from collectors.data_expansion import DisabledCollector


class TrendsCollector(DisabledCollector):
    """Scaffold for Google Trends data."""

    category = "trends"
    data_categories = ("Google Trends",)
    source_name = "Google Trends"
    requires_api_key = False
