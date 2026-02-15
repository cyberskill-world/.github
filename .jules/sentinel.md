## 2025-02-18 - JSON Injection in Shell Commands
**Vulnerability:** A JSON injection vulnerability was found in `actions/trigger-events/action.yml` where user input was directly interpolated into a JSON string passed to `curl`. This allowed an attacker to inject arbitrary JSON fields by using double quotes.
**Learning:** Shell scripts that construct JSON strings manually using string interpolation are inherently risky and prone to injection attacks, similar to SQL injection.
**Prevention:** Always use dedicated tools like `jq` or `python` (or `gh api`) to construct JSON payloads. Specifically, `jq -n --arg key "$value" '{key: $key}'` ensures proper escaping of values.
