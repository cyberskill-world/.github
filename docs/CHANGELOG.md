# Changelog

All notable changes to the CyberSkill `.github` shared actions and configurations are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [2.0.0] — 2026-03-06

### Added
- `deploy` action: `BUILD_COMMAND` and `RELOAD_COMMAND` inputs for flexible project setups
- `create-pr` action: `LABELS` and `ASSIGNEES` optional inputs
- `create-pr` action: Branch input validation via shared `validate-branch.sh`
- `env-deps` action: Secret-pattern scanning guard for `.env.example`
- `trigger-events` action: `REPO` format validation (`owner/repo`)
- `test` action: Multi-metric coverage threshold (lines, branches, functions, statements)
- CI: `dependency-review` job for PR vulnerability scanning
- CI: `settings-validation` job for `settings.yml` schema validation
- `CHANGELOG.md` (this file)
- `.editorconfig` for consistent editor settings
- Per-action minimum permissions documented in README

### Changed
- `deploy` action: Replace `eval` with `bash -c` for build/reload commands (security hardening)
- `deploy` action: Health check messages now print before sleep delay
- `security-audit` action: Upload step now runs on failure (`if: always()`)
- `merge` / `rebase` actions: Log resulting commit SHA after push
- `CONTRIBUTING.md`: Pin `actionlint` version to match CI
- `RELEASING.md`: Clarify tag vs. `@main` release model
- CI ShellCheck: Pass file path via env var for safety
- Renovate: Disable automerge for major GitHub Actions updates

### Removed
- `deploy` action: `PASSWORD` input (use `KEY`-based auth instead)
- `deploy` action: `eval` usage (replaced with `bash -c`)

---

## [1.0.0] — 2025-01-01

### Added
- Initial set of 12 reusable composite actions
- CI validation workflow (YAML lint, actionlint, SHA pinning, ShellCheck, CODEOWNERS, breaking changes, README sync)
- Organization-wide tag protection rulesets (`settings.yml`)
- Renovate configuration for automated dependency updates
- Community health files (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, RELEASING)
- PR and issue templates
- CODEOWNERS with `@cyberskill-world/core` ownership

