## 2024-02-14 - Centralized Dependency Caching in Composite Actions
**Learning:** Composite actions often centralize setup steps like dependency installation. Missing caching in these shared actions propagates inefficiency to every workflow that uses them.
**Action:** Always verify `actions/setup-node` (and similar setup actions) includes `cache: 'pnpm'` (or npm/yarn) in shared `env-deps` actions.
