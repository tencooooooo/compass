#!/usr/bin/env bash
set -euo pipefail

DATA_BRANCH="${COMPASS_DATA_BRANCH:-compass-data}"

mkdir -p memory storage/notifications

git fetch origin "${DATA_BRANCH}" || true
if git show-ref --verify --quiet "refs/remotes/origin/${DATA_BRANCH}"; then
  git checkout "origin/${DATA_BRANCH}" -- memory || true
  git checkout "origin/${DATA_BRANCH}" -- storage/notifications || true
  echo "Restored persistent Compass data from ${DATA_BRANCH}."
else
  echo "No ${DATA_BRANCH} branch found. Cache fallback or empty memory will be used."
fi
