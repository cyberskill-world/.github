## 2025-01-22 - [Avoid Alpha/Non-Standard Python Versions in CI]
**Learning:** Using a Python version that is not pre-installed on GitHub Actions runners (e.g., `3.14.3` alpha) forces `actions/setup-python` to download and compile it from source, adding significant overhead (30s to minutes) to every workflow run.
**Action:** Always prefer stable Python versions (e.g., `3.12`, `3.13`) that are pre-cached on runners unless a specific bleeding-edge feature is strictly required. This ensures near-instant setup.
