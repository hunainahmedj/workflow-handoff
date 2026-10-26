# Testing

Automated tests exercise readiness, immutable packet links, unsafe URLs, draft
handling and installation without overwrites. These run without remote accounts.
`claude plugin validate` checks the plugin and marketplace format separately.

Behavioral evaluation should use a fresh session with only the skill and a synthetic
case. Ask it to prepare a handoff, have a separate receiver explain the scope and
journey without the original notes, then evaluate returned changes against their
actual base. A clean file merge must not hide a contradictory policy decision.
Record the exact inputs, host, output and limitations privately. Never publish real
project context as evaluation data. Structural validity alone does not establish
comprehension or correct judgment. No live Slack delivery is part of CI.
