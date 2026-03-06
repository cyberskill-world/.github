# Releasing

## How Actions Are Released

This repository uses a **main-branch rolling release** model. All actions reference `@main`:

```yaml
uses: cyberskill-world/.github/actions/<action-name>@main
```

Changes merged to `main` are **immediately available** to all consuming repositories.

## Change Process

1. **Create a branch** from `main`
2. **Make changes** and ensure CI passes (YAML lint, actionlint, SHA pin check, ShellCheck)
3. **Open a PR** and request review from `@cyberskill-world/core`
4. **Merge** — changes propagate to all org repos on next workflow run

## Breaking Changes

Since all repos consume actions from `@main`, breaking changes require coordination:

1. Announce the change in a PR description with `⚠️ BREAKING` label
2. Update all consuming repos in the same PR batch (or coordinate timing)
3. Consider adding backward-compatible input defaults to avoid breakage

## Versioning

> **Note:** The SemVer tags described below are **org-wide tag protection rules** enforced by `settings.yml`. They apply to all CyberSkill repositories that use Git tags for releases (e.g., npm packages, Tauri apps). They are **not** used for consuming these shared actions — actions always reference `@main`.

- **Tags** follow [Semantic Versioning](https://semver.org/) and are enforced by the `settings.yml` rulesets
- Tag protection rules prevent deletion and non-fast-forward updates
- Tag names must match the SemVer pattern (e.g., `1.0.0`, `2.1.0-beta.1`)

## CI Validation

Every PR is validated by the CI workflow:

| Check | Tool | Purpose |
|-------|------|---------|
| YAML Lint | `yamllint` | Validates YAML syntax and style |
| Action Schemas | `actionlint` | Validates workflow and action definitions |
| SHA Pinning | Custom script | Ensures all external `uses:` are SHA-pinned |
| Shell Scripts | `shellcheck` | Lints shell scripts in `scripts/` |
