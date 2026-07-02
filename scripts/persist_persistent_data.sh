#!/usr/bin/env bash
set -euo pipefail

DATA_BRANCH="${COMPASS_DATA_BRANCH:-compass-data}"
TEMP_DIR="$(mktemp -d)"

mkdir -p "${TEMP_DIR}/storage"
if [ -d memory ]; then
  cp -R memory "${TEMP_DIR}/memory"
else
  mkdir -p "${TEMP_DIR}/memory"
fi

if [ -d storage/notifications ]; then
  cp -R storage/notifications "${TEMP_DIR}/storage/notifications"
else
  mkdir -p "${TEMP_DIR}/storage/notifications"
fi

rm -rf memory storage/notifications

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

git fetch origin "${DATA_BRANCH}" || true
if git show-ref --verify --quiet "refs/remotes/origin/${DATA_BRANCH}"; then
  git checkout -B "${DATA_BRANCH}" "origin/${DATA_BRANCH}"
else
  git checkout --orphan "${DATA_BRANCH}"
  git rm -r --cached . || true
fi

rm -rf memory storage/notifications
mkdir -p storage
cp -R "${TEMP_DIR}/memory" ./memory
cp -R "${TEMP_DIR}/storage/notifications" ./storage/notifications

git add -f memory storage/notifications
if git diff --cached --quiet; then
  echo "No persistent Compass data changes to commit."
else
  git commit -m "Persist Compass memory data ${GITHUB_RUN_ID:-local}"
  git push origin "${DATA_BRANCH}"
fi
