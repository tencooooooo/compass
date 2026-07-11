#!/usr/bin/env bash
set -euo pipefail

# データ専用ブランチからMemoryと再現に必要な運用データを復元します。
# git restore --worktree で作業ツリーのみ更新し、indexには手を付けません。

DATA_BRANCH="${COMPASS_DATA_BRANCH:-compass-data}"
PERSISTENT_PATHS=(
  memory
  storage/notifications
  storage/raw/prices
  storage/raw/companies
  storage/raw/financials
  storage/raw/news
  storage/events
  storage/knowledge_graph
  reports/discovery
  reports/scoring
  reports/market
  reports/validation
  reports/feedback
  reports/proposals
  reports/knowledge_updates
  reports/learning
  reports/themes
  reports/patterns
  reports/performance
  reports/strategy
  reports/experiments
  reports/graph
)

mkdir -p memory storage/notifications reports

git fetch origin "${DATA_BRANCH}" || true
if git show-ref --verify --quiet "refs/remotes/origin/${DATA_BRANCH}"; then
  for path in "${PERSISTENT_PATHS[@]}"; do
    if git cat-file -e "origin/${DATA_BRANCH}:${path}" 2>/dev/null; then
      mkdir -p "$(dirname "${path}")"
      git restore --source="origin/${DATA_BRANCH}" --worktree -- "${path}"
    fi
  done
  echo "Restored persistent Compass data from ${DATA_BRANCH}."
else
  echo "No ${DATA_BRANCH} branch found. Cache fallback or empty memory will be used."
fi
