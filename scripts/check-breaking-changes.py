#!/usr/bin/env python3
"""Compare required action inputs between base and PR versions.

Detects breaking changes where required inputs are removed.

Usage:
    python3 scripts/check-breaking-changes.py <base_file> <pr_file>

Exit codes:
    0 - No breaking changes
    1 - Breaking changes detected (removed required inputs)
"""

import sys

import yaml


def get_required_inputs(filepath):
    """Extract required input names from an action.yml file."""
    with open(filepath) as f:
        data = yaml.safe_load(f) or {}
    inputs = data.get("inputs", {}) or {}
    return sorted(name for name, props in inputs.items() if props.get("required", False))


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <base_file> <pr_file>", file=sys.stderr)
        sys.exit(2)

    base_file = sys.argv[1]
    pr_file = sys.argv[2]

    base_inputs = set(get_required_inputs(base_file))
    pr_inputs = set(get_required_inputs(pr_file))

    removed = base_inputs - pr_inputs
    if removed:
        for name in sorted(removed):
            print(f"REMOVED: {name}")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
