from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

from api.services.data_loader import REPO_ROOT
from research.notebook.hypothesis_tracker import HypothesisTracker
from research.notebook.notebook_entry import NotebookEntry


class Notebook:
    """Research Notebook API for creating, indexing, and searching Compass research notes."""

    entries_root = REPO_ROOT / "research" / "entries"
    index_path = REPO_ROOT / "research" / "notebook_index.json"

    @classmethod
    def save(cls, entry: NotebookEntry | dict[str, Any]) -> dict[str, Any]:
        note = entry if isinstance(entry, NotebookEntry) else NotebookEntry(**entry)
        day_dir = cls.entries_root / note.date[:4] / note.date
        day_dir.mkdir(parents=True, exist_ok=True)
        notebook_path = day_dir / "notebook.md"
        metadata_path = day_dir / "metadata.json"
        existing = notebook_path.read_text(encoding="utf-8") if notebook_path.exists() else f"# Research Notebook - {note.date}\n\n"
        if note.entry_id not in existing:
            notebook_path.write_text(existing.rstrip() + "\n\n" + note.markdown(), encoding="utf-8")
        metadata = cls._load_metadata(metadata_path)
        by_id = {item.get("entry_id"): item for item in metadata if item.get("entry_id")}
        by_id[note.entry_id] = note.metadata()
        metadata_path.write_text(json.dumps(list(by_id.values()), ensure_ascii=False, indent=2), encoding="utf-8")
        index = cls.rebuild_index()
        cls.write_reports(index)
        return {"entry": note.metadata(), "notebook": str(notebook_path.relative_to(REPO_ROOT)), "metadata": str(metadata_path.relative_to(REPO_ROOT))}

    @classmethod
    def rebuild_index(cls) -> list[dict[str, Any]]:
        rows = []
        if cls.entries_root.exists():
            for path in sorted(cls.entries_root.glob("*/*/metadata.json")):
                for item in cls._load_metadata(path):
                    item = dict(item)
                    item["path"] = str(path.relative_to(REPO_ROOT))
                    rows.append(item)
        rows = sorted(rows, key=lambda row: (row.get("date", ""), row.get("entry_id", "")), reverse=True)
        cls.index_path.parent.mkdir(parents=True, exist_ok=True)
        cls.index_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
        cls.write_dashboard(rows)
        return rows

    @classmethod
    def search(cls, keyword: str | None = None, category: str | None = None) -> list[dict[str, Any]]:
        index = cls._load_index()
        keyword_lower = keyword.lower() if keyword else None
        results = []
        for row in index:
            if category and row.get("category") != category:
                continue
            if keyword_lower:
                text = " ".join(str(row.get(field, "")) for field in ("title", "hypothesis", "experiment", "result", "conclusion", "related_experiment")).lower()
                if keyword_lower not in text:
                    continue
            results.append(row)
        return results

    @classmethod
    def write_reports(cls, index: list[dict[str, Any]] | None = None) -> dict[str, str]:
        rows = index if index is not None else cls._load_index()
        output_dir = REPO_ROOT / "reports" / "research"
        output_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "monthly": output_dir / "monthly_summary.md",
            "yearly": output_dir / "yearly_summary.md",
            "hypothesis": output_dir / "hypothesis_status.md",
        }
        files["monthly"].write_text(cls._summary(rows, "month"), encoding="utf-8")
        files["yearly"].write_text(cls._summary(rows, "year"), encoding="utf-8")
        files["hypothesis"].write_text(HypothesisTracker().status_report(rows), encoding="utf-8")
        return {name: str(path.relative_to(REPO_ROOT)) for name, path in files.items()}

    @classmethod
    def write_dashboard(cls, rows: list[dict[str, Any]]) -> Path:
        output_dir = REPO_ROOT / "reports" / "research"
        output_dir.mkdir(parents=True, exist_ok=True)
        path = output_dir / "notebook_dashboard.json"
        path.write_text(json.dumps({"entries": rows, "entry_count": len(rows)}, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    @classmethod
    def _summary(cls, rows: list[dict[str, Any]], period: str) -> str:
        title = "Monthly Summary" if period == "month" else "Yearly Summary"
        buckets: dict[str, list[dict[str, Any]]] = {}
        for row in rows:
            key = str(row.get("date", ""))[:7 if period == "month" else 4] or "Unknown"
            buckets.setdefault(key, []).append(row)
        lines = [f"# Research {title}", "", "Research Notebook records why Compass changed, what was tested, and what was learned.", ""]
        if not buckets:
            lines.append("- No research entries yet.")
        for key, items in sorted(buckets.items(), reverse=True):
            lines.extend([f"## {key}", "", f"- Entries: {len(items)}"])
            categories: dict[str, int] = {}
            for item in items:
                categories[item.get("category", "General")] = categories.get(item.get("category", "General"), 0) + 1
            for category, count in sorted(categories.items()):
                lines.append(f"- {category}: {count}")
            lines.append("")
        return "\n".join(lines)

    @classmethod
    def _load_index(cls) -> list[dict[str, Any]]:
        if not cls.index_path.exists():
            return cls.rebuild_index()
        try:
            data = json.loads(cls.index_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
        return data if isinstance(data, list) else []

    @staticmethod
    def _load_metadata(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return [data]
        return []


if __name__ == "__main__":
    index = Notebook.rebuild_index()
    outputs = Notebook.write_reports(index)
    print({"success": True, "entries": len(index), "index": str(Notebook.index_path.relative_to(REPO_ROOT)), "outputs": outputs})

