from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]

from core.decision.proposal_generator import (  # noqa: E402
    build_proposals,
    render_knowledge_update_candidate,
    render_proposal_markdown,
)
from core.decision.review_manager import ReviewManager  # noqa: E402
from utils.config import load_yaml  # noqa: E402
from utils.logger import get_timezone, setup_logger  # noqa: E402


SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.yaml"
FEEDBACK_HISTORY_PATH = PROJECT_ROOT / "reports" / "feedback" / "feedback_history.json"
FEEDBACK_MEMORY_PATH = PROJECT_ROOT / "memory" / "feedback" / "feedback_history.json"
PROPOSAL_DIR = PROJECT_ROOT / "reports" / "proposals"
KNOWLEDGE_UPDATE_DIR = PROJECT_ROOT / "reports" / "knowledge_updates"
PROPOSAL_INDEX_PATH = PROPOSAL_DIR / "proposal_index.json"
PROPOSAL_STATE_PATH = PROJECT_ROOT / "memory" / "decision" / "proposal_index.json"


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    settings = load_yaml(SETTINGS_PATH)
    logger = setup_logger(PROJECT_ROOT, settings, "compass.decision")
    timezone = get_timezone(settings)
    now = datetime.now(timezone)
    timestamp = now.isoformat()
    date_key = now.strftime("%Y-%m-%d")

    logger.info("Compass Core 03 - Decision Engine")
    feedback_history = load_json(FEEDBACK_MEMORY_PATH, load_json(FEEDBACK_HISTORY_PATH, []))
    if not isinstance(feedback_history, list):
        feedback_history = []

    proposals = build_proposals(feedback_history, date_key, timestamp)
    PROPOSAL_DIR.mkdir(parents=True, exist_ok=True)
    KNOWLEDGE_UPDATE_DIR.mkdir(parents=True, exist_ok=True)

    proposal_path = PROPOSAL_DIR / f"proposal_{date_key}.md"
    proposal_path.write_text(render_proposal_markdown(proposals, date_key), encoding="utf-8")

    candidate_path = KNOWLEDGE_UPDATE_DIR / f"candidate_{date_key}.md"
    candidate_path.write_text(render_knowledge_update_candidate(proposals, date_key), encoding="utf-8")

    review_manager = ReviewManager(PROPOSAL_INDEX_PATH, PROPOSAL_STATE_PATH)
    for proposal in proposals:
        review_manager.upsert_pending(proposal)

    logger.info("Proposal report saved: %s", proposal_path)
    logger.info("Knowledge update candidate saved: %s", candidate_path)
    logger.info("Proposal count: %s", len(proposals))
    logger.info("Knowledge was not updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
