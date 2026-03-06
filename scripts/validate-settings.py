#!/usr/bin/env python3
"""Validate settings.yml structure against known schema constraints.

Checks:
- Required 'rulesets' key
- Valid actor_type values in bypass_actors
- Valid rule type values in rules

Usage:
    python3 scripts/validate-settings.py [settings_file]
    Defaults to 'settings.yml' if no argument is provided.
"""

import sys

import yaml

VALID_ACTOR_TYPES = {
    "OrganizationAdmin",
    "RepositoryRole",
    "Team",
    "Integration",
    "DeployKey",
}
VALID_RULE_TYPES = {
    "deletion",
    "non_fast_forward",
    "tag_name_pattern",
    "creation",
    "update",
    "required_linear_history",
}


def main():
    settings_file = sys.argv[1] if len(sys.argv) > 1 else "settings.yml"

    with open(settings_file) as f:
        data = yaml.safe_load(f)

    if not data or "rulesets" not in data:
        print(f"::error::{settings_file} must contain a 'rulesets' key")
        sys.exit(1)

    errors = 0
    for i, ruleset in enumerate(data["rulesets"]):
        name = ruleset.get("name", f"ruleset[{i}]")
        for bypass in ruleset.get("bypass_actors", []):
            at = bypass.get("actor_type")
            if at and at not in VALID_ACTOR_TYPES:
                print(f"::error::Ruleset '{name}': invalid actor_type '{at}'")
                errors += 1
        for rule in ruleset.get("rules", []):
            rt = rule.get("type")
            if rt not in VALID_RULE_TYPES:
                print(f"::error::Ruleset '{name}': invalid rule type '{rt}'")
                errors += 1

    if errors > 0:
        print(f"::error::Found {errors} settings.yml validation error(s)")
        sys.exit(1)
    print(f"✅ {settings_file} schema is valid.")


if __name__ == "__main__":
    main()
