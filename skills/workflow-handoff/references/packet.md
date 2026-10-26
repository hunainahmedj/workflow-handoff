# Packet contract — version 1

A packet is a compact checkpoint, not a transcript. Use the JSON template and a
human-readable brief. All timestamps are ISO 8601 with timezone. Packet ID is a
new UUID. `supersedes` is the previous packet ID, or null for the first packet.
Do not replace old packets; corrections create a new packet and explain the change.
Use an actual clock/tool result for the packet creation timestamp. A source note's
date does not establish the current hour or minute. If no clock is available, leave
the timestamp unresolved and report the draft as structurally incomplete rather
than inventing a valid-looking time. Source-event dates remain separate.

Required meaning:
- `workflow_id`, `title`, `objective`: stable slug and concrete outcome.
- `author`, `recipient`, `current_owner`: human names, not model names. Record
  harness separately. Do not assume the recipient has accepted.
- `state`: draft, offered, accepted, blocked or completed. `ready_for_resume`
  concerns artifact readiness only; it does not assert acceptance or correctness.
  `state` concerns this packet, while `current_owner` concerns the workflow. An offered
  supplement can name the already accepted review owner; it does not revoke their
  earlier acceptance. Record that acceptance source in the dossier.
- `scope`: review/design/prototype/backend/frontend/mixed. Identify production
  delivery accurately in the brief.
- `brief`: shared URL and version (Git commit or provider revision); until shared,
  null URL and an explicit blocker. A local path belongs only in local notes.
- `repositories`: one record per affected repo. Remote without credentials,
  branch, exact 40/64-character commit, dirty flag, `published_verified`.
  Verify the remote contains the commit. A clean unrelated HEAD does not capture
  uncommitted feature work. In v1 dirty work cannot be advertised as ready;
  scope/commit the authorized changes or send a review-only blocked packet.
- `artifacts`: named URLs with `accessible_verified` set only after successful
  readback using available access. Sender access does not prove recipient access;
  recipient verifies again. No localhost/file URLs as shared artifacts.
- `demo`: mode none/fixture/instructions/browser-only, reference and reproduction
  steps. For fixtures/instructions reference a versioned reachable artifact.
- `decisions`, `open_questions`, `changes`, `checks`, `next_steps`, `blockers`:
  concise arrays. Decisions name who decided and evidence links in the brief;
  checks state command/journey, environment, result and commit tested, including
  failures/untested areas. One next step should be immediately executable.
- `slack`: verified channel ID, workflow parent timestamp and delivery receipt.
  Null thread is valid before first publication. Never invent a permalink.

A ready packet needs reachable/versioned brief, a verified published commit for
all repo work, no dirty affected repos, no blockers, and reproducible demo state.
Keep artifact readiness, delivery and human acceptance separate: missing recipient
acceptance is not an artifact blocker. A packet can be ready while still offered.
A missing Slack destination blocks a requested send, not preparation or artifact
readiness when the work is otherwise shared. Missing Git access is not itself a
blocker for a review-only task that has all required versioned review material.
List only missing inputs that actually prevent the stated next task in `blockers`;
record unrelated access/verification limits in the brief or checks.
A design-only packet can be ready without repositories if its shared document is
verified. Empty test arrays are allowed only with an explicit explanation in the
brief of why no checks were run. Ready means resumable, not test-passing.

Keep secrets and private personal records out. Copy domain evidence only under a
separately authorized data-handling task; normal handoffs link to it.
