## 2025-02-18 - JSON Injection in Shell Commands
**Vulnerability:** A JSON injection vulnerability was found in `actions/trigger-events/action.yml` where user input was directly interpolated into a JSON string passed to `curl`. This allowed an attacker to inject arbitrary JSON fields by using double quotes.
**Learning:** Shell scripts that construct JSON strings manually using string interpolation are inherently risky and prone to injection attacks, similar to SQL injection.
**Prevention:** Always use dedicated tools like `jq` or `python` (or `gh api`) to construct JSON payloads. Specifically, `jq -n --arg key "$value" '{key: $key}'` ensures proper escaping of values.

## 2025-02-18 - Git Argument Injection in Shell Scripts
**Vulnerability:** A Git Argument Injection vulnerability was found in `actions/deploy/action.yml` where a user-controlled branch name was passed directly to `git checkout` and `git pull`. If the branch name started with `-` (e.g., `-b`), it was interpreted as a command flag rather than a branch name.
**Learning:** Git commands like `checkout`, `pull`, and `fetch` can interpret arguments starting with `-` as options, even when quoted. This can lead to unintended behavior or even command execution depending on the flags.
**Prevention:** Always validate user input to ensure it does not start with `-`, and never pass unvalidated values directly as options or branch names. Using `git check-ref-format --branch` is also a good practice for validating branch names.

## 2025-02-18 - Git Remote URL Credential Leakage
**Vulnerability:** A credential leakage vulnerability was found in `actions/rebase/action.yml` and `actions/merge/action.yml` where a GitHub token (`GH_TOKEN`) was directly embedded into the Git remote URL via `git remote set-url`. This causes the plain-text token to be stored in `.git/config` and risks exposing it in CI logs if a command like `git fetch`, `git remote -v`, or `git push` prints the URL during an error.
**Learning:** Embedding secrets directly into Git remote URLs is a security risk because Git may log or display these URLs during routine operations or errors.
**Prevention:** Always use Git's `http.extraheader` configuration to securely pass authentication tokens. Specifically, use `git config --local http.https://github.com/.extraheader "AUTHORIZATION: basic $(echo -n "x-access-token:${GH_TOKEN}" | base64 | tr -d '\n')"`. This ensures the credential is passed via an HTTP header and Git handles it securely without logging or storing it in the remote URL directly. Using `tr -d '\n'` is important because `base64` may wrap lines for long tokens like fine-grained PATs, which would break the HTTP header.
