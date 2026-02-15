## 2025-01-22 - [Avoid Alpha/Non-Standard Python Versions in CI]
**Learning:** Using a Python version that is not pre-installed on GitHub Actions runners (e.g., `3.14.3` alpha) forces `actions/setup-python` to download and compile it from source, adding significant overhead (30s to minutes) to every workflow run.
**Action:** Always prefer stable Python versions (e.g., `3.12`, `3.13`) that are pre-cached on runners unless a specific bleeding-edge feature is strictly required. This ensures near-instant setup.

## 2026-02-15 - Git Fetch Optimization for Deployments
**Learning:** Fetching all branches (`git fetch origin`) in deployment scripts is wasteful for large repositories. Targeting a specific branch via refspec (`git fetch origin +refs/heads/$BRANCH:refs/remotes/origin/$BRANCH`) significantly reduces data transfer and time. A fallback to general fetch (`|| git fetch origin $BRANCH`) is necessary to support tags or non-standard refs.
**Action:** When optimizing deployment scripts, always prefer targeted fetches over full fetches, ensuring to handle both branches (updating remote tracking refs) and tags.
