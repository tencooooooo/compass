from datetime import datetime
import logging
import sys
from pathlib import Path
from zoneinfo import ZoneInfo


def get_timezone(settings: dict) -> ZoneInfo:
    """settings.yaml の timezone を読み込みます。無効な場合はUTCにします。"""
    timezone_name = str(settings.get("timezone", "UTC"))
    try:
        return ZoneInfo(timezone_name)
    except Exception:
        return ZoneInfo("UTC")


class TimezoneFormatter(logging.Formatter):
    """loggingの時刻表示をsettings.yamlのtimezoneに合わせるformatterです。"""

    def __init__(self, timezone: ZoneInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timezone = timezone

    def formatTime(self, record, datefmt=None):
        created_at = datetime.fromtimestamp(record.created, tz=self.timezone)
        if datefmt:
            return created_at.strftime(datefmt)
        return created_at.isoformat()


def setup_logger(project_root: Path, settings: dict, logger_name: str) -> logging.Logger:
    """コンソールと logs/YYYY-MM-DD.log の両方へ出力するloggerを作成します。"""
    log_dir = project_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_level_name = str(settings.get("log_level", "INFO")).upper()
    log_level = getattr(logging, log_level_name, logging.INFO)
    timezone = get_timezone(settings)
    log_path = log_dir / f"{datetime.now(timezone).strftime('%Y-%m-%d')}.log"

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.handlers.clear()
    logger.propagate = False

    formatter = TimezoneFormatter(
        timezone,
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
