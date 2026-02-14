## 2024-05-23 - Command Injection in Composite Actions
**Vulnerability:** GitHub Action inputs (`${{ inputs.X }}`) are directly interpolated into shell scripts in `actions/`.
**Learning:** This allows attackers to inject arbitrary shell commands if they control the input (e.g., via PR title/body).
**Prevention:** Always map inputs to environment variables in the `env` block and use the environment variables in the script (e.g., `$VAR_NAME`).

## 2025-05-24 - Command Injection in SSH Actions
**Vulnerability:** `appleboy/ssh-action` inputs are interpolated into the `script` string, allowing remote command injection.
**Learning:** Even though `appleboy/ssh-action` executes remotely, interpolating inputs into the script string is vulnerable. Environment variables must be passed via `envs` input and defined in `env`.
**Prevention:** Map inputs to environment variables in `env`, list them in `with.envs`, and use `$VAR_NAME` in the script. Note that tilde expansion `~/path` will not work with quoted variables.
