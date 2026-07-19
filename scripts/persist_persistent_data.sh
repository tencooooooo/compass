#!/usr/bin/env bash
set -euo pipefail

# Memoryと再現に必要な運用データをデータ専用ブランチへ保存します。
# メインの作業ツリーはブランチ切替せず、git worktreeで隔離したコピー上で操作します。

DATA_BRANCH="${COMPASS_DATA_BRANCH:-compass-data}"
WORKTREE_DIR="$(mktemp -d)"
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

mkdir -p "${WORKTREE_DIR}/memory" "${WORKTREE_DIR}/storage" "${WORKTREE_DIR}/reports"
for path in "${PERSISTENT_PATHS[@]}"; do
  if [ ! -e "${path}" ]; then
    continue
  fi
  target="${WORKTREE_DIR}/${path}"
  rm -rf "${target}"
  mkdir -p "$(dirname "${target}")"
  cp -R "${path}" "${target}"
done

git -C "${WORKTREE_DIR}" add -A -f -- memory storage reports
if git -C "${WORKTREE_DIR}" diff --cached --quiet; then
  echo "No persistent Compass data changes to commit."
else
  git -C "${WORKTREE_DIR}" commit -m "Persist Compass operational data ${GITHUB_RUN_ID:-local}"
  git -C "${WORKTREE_DIR}" push origin "${DATA_BRANCH}"
fi

# データブランチの履歴は保存媒体としてのみ使うため、コミットが溜まりすぎたら
# 最新ツリーだけの1コミットへ畳み、リポジトリの肥大化を防ぎます。
# 400コミット ≒ 日次+週次で約1年分。concurrencyグループで直列化されている前提です。
SQUASH_THRESHOLD="${COMPASS_DATA_SQUASH_THRESHOLD:-400}"
COMMIT_COUNT="$(git -C "${WORKTREE_DIR}" rev-list --count HEAD)"
if [ "${COMMIT_COUNT}" -gt "${SQUASH_THRESHOLD}" ]; then
  SQUASHED="$(git -C "${WORKTREE_DIR}" commit-tree "HEAD^{tree}" -m "Squash Compass data history (${COMMIT_COUNT} commits)")"
  git -C "${WORKTREE_DIR}" reset --hard "${SQUASHED}"
  git -C "${WORKTREE_DIR}" push --force origin "${DATA_BRANCH}"
  echo "Squashed ${DATA_BRANCH} history: ${COMMIT_COUNT} commits -> 1."
fi
