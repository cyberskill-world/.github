## 2024-02-14 - Centralized Dependency Caching in Composite Actions
**Learning:** Composite actions often centralize setup steps like dependency installation. Missing caching in these shared actions propagates inefficiency to every workflow that uses them.
**Action:** Always verify `actions/setup-node` (and similar setup actions) includes `cache: 'pnpm'` (or npm/yarn) in shared `env-deps` actions.

## 2025-05-23 - GitHub Actions Python Caching
**Learning:** `actions/setup-python`'s `cache-dependency-path` often fails to cache dependencies correctly when pointing to files outside the GitHub Actions workspace (e.g., using `${{ github.action_path }}`).
**Action:** When using `actions/setup-python` inside a composite action, copy the requirements file (e.g., `requirements.txt`) from `${{ github.action_path }}` to the current workspace (e.g., `.github-action-requirements.txt`) before the setup step. This ensures the dependency file is hashable and caching works reliably.
