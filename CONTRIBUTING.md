# Contributing

Use synthetic examples only. Do not submit real conversations, private handoffs,
customer records, credentials, account identifiers or private service links.

Explain the user problem and observable behavior in an issue or pull request.
Preserve the distinction between exploratory work and an implementation request.
Keep host-specific setup outside the shared skill. Add tests when a validator or
installer behavior changes; do not enforce exact wording of generated briefs.

Run `python3 -m unittest discover -s tests -v` and the manifest validation commands
in the README. Document checks actually run and remaining gaps. Version changes
use semantic versioning; append release notes to CHANGELOG.md. Do not silently
change packet version 1 semantics or remove older packet history.
