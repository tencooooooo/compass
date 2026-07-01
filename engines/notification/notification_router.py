from __future__ import annotations

from typing import Any

from integrations.slack.slack_connector import SlackConnector


class NotificationRouter:
    """通知先を抽象化するRouterです。将来DiscordやEmailをここへ追加します。"""

    def __init__(self, channels: list[str] | None = None):
        self.channels = channels or ["slack"]
        self.connectors = {"slack": SlackConnector()}

    def route(self, event: dict[str, Any], dry_run: bool = False) -> list[dict[str, Any]]:
        results = []
        for channel in self.channels:
            connector = self.connectors.get(channel)
            if connector is None:
                results.append({"channel": channel, "status": "unsupported"})
                continue
            results.append(connector.send(event, dry_run=dry_run))
        return results
