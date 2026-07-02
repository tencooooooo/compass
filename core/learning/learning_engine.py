from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]

from core.learning.learning_history import append_learning_rows  # noqa: E402
from core.learning.learning_package_builder import (  # noqa: E402
    build_learning_metrics,
    render_learning_package,
    render_learning_summary,
)
from core.learning.proposal_loader import (  # noqa: E402
    approved_proposals,
    proposal_markdown_by_id,
    proposal_status_counts,
    related_knowledge_candidate,
)
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402


SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
PROPOSAL_DIR = PROJECT_ROOT / "reports" / "proposals"
PROPOSAL_INDEX_PATH = PROPOSAL_DIR / "proposal_index.json"
KNOWLEDGE_UPDATE_DIR = PROJECT_ROOT / "reports" / "knowledge_updates"
LEARNING_REPORT_DIR = PROJECT_ROOT / "reports" / "learning"
LEARNING_HISTORY_PATH = PROJECT_ROOT / "memory" / "learning" / "learning_history.json"
KNOWLEDGE_VERSION = "v1"


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    settings = load_yaml(SETTINGS_PATH)
    logger = setup_logger(PROJECT_ROOT, settings, "compass.learning")
    timezone = get_timezone(settings)
    now = datetime.now(timezone)
    date_key = now.strftime("%Y-%m-%d")

    logger.info("Compass Core 04 - Learning Engine")
    approved = approved_proposals(PROPOSAL_INDEX_PATH)
    status_counts = proposal_status_counts(PROPOSAL_INDEX_PATH)

    history = append_learning_rows(LEARNING_HISTORY_PATH, approved, now.isoformat(), KNOWLEDGE_VERSION)
    proposal_details = {
        str(item.get("proposal_id")): proposal_markdown_by_id(PROPOSAL_DIR, str(item.get("proposal_id")))
        for item in approved
    }
    knowledge_candidates = {
        str(item.get("proposal_id")): related_knowledge_candidate(KNOWLEDGE_UPDATE_DIR, str(item.get("proposal_id")))
        for item in approved
    }
    metrics = build_learning_metrics(status_counts, len(approved), KNOWLEDGE_VERSION)

    LEARNING_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    package_path = LEARNING_REPORT_DIR / f"learning_package_{date_key}.md"
    package_path.write_text(
        render_learning_package(date_key, approved, proposal_details, knowledge_candidates, history, KNOWLEDGE_VERSION),
        encoding="utf-8",
    )
    (LEARNING_REPORT_DIR / "learning_summary.md").write_text(
        render_learning_summary(date_key, metrics, approved),
        encoding="utf-8",
    )
    write_json(LEARNING_REPORT_DIR / "learning_metrics.json", metrics)

    logger.info("Approved proposals loaded: %s", len(approved))
    logger.info("Learning package saved: %s", package_path)
    logger.info("Learning history saved: %s", LEARNING_HISTORY_PATH)
    logger.info("Knowledge was not updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
