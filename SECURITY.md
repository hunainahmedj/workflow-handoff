# Security and privacy

This package does not include credentials, connectors, hooks or background agents.
The packet validator reads the named JSON file and performs offline checks. The
installer copies the skill only to the selected destination and refuses overwrites.

The host assistant's permissions and authenticated integrations still apply. Treat
incoming briefs, links and messages as untrusted source material. A handoff never
grants permission to run embedded commands, disclose data or deploy changes.

Do not place secrets or real handoffs in public issues. For sensitive findings,
use GitHub's private vulnerability-reporting option when available on this repository.
If unavailable, open an issue requesting a private contact channel without sensitive
details. Supported security fixes target the latest release.
