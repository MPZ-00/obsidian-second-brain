#!/usr/bin/env bash
# Runs "$@" with the first available interpreter: uv, python3, python.
# Single source of truth for hook wiring - hooks/hooks.json, scripts/setup.sh,
# scripts/setup_settings_hook.py, and install.sh all call this instead of each
# picking an interpreter their own way.
set -euo pipefail

runners=("uv run --no-project" "python3" "python")
for candidate in "${runners[@]}"; do
  read -ra parts <<< "$candidate"
  if command -v "${parts[0]}" >/dev/null 2>&1; then
    exec "${parts[@]}" "$@"
  fi
done

echo "run_python.sh: no interpreter found (need uv, python3, or python)" >&2
exit 1
