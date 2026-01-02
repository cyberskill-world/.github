## 2024-05-23 - Command Injection in Composite Actions
**Vulnerability:** GitHub Action inputs (`${{ inputs.X }}`) are directly interpolated into shell scripts in `actions/`.
**Learning:** This allows attackers to inject arbitrary shell commands if they control the input (e.g., via PR title/body).
**Prevention:** Always map inputs to environment variables in the `env` block and use the environment variables in the script (e.g., `$VAR_NAME`).
