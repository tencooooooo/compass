from __future__ import annotations

import argparse
from datetime import datetime
import json
import logging
import os
from pathlib import Path
import sys
from typing import Any
from urllib import request
from urllib.error import URLError


# このファイル(integrations/slack/slack_notifier.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from integrations.slack.slack_formatter import build_failure_text, build_payload, build_success_text, current_timestamp  # noqa: E402


CONFIG_PATH = PROJECT_ROOT / "config" / "notification.yaml"
LOG_DIR = PROJECT_ROOT / "logs"


DEFAULT_CONFIG = {
    "slack": {"enabled": True},
    "daily_summary": True,
    "send_on_success": True,
    "send_on_failure": True,
    "max_news": 5,
    "top_candidates": 3,
}


def setup_simple_logger() -> logging.Logger:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("compass.slack")
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


def load_notification_config(path: Path) -> dict[str, Any]:
    """PyYAMLがない失敗ケースでも通知できるように、最小YAMLを自前で読めるようにします。"""
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if not path.exists():
        return config

    try:
        import yaml  # type: ignore

        with path.open("r", encoding="utf-8") as file:
            loaded = yaml.safe_load(file) or {}
        if isinstance(loaded, dict):
            config.update(loaded)
        if isinstance(loaded.get("slack"), dict):
            config["slack"] = {**DEFAULT_CONFIG["slack"], **loaded["slack"]}
        return config
    except Exception:
        pass

    current_section: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        if not value.strip():
            current_section = key.strip()
            config.setdefault(current_section, {})
            continue
        parsed_value = parse_scalar(value)
        if line.startswith(" ") and current_section and isinstance(config.get(current_section), dict):
            config[current_section][key.strip()] = parsed_value
        else:
            config[key.strip()] = parsed_value
            current_section = None
    return config


def post_to_slack(webhook_url: str, payload: dict[str, Any]) -> None:
    data = json.dumps(payload).encode("utf-8")
    slack_request = request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(slack_request, timeout=20) as response:
        if response.status >= 400:
            raise RuntimeError(f"Slack webhook returned HTTP {response.status}")


def build_context(args: argparse.Namespace) -> dict[str, str]:
    return {
        "timestamp": current_timestamp(),
        "status": args.status or os.getenv("COMPASS_WORKFLOW_STATUS", "success"),
        "run_number": os.getenv("GITHUB_RUN_NUMBER") or os.getenv("COMPASS_RUN_NUMBER") or "N/A",
        "failed_step": args.failed_step or os.getenv("COMPASS_FAILED_STEP", ""),
        "error": args.error or os.getenv("COMPASS_ERROR", ""),
        "repository": os.getenv("GITHUB_REPOSITORY", ""),
        "workflow": os.getenv("GITHUB_WORKFLOW", ""),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send Compass daily research brief to Slack.")
    parser.add_argument("--status", choices=["success", "failure", "cancelled"], default=None)
    parser.add_argument("--failed-step", default=None)
    parser.add_argument("--error", default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = setup_simple_logger()
    config = load_notification_config(CONFIG_PATH)
    slack_config = config.get("slack", {}) if isinstance(config.get("slack"), dict) else {}

    if not slack_config.get("enabled", True):
        logger.info("Slack通知はnotification.yamlで無効化されています。")
        return 0

    context = build_context(args)
    status = context["status"]
    if status == "success" and not config.get("daily_summary", True):
        logger.info("daily_summaryが無効のためSlack通知をスキップします。")
        return 0
    if status == "success" and not config.get("send_on_success", True):
        logger.info("成功通知はnotification.yamlで無効化されています。")
        return 0
    if status != "success" and not config.get("send_on_failure", True):
        logger.info("失敗通知はnotification.yamlで無効化されています。")
        return 0

    text = build_success_text(PROJECT_ROOT, context, config) if status == "success" else build_failure_text(context)
    payload = build_payload(text)

    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        logger.info("SLACK_WEBHOOK_URLが未設定のためSlack通知をスキップします。")
        return 0

    try:
        post_to_slack(webhook_url, payload)
    except (RuntimeError, TimeoutError, URLError) as error:
        logger.error("Slack通知に失敗しました: %s", error)
        return 0

    logger.info("Slack通知を送信しました。status=%s", status)
    return 0


if __name__ == "__main__":
    sys.exit(main())
