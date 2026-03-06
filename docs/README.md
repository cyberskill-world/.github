# CyberSkill `.github`

Organization-level defaults, **reusable composite actions**, branch/tag rulesets, and community health files for all [CyberSkill](https://github.com/cyberskill-world) repositories.

## 📦 Reusable Actions

All actions live under `actions/` and can be referenced by any repo in the org:

```yaml
uses: cyberskill-world/.github/actions/<action-name>@main
```

| Action | Description | Key Inputs |
| ------ | ----------- | ---------- |
| [`env-deps`](../actions/env-deps) | Sets up pnpm, Node.js, `.env`, and installs dependencies | `NODE_VERSION` (default: `24.12.0`), `PNPM_VERSION` (default: `10.29.3`) |
| [`build`](../actions/build) | Runs `pnpm build` and optionally uploads artifacts | `BUILD_ARTIFACT_NAME`, `BUILD_PATH`, `RETENTION_DAYS` |
| [`lint`](../actions/lint) | Runs YAML lint + `pnpm lint` (with optional `SKIP_YAML_LINT` input) | `SKIP_YAML_LINT` |
| [`lint-yaml`](../actions/lint-yaml) | Standalone YAML linting via `yamllint` | — |
| [`test`](../actions/test) | Runs `pnpm test` with optional coverage upload and multi-metric threshold | `COVERAGE`, `COVERAGE_THRESHOLD`, `COVERAGE_ARTIFACT_NAME` |
| [`security-audit`](../actions/security-audit) | Runs `pnpm audit` with configurable severity threshold | `AUDIT_LEVEL` (default: `high`), `OUTPUT_FORMAT` |
| [`deploy`](../actions/deploy) | SSH deploy with health-check and automatic rollback | `HOST`\*, `KEY`\*, `PATH`\*, `BRANCH`\*, `BUILD_COMMAND`, `RELOAD_COMMAND` |
| [`create-pr`](../actions/create-pr) | Creates a pull request via `gh` CLI (idempotent) | `GH_TOKEN`\*, `FROM`\*, `TO`\*, `LABELS`, `ASSIGNEES` |
| [`merge`](../actions/merge) | Merges one branch into another with strategy option | `GH_TOKEN`\*, `FROM`\*, `TO`\*, `CHOOSE_STRATEGY` |
| [`rebase`](../actions/rebase) | Rebases a branch onto another | `GH_TOKEN`\*, `FROM`\*, `TO`\*, `DRY_RUN` |
| [`match-branch`](../actions/match-branch) | Checks branch match and sets `matched` output | `BRANCH`\* |
| [`trigger-events`](../actions/trigger-events) | Fires `repository_dispatch` events with concurrency control | `GH_TOKEN`\*, `REPO`\*, `EVENTS`\* |

\* = required

### Permissions Reference

Minimum GitHub token permissions required by each action:

| Action | Required Permissions |
| ------ | -------------------- |
| `env-deps` | `contents: read` |
| `build` | `contents: read` (+ `actions: write` if uploading artifacts) |
| `lint` | `contents: read` |
| `lint-yaml` | `contents: read` |
| `test` | `contents: read` (+ `actions: write` if uploading coverage) |
| `security-audit` | `contents: read` (+ `actions: write` if uploading report) |
| `deploy` | None (runs on remote SSH server) |
| `create-pr` | `contents: write`, `pull-requests: write` |
| `merge` | `contents: write` |
| `rebase` | `contents: write` |
| `match-branch` | `contents: read` |
| `trigger-events` | — requires a PAT or GitHub App with `repo` scope |

### Quick Start

A typical CI pipeline using these actions:

```yaml
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd  # v6.0.2

      - name: Setup environment
        uses: cyberskill-world/.github/actions/env-deps@main

      - name: Security Audit
        uses: cyberskill-world/.github/actions/security-audit@main

      - name: Lint
        uses: cyberskill-world/.github/actions/lint@main

      - name: Test
        uses: cyberskill-world/.github/actions/test@main

      - name: Build
        uses: cyberskill-world/.github/actions/build@main
        with:
          BUILD_ARTIFACT_NAME: my-app
```

## 🛡️ Rulesets

| Ruleset | Scope | Key Rules |
| ------- | ----- | --------- |
| **Tags** (`settings.yml`) | All repos | Deletion protection, non-fast-forward block, SemVer name pattern |
| **Branches** (`rulesets/`) | Per-repo | PR review required, stale review dismissal, linear history |

## 📄 Community Health Files

Default [community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file) inherited by all repos:

- [CONTRIBUTING.md](CONTRIBUTING.md) — How to fork, branch, and contribute
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Contributor Covenant v2.1
- [SECURITY.md](SECURITY.md) — Vulnerability reporting & disclosure policy
- [RELEASING.md](RELEASING.md) — How actions are released and versioned

## 🤖 CI for This Repo

The [CI workflow](../.github/workflows/ci.yml) validates this repo itself:

1. **Validate YAML** — `yamllint` on all YAML files
2. **Validate Action Schemas** — `actionlint` on all workflow/action files
3. **Verify SHA Pinning** — Ensures all external `uses:` are pinned to full commit SHAs
4. **Validate Inlined Code Sync** — Ensures duplicated functions stay in sync
5. **Lint Shell Scripts** — `shellcheck` on all scripts (standalone + inline)
6. **Validate CODEOWNERS** — Syntax validation for ownership rules
7. **Detect Breaking Changes** — Flags removed required inputs (override with label)
8. **Verify README Sync** — Ensures all actions are documented
9. **Dependency Review** — Scans PR dependencies for known vulnerabilities (PR only)
10. **Validate Settings Schema** — Validates `settings.yml` structure and values

## 📋 Other Config

| File | Purpose |
| ---- | ------- |
| [`CODEOWNERS`](../CODEOWNERS) | Auto-assigns `@cyberskill-world/core` for reviews |
| [`renovate.json`](../renovate.json) | Automated dependency updates (pnpm + GitHub Actions) |
| [`.yamllint`](../.yamllint) | Shared YAML lint configuration |
| [`.editorconfig`](../.editorconfig) | Consistent editor settings (indent, line endings) |
| [`CHANGELOG.md`](CHANGELOG.md) | Notable changes to actions and configurations |
