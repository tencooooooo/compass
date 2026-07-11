from __future__ import annotations

import argparse
from datetime import datetime
import json
import logging
import os
from pathlib import Path
import sys
from typing import Any


# このファイル(engines/notification/notification_engine.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]

from engines.notification.event_detector import (  # noqa: E402
    current_market_snapshot,
    current_score_snapshot,
    detect_events,
    workflow_failure_event,
)
from engines.notification.notification_router import NotificationRouter  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "notification.yaml"
LOG_DIR = PROJECT_ROOT / "logs"
STORAGE_DIR = PROJECT_ROOT / "storage" / "notifications"
STATE_DIR = STORAGE_DIR / "state"
HISTORY_PATH = STORAGE_DIR / "notification_history.json"
SCORE_STATE_PATH = STATE_DIR / "company_scores_latest.json"
MARKET_STATE_PATH = STATE_DIR / "market_trends_latest.json"


DEFAULT_RULES = {
    "discovery_score": 90,
    "score_change": 5,
    "market_change": True,
    "important_news": True,
    "validation": "Excellent",
}


def setup_simple_logger() -> logging.Logger:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("compass.notification")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler = logging.FileHandler(LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def parse_scalar(value: str) -> Any:
    normalized = value.strip()
    if normalized.lower() == "true":
        return True
    if normalized.lower() == "false":
        return False
    try:
        return int(normalized)
    except ValueError:
        return normalized


def load_simple_yaml(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    """通知は依存関係インストール失敗時にも動かしたいので、最小YAMLを標準ライブラリで読みます。"""
    if not path.exists():
        return json.loads(json.dumps(default))

    config = json.loads(json.dumps(default))
    current_section: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        if not value.strip():
            current_section = key
            config.setdefault(current_section, {})
            continue
        parsed_value = parse_scalar(value)
        if line.startswith(" ") and current_section and isinstance(config.get(current_section), dict):
            config[current_section][key] = parsed_value
        else:
            config[key] = parsed_value
            current_section = None
    return config


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_notification_config() -> dict[str, Any]:
    data = load_simple_yaml(CONFIG_PATH, {"notification": DEFAULT_RULES, "max_news": 5})
    rules = {**DEFAULT_RULES, **(data.get("notification") or {})}
    data["notification"] = rules
    return data


def sent_event_ids(history: list[dict[str, Any]]) -> set[str]:
    sent_statuses = {"sent", "dry_run", "skipped_no_webhook"}
    ids: set[str] = set()
    for record in history:
        if record.get("status") in sent_statuses and record.get("event_id"):
            ids.add(str(record["event_id"]))
    return ids


def append_history(history: list[dict[str, Any]], event: dict[str, Any], route_results: list[dict[str, Any]]) -> None:
    for result in route_results:
        history.append(
            {
                "event_id": event.get("event_id"),
                "event_type": event.get("event_type"),
                "priority": event.get("priority"),
                "title": event.get("title"),
                "ticker": event.get("ticker"),
                "detected_at": event.get("detected_at"),
                "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
                "channel": result.get("channel"),
                "status": result.get("status"),
                "error": result.get("error"),
            }
        )


def save_state_snapshots() -> None:
    write_json(SCORE_STATE_PATH, current_score_snapshot(PROJECT_ROOT))
    write_json(MARKET_STATE_PATH, current_market_snapshot(PROJECT_ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect important Compass events and route notifications.")
    parser.add_argument("--status", choices=["success", "failure", "cancelled"], default=None)
    parser.add_argument("--failed-step", default=None)
    parser.add_argument("--error", default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = setup_simple_logger()
    started_at = datetime.now().astimezone()
    logger.info("Compass Research 06 - Notification Engine")
    logger.info("開始時刻: %s", started_at.strftime("%Y-%m-%d %H:%M:%S"))

    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    config = load_notification_config()
    rules = config.get("notification", DEFAULT_RULES)
    max_news = int(config.get("max_news", 5))
    important_news_max_age_hours = int(config.get("important_news_max_age_hours", 36))
    history = load_json(HISTORY_PATH, [])
    if not isinstance(history, list):
        history = []

    status = args.status or os.getenv("COMPASS_WORKFLOW_STATUS", "success")
    if status != "success":
        events = [
            workflow_failure_event(
                status=status,
                run_number=os.getenv("GITHUB_RUN_NUMBER") or os.getenv("COMPASS_RUN_NUMBER") or "N/A",
                failed_step=args.failed_step or os.getenv("COMPASS_FAILED_STEP", ""),
                error=args.error or os.getenv("COMPASS_ERROR", ""),
            )
        ]
    else:
        previous_scores = load_json(SCORE_STATE_PATH, {})
        previous_market = load_json(MARKET_STATE_PATH, {})
        events = detect_events(
            PROJECT_ROOT,
            rules,
            previous_scores,
            previous_market,
            max_news,
            important_news_max_age_hours,
        )

    already_sent = sent_event_ids(history)
    fresh_events = [event for event in events if event.get("event_id") not in already_sent]
    router = NotificationRouter(channels=["slack"])

    logger.info("検知イベント数: %s / 新規通知対象: %s", len(events), len(fresh_events))
    for event in fresh_events:
        route_results = router.route(event, dry_run=args.dry_run)
        append_history(history, event, route_results)
        logger.info(
            "[%s] %s: %s",
            event.get("priority"),
            event.get("event_type"),
            ", ".join(f"{result.get('channel')}={result.get('status')}" for result in route_results),
        )

    write_json(HISTORY_PATH, history)
    if status == "success":
        save_state_snapshots()

    finished_at = datetime.now().astimezone()
    logger.info("通知履歴保存: %s", HISTORY_PATH)
    logger.info("終了時刻: %s", finished_at.strftime("%Y-%m-%d %H:%M:%S"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
