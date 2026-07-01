from __future__ import annotations

import json
import os
from typing import Any
from urllib import request
from urllib.error import URLError

from integrations.slack.slack_formatter import build_payload


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


def format_event(event: dict[str, Any]) -> str:
    lines = [
        f"{event.get('emoji', '🧭')} *{event.get('title', 'Compass Alert')}*",
        "",
        f"*Priority*: {event.get('priority', 'Medium')}",
    ]
    ticker = event.get("ticker")
    if ticker:
        lines.append(f"*Ticker*: {ticker}")
    if event.get("summary"):
        lines.extend(["", str(event["summary"])])
    details = event.get("details") or []
    if details:
        lines.extend(["", "*Details*"])
        lines.extend([f"- {item}" for item in details[:8]])
    evidence = event.get("evidence") or []
    if evidence:
        lines.extend(["", "*Evidence*"])
        lines.extend([f"- {item}" for item in evidence[:8]])
    return "\n".join(lines)


class SlackConnector:
    """Notification Routerから呼び出すSlack送信用Connectorです。"""

    channel_name = "slack"

    def __init__(self, webhook_url: str | None = None):
        self.webhook_url = webhook_url or os.getenv("SLACK_WEBHOOK_URL")

    def send(self, event: dict[str, Any], dry_run: bool = False) -> dict[str, Any]:
        text = format_event(event)
        payload = build_payload(text)
        if dry_run:
            return {"channel": self.channel_name, "status": "dry_run", "payload": payload}
        if not self.webhook_url:
            return {"channel": self.channel_name, "status": "skipped_no_webhook"}
        try:
            post_to_slack(self.webhook_url, payload)
        except (RuntimeError, TimeoutError, URLError) as error:
            return {"channel": self.channel_name, "status": "failed", "error": str(error)}
        return {"channel": self.channel_name, "status": "sent"}
