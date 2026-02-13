## 2024-02-14 - Centralized Dependency Caching in Composite Actions
**Learning:** Composite actions often centralize setup steps like dependency installation. Missing caching in these shared actions propagates inefficiency to every workflow that uses them.
**Action:** Always verify `actions/setup-node` (and similar setup actions) includes `cache: 'pnpm'` (or npm/yarn) in shared `env-deps` actions.

## 2024-05-22 - Composite Action Resource Paths
**Learning:** When using `actions/setup-python` caching in composite actions, the `cache-dependency-path` must use the absolute path `${{ github.action_path }}/requirements.txt` if a requirements file is used.
**Action:** Use `${{ github.action_path }}` to locate resources relative to the action directory in composite actions.
