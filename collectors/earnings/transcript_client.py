from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class TranscriptClient:
    """Loads earnings call transcripts from local files or future source URLs."""

    def __init__(self, user_agent: str | None = None, timeout: int = 30) -> None:
        self.user_agent = user_agent or os.getenv("EARNINGS_USER_AGENT") or "Compass Research Platform"
        self.timeout = timeout

    def fetch(self, source_path: str | None = None, source_url: str | None = None) -> dict[str, Any]:
        if source_path:
            return self._from_path(Path(source_path))
        if source_url:
            return self._from_url(source_url)
        raise ValueError("source_path or source_url is required for transcript collection.")

    def _from_path(self, path: Path) -> dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Transcript source does not exist: {path}")
        text = path.read_text(encoding="utf-8")
        if path.suffix.lower() == ".json":
            data = json.loads(text)
            return {
                "source": str(path),
                "metadata": data.get("metadata", {}),
                "text": data.get("transcript") or data.get("text") or "",
            }
        return {"source": str(path), "metadata": {}, "text": text}

    def _from_url(self, url: str) -> dict[str, Any]:
        request = Request(url, headers={"User-Agent": self.user_agent})
        try:
            with urlopen(request, timeout=self.timeout) as response:
                text = response.read().decode("utf-8", errors="replace")
        except (HTTPError, URLError, TimeoutError) as error:
            raise RuntimeError(f"Transcript request failed: {url}") from error
        return {"source": url, "metadata": {}, "text": text}
