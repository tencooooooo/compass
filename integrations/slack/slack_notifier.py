from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from typing import Any
from urllib import request
from urllib.error import HTTPError, URLError


# このファイル(integrations/slack/slack_notifier.py)から見て2つ上がプロジェクトルートです。
PROJECT_ROOT = Path(__file__).resolve().parents[2]

from integrations.slack.slack_formatter import build_failure_text, build_payload, build_success_text, current_timestamp
from utils.config import load_yaml
from utils.logger import setup_logger


CONFIG_PATH = PROJECT_ROOT / "config" / "notification.yaml"
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"


DEFAULT_CONFIG = {
    "slack": {"enabled": True},
    "daily_summary": True,
    "send_on_success": True,
    "send_on_failure": True,
    "max_news": 5,
    "top_candidates": 3,
}


def load_notification_config(path: Path) -> dict[str, Any]:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if not path.exists():
        return config

    import yaml

    with path.open("r", encoding="utf-8") as file:
        loaded = yaml.safe_load(file) or {}
    if isinstance(loaded, dict):
        config.update(loaded)
    if isinstance(loaded.get("slack"), dict):
        config["slack"] = {**DEFAULT_CONFIG["slack"], **loaded["slack"]}
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
        response.read()


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
    settings = load_yaml(SETTINGS_PATH)
    logger = setup_logger(PROJECT_ROOT, settings, "compass.slack")
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
    except HTTPError as error:
        logger.error("Slack通知に失敗しました: HTTP %s", error.code)
        return 0
    except (TimeoutError, URLError) as error:
        logger.error("Slack通知に失敗しました: %s", error)
        return 0

    logger.info("Slack通知を送信しました。status=%s", status)
    return 0


if __name__ == "__main__":
    sys.exit(main())
