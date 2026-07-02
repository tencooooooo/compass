from __future__ import annotations

import re
from typing import Any


_NORMALIZE_PATTERN = re.compile(r"[^a-z0-9぀-ヿ一-鿿]+")


def normalized_title(title: Any) -> str:
    """比較用にタイトルを正規化します(小文字化・記号と空白の除去)。"""
    return _NORMALIZE_PATTERN.sub("", str(title or "").lower())


def dedupe_news_items(news_items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """タイトルが実質同一のニュース(通信社経由の再配信など)を除きます。

    件数ベースのNewsスコアが同一ニュースの配信違いで水増しされるのを防ぎます。
    タイトルが空のものは判定できないため、そのまま残します。
    """
    seen: set[str] = set()
    unique_items: list[dict[str, Any]] = []
    for item in news_items:
        key = normalized_title(item.get("title") if isinstance(item, dict) else None)
        if key and key in seen:
            continue
        if key:
            seen.add(key)
        unique_items.append(item)
    return unique_items
