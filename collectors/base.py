import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseCollector(ABC):
    """データ収集処理で共通して使う、薄い基底クラスです。"""

    def __init__(self, project_root: Path, settings: dict[str, Any], logger: logging.Logger):
        self.project_root = project_root
        self.settings = settings
        self.logger = logger
        self.output_root = project_root / settings.get("output_directory", "storage")

    @abstractmethod
    def run(self) -> int:
        """collectorごとのメイン処理を実行します。"""
        raise NotImplementedError

