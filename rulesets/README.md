# Rulesets

This directory contains **template rulesets** for GitHub branch and tag protection.

## Usage

These JSON files are reference templates — not automatically applied org-wide. To apply a ruleset to a new repository:

1. Copy the relevant JSON file
2. Update the `source` field with your repository name
3. Import via **Settings → Rules → Rulesets → Import**

## Templates

| File | Purpose |
|---|---|
| `Branches.json` | Branch protection: PR reviews, stale review dismissal, linear history |
