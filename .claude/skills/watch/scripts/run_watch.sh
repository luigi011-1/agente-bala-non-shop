#!/usr/bin/env bash
# Compatibility with existing production commands; delegate to the canonical /watch.
set -euo pipefail
watch_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
exec bash "$watch_root/.agents/skills/watch/scripts/run_watch.sh" "$@"
