from __future__ import annotations

from collections import deque
from typing import Any

from lab.knowledge_graph.graph_storage import GraphStorage


class Graph:
    """Query API for the Compass Knowledge Graph."""

    storage = GraphStorage()

    @classmethod
    def find_related(cls, node_id: str, limit: int = 20) -> list[dict[str, Any]]:
        graph = cls.storage.load()
        labels = {node["id"]: node for node in graph.get("nodes", [])}
        rows = []
        for edge in graph.get("edges", []):
            if edge.get("source") == node_id:
                target = labels.get(edge.get("target"), {"id": edge.get("target"), "label": edge.get("target")})
                rows.append({"node": target, "relationship": edge.get("relationship"), "direction": "out", "evidence": edge.get("evidence")})
            elif edge.get("target") == node_id:
                source = labels.get(edge.get("source"), {"id": edge.get("source"), "label": edge.get("source")})
                rows.append({"node": source, "relationship": edge.get("relationship"), "direction": "in", "evidence": edge.get("evidence")})
        return rows[:limit]

    @classmethod
    def find_theme(cls, theme: str) -> dict[str, Any]:
        graph = cls.storage.load()
        related = cls.find_related(theme, limit=100)
        companies = [row for row in related if row["node"].get("type") == "Company"]
        themes = [row for row in related if row["node"].get("type") == "Theme"]
        return {"theme": theme, "companies": companies, "related_themes": themes, "related_count": len(related)}

    @classmethod
    def shortest_path(cls, start: str, end: str) -> list[str]:
        graph = cls.storage.load()
        adjacency: dict[str, set[str]] = {}
        for edge in graph.get("edges", []):
            source = edge.get("source")
            target = edge.get("target")
            adjacency.setdefault(source, set()).add(target)
            adjacency.setdefault(target, set()).add(source)
        queue = deque([(start, [start])])
        seen = {start}
        while queue:
            node, path = queue.popleft()
            if node == end:
                return path
            for neighbor in sorted(adjacency.get(node, [])):
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
        return []

