## 2025-02-18 - JSON Injection in Shell Commands
**Vulnerability:** A JSON injection vulnerability was found in `actions/trigger-events/action.yml` where user input was directly interpolated into a JSON string passed to `curl`. This allowed an attacker to inject arbitrary JSON fields by using double quotes.
**Learning:** Shell scripts that construct JSON strings manually using string interpolation are inherently risky and prone to injection attacks, similar to SQL injection.
**Prevention:** Always use dedicated tools like `jq` or `python` (or `gh api`) to construct JSON payloads. Specifically, `jq -n --arg key "$value" '{key: $key}'` ensures proper escaping of values.

## 2025-02-18 - Git Argument Injection in Shell Scripts
**Vulnerability:** A Git Argument Injection vulnerability was found in `actions/deploy/action.yml` where a user-controlled branch name was passed directly to `git checkout` and `git pull`. If the branch name started with `-` (e.g., `-b`), it was interpreted as a command flag rather than a branch name.
**Learning:** Git commands like `checkout`, `pull`, and `fetch` can interpret arguments starting with `-` as options, even when quoted. This can lead to unintended behavior or even command execution depending on the flags.
**Prevention:** Always validate user input to ensure it does not start with `-`. Additionally, use `--` to separate options from positional arguments (e.g., `git checkout -- "$BRANCH"`), though validation is the primary defense. Using `git check-ref-format --branch` is also a good practice for validating branch names.
