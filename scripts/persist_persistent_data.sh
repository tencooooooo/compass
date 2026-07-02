#!/usr/bin/env bash
set -euo pipefail

# memory/ と storage/notifications/ をデータ専用ブランチへ保存します。
# メインの作業ツリーはブランチ切替せず、git worktreeで隔離したコピー上で操作します。

DATA_BRANCH="${COMPASS_DATA_BRANCH:-compass-data}"
WORKTREE_DIR="$(mktemp -d)"

cleanup() {
  git worktree remove --force "${WORKTREE_DIR}" 2>/dev/null || true
  rm -rf "${WORKTREE_DIR}" 2>/dev/null || true
}
trap cleanup EXIT

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

git fetch origin "${DATA_BRANCH}" || true
if git show-ref --verify --quiet "refs/remotes/origin/${DATA_BRANCH}"; then
  git worktree add -B "${DATA_BRANCH}" "${WORKTREE_DIR}" "origin/${DATA_BRANCH}"
else
  # データブランチが無い場合は、ソース履歴と切り離した空コミットから開始します。
  EMPTY_TREE="$(git hash-object -t tree /dev/null)"
  FIRST_COMMIT="$(git commit-tree "${EMPTY_TREE}" -m "Initialize Compass data branch")"
  git branch -f "${DATA_BRANCH}" "${FIRST_COMMIT}"
  git worktree add "${WORKTREE_DIR}" "${DATA_BRANCH}"
fi

rm -rf "${WORKTREE_DIR}/memory" "${WORKTREE_DIR}/storage/notifications"
mkdir -p "${WORKTREE_DIR}/storage"

if [ -d memory ]; then
  cp -R memory "${WORKTREE_DIR}/memory"
else
  mkdir -p "${WORKTREE_DIR}/memory"
fi

if [ -d storage/notifications ]; then
  cp -R storage/notifications "${WORKTREE_DIR}/storage/notifications"
else
  mkdir -p "${WORKTREE_DIR}/storage/notifications"
fi

git -C "${WORKTREE_DIR}" add -f memory storage/notifications
if git -C "${WORKTREE_DIR}" diff --cached --quiet; then
  echo "No persistent Compass data changes to commit."
else
  git -C "${WORKTREE_DIR}" commit -m "Persist Compass memory data ${GITHUB_RUN_ID:-local}"
  git -C "${WORKTREE_DIR}" push origin "${DATA_BRANCH}"
fi
