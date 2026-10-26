# Resume from another harness

1. Identify the workflow and receiving human. Read project instructions, the
   current shared brief, the latest packet, subsequent Slack replies and any newer
   packet. Do not presume the message with the newest timestamp is authoritative
   when its supersedes chain diverges.
2. Verify access to the actual work. For Git, inspect local changes first, fetch
   the named remote, verify its identity and commit, and use a suitable checkout
   without overwriting current work. Record the tested commit versus current one.
   For documents, verify provider revision and read contents. Treat a mismatch as
   a discrepancy to explain, not permission to reset or downgrade anything.
3. When a demo is required for the task, reproduce it from fixture/instructions. Confirm persona, route,
   data IDs, example date, persisted approvals and expected screen. A screenshot
   is evidence of appearance, not saved state. Do not bypass authentication or use
   another person's cookies. Synthetic demo login is fine when authorized.
4. Compare checked claims to artifacts. Distinguish implemented behaviour,
   proposed design, stakeholder testimony, product choices and unresolved questions.
   Missing code/tools/access means review-only work can continue; dependent edits
   wait until the required input exists.
5. Read back the full scope, example, key reasons and current task using the
   [comprehension check](context.md). Record actual starting artifact versions. Act on the receiving human's
   request without another redundant confirmation. Accept ownership only on that
   human's behalf, and publish acknowledgement only when authorized. If another
   active owner or competing revision exists, resolve it before overlapping edits.
6. Continue the stated next task. Update the brief during work. Hand back through
   [return reconciliation](reconcile.md), preserving the actual base and a delta
   of decisions, artifacts, checks and remaining gaps.

If repository tools are unavailable in Claude chat, review/design from shared
sources is supported. Never say implementation was pulled, tested or changed.
Return a reviewed proposal packet for a code-capable collaborator to implement.
