from datasources.base.datasource import BaseDataSource, DataSourceResult

__all__ = ["BaseDataSource", "DataSourceManager", "DataSourceRegistry", "DataSourceResult"]


def __getattr__(name: str):
    if name == "DataSourceManager":
        from datasources.base.datasource_manager import DataSourceManager

        return DataSourceManager
    if name == "DataSourceRegistry":
        from datasources.base.datasource_registry import DataSourceRegistry

        return DataSourceRegistry
    raise AttributeError(name)
