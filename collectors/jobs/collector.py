from collectors.data_expansion import DisabledCollector


class JobsCollector(DisabledCollector):
    """Scaffold for hiring trend and job posting data."""

    category = "jobs"
    data_categories = ("Hiring Trends", "Job Postings")
    source_name = "Jobs data providers"
