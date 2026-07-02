from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any


class DuplicateDetector:
    """Detects duplicate files by content hash."""

    def detect(self, files: list[Path]) -> dict[str, Any]:
        hashes: dict[str, list[str]] = {}
        for path in files:
            try:
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
            except OSError:
                continue
            hashes.setdefault(digest, []).append(str(path))
        groups = [paths for paths in hashes.values() if len(paths) > 1]
        duplicate_count = sum(len(paths) - 1 for paths in groups)
        score = max(0, 100 - duplicate_count * 10)
        return {"score": score, "duplicate_count": duplicate_count, "groups": groups}

