from collectors.data_expansion import DisabledCollector


class MacroCollector(DisabledCollector):
    """Scaffold for macroeconomic data such as CPI, FOMC, employment, rates, and VIX."""

    category = "macro"
    data_categories = ("CPI", "FOMC", "Employment", "Interest Rates", "VIX")
    source_name = "Macro data providers"
