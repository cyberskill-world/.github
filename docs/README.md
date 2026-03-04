# CyberSkill `.github`

Organization-level defaults, **reusable composite actions**, branch/tag rulesets, and community health files for all [CyberSkill](https://github.com/cyberskill-world) repositories.

## 📦 Reusable Actions

All actions live under `actions/` and can be referenced by any repo in the org:

```yaml
uses: cyberskill-world/.github/actions/<action-name>@main
```

| Action | Description |
| ------ | ----------- |
| [`env-deps`](../actions/env-deps) | Sets up pnpm, Node.js, `.env`, and installs dependencies |
| [`build`](../actions/build) | Runs `pnpm build` and optionally uploads artifacts |
| [`lint`](../actions/lint) | Runs YAML lint + `pnpm lint` |
| [`lint-yaml`](../actions/lint-yaml) | Standalone YAML linting via `yamllint` |
| [`test`](../actions/test) | Runs `pnpm test` with optional coverage upload |
| [`security-audit`](../actions/security-audit) | Runs `pnpm audit` with configurable severity threshold |
| [`deploy`](../actions/deploy) | SSH deploy with health-check and automatic rollback |
| [`create-pr`](../actions/create-pr) | Creates a pull request via `gh` CLI (idempotent) |
| [`merge`](../actions/merge) | Merges one branch into another with strategy option |
| [`rebase`](../actions/rebase) | Rebases a branch onto another |
| [`match-branch`](../actions/match-branch) | Checks branch match and sets `matched` output |
| [`trigger-events`](../actions/trigger-events) | Fires `repository_dispatch` events with concurrency control |

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

## 🤖 CI for This Repo

The [CI workflow](../.github/workflows/ci.yml) validates this repo itself:

1. **Validate YAML** — `yamllint` on all YAML files
2. **Validate Action Schemas** — `actionlint` on all workflow/action files
3. **Verify SHA Pinning** — Ensures all external `uses:` are pinned to full commit SHAs
4. **Lint Shell Scripts** — `shellcheck` on all scripts

## 📋 Other Config

| File | Purpose |
| ---- | ------- |
| [`CODEOWNERS`](../CODEOWNERS) | Auto-assigns `@cyberskill-world/core` for reviews |
| [`renovate.json`](../renovate.json) | Automated dependency updates (pnpm + GitHub Actions) |
| [`.yamllint`](../.yamllint) | Shared YAML lint configuration |
