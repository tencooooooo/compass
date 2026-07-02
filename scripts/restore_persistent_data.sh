#!/usr/bin/env bash
set -euo pipefail

# データ専用ブランチから memory/ と storage/notifications/ を復元します。
# git restore --worktree で作業ツリーのみ更新し、indexには手を付けません。

DATA_BRANCH="${COMPASS_DATA_BRANCH:-compass-data}"

mkdir -p memory storage/notifications

git fetch origin "${DATA_BRANCH}" || true
if git show-ref --verify --quiet "refs/remotes/origin/${DATA_BRANCH}"; then
  git restore --source="origin/${DATA_BRANCH}" --worktree -- memory || true
  git restore --source="origin/${DATA_BRANCH}" --worktree -- storage/notifications || true
  echo "Restored persistent Compass data from ${DATA_BRANCH}."
else
  echo "No ${DATA_BRANCH} branch found. Cache fallback or empty memory will be used."
fi
