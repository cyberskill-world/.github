#!/usr/bin/env bash
# Shared branch-name validation for reusable GitHub Actions.
# Usage: source this file, then call `validate_branch "LABEL" "$BRANCH_VAR"`

set -euo pipefail

validate_branch() {
  local name="$1"
  local value="$2"

  if [[ -z "$value" ]]; then
    echo "❌ Invalid branch name for $name: must not be empty" >&2
    exit 1
  fi

  if [[ "$value" == -* ]]; then
    echo "❌ Invalid branch name for $name: must not start with '-'" >&2
    exit 1
  fi

  if [[ "$value" == *:* ]]; then
    echo "❌ Invalid branch name for $name: must not contain ':' (refspecs are not allowed)" >&2
    exit 1
  fi

  if [[ "$value" == refs/* ]]; then
    echo "❌ Invalid branch name for $name: must not start with 'refs/'" >&2
    exit 1
  fi

  if ! git check-ref-format --branch "$value" > /dev/null 2>&1; then
    echo "❌ Invalid branch name for $name: '$value' is not a valid Git branch" >&2
    exit 1
  fi
}
