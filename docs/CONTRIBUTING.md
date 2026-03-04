# Contributing

## Request for changes/ Pull Requests
You first need to create a fork of the [.github](https://github.com/cyberskill-world/.github/) repository to commit your changes to it. Methods to fork a repository can be found in the [GitHub Documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

Then add your fork as a local project:

```sh
# Using HTTPS
git clone https://github.com/cyberskill-world/.github.git

# Using SSH
git clone git@github.com:cyberskill-world/.github.git
```

> [Which remote URL should be used ?](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories)

Then, go to your local folder

```sh
cd .github
```

Add git remote controls :

```sh
# Using HTTPS
git remote add fork https://github.com/YOUR-USERNAME/.github.git
git remote add upstream https://github.com/cyberskill-world/.github.git


# Using SSH
git remote add fork git@github.com:YOUR-USERNAME/.github.git
git remote add upstream git@github.com:cyberskill-world/.github.git
```

You can now verify that you have your two git remotes:

```sh
git remote -v
```

## Receive remote updates
In view of staying up to date with the central repository :

```sh
git pull upstream main
```

## Choose a base branch
Before starting development, you need to know which branch to base your modifications/additions on. When in doubt, use main.

| Type of change                |           | Branches              |
| :------------------           |:---------:| ---------------------:|
| Documentation                 |           | `main`              |
| Bug fixes                     |           | `main`              |
| New features                  |           | `main`              |
| New issues models             |           | `main`              |

```sh
# Switch to the desired branch
git switch main

# Pull down any upstream changes
git pull

# Create a new branch to work on
git switch --create patch/1234-name-issue
```

Commit your changes, then push the branch to your fork with `git push -u fork` and open a pull request on [the .github repository](https://github.com/cyberskill-world/.github/) following the template provided.

## Action Development Guide

When adding or modifying shared actions, follow these quality standards:

### Required Elements

- **SHA pinning**: All external `uses:` must be pinned to full 40-character commit SHAs (e.g., `@de0fac2e...`), not floating tags
- **Shell specification**: Every `run:` step must include `shell: bash`
- **Input validation**: Validate all user-provided inputs. Use `scripts/validate-branch.sh` for branch names
- **Error handling**: Start scripts with `set -euo pipefail`

### Naming Convention

- **Action name**: Use emoji prefix + descriptive name (e.g., `🛠️ Build`, `🚀 Deploy`)
- **Input names**: UPPER_SNAKE_CASE (e.g., `BUILD_ARTIFACT_NAME`)
- **File structure**: `actions/<name>/action.yml`

### Testing Locally

You can validate actions locally before pushing:

```sh
# Lint all YAML files
yamllint -c .yamllint .

# Validate action schemas (requires Go)
go install github.com/rhysd/actionlint/cmd/actionlint@latest
actionlint -color

# Lint shell scripts
shellcheck scripts/*.sh
```

### Documentation

- Update `docs/README.md` action table if you add, remove, or rename inputs/outputs
- Add inline comments for non-obvious logic
- Use `# ⚠️ SYNC:` comments to mark code that must stay in sync across files