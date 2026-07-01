from collectors.data_expansion import DisabledCollector


class SentimentCollector(DisabledCollector):
    """Scaffold for Reddit, X, and news sentiment data."""

    category = "sentiment"
    data_categories = ("Reddit", "X", "News Sentiment")
    source_name = "Sentiment data providers"
