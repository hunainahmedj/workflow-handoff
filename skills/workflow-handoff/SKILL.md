---
name: workflow-handoff
license: MIT
metadata:
  version: "0.5.0"
description: Prepare, publish to Slack, or resume a versioned human-to-human workflow handoff across Claude and Codex, preserving decisions, work versions, demo state and ownership.
---

# Workflow handoff

Help collaborators continue each other's work without sharing a chat or account.
Preserve the user's actual mode of work: a walkthrough or test is not automatically
a design or implementation task. Record the path taken and findings so far; let
verified gaps and the user's direction determine whether changes are needed.
The shared brief and versioned artifacts hold the work; one Slack thread per
workflow holds handoff announcements and acknowledgements. This skill is not a
background watcher, distributed lock, deployment permission or autonomous agent delegation.

## Route the request

- **Prepare / hand off:** read [packet contract](references/packet.md), use
  [handoff.json](assets/handoff.json) and [brief.md](assets/brief.md). Read
  [context preservation](references/context.md) before condensing an ongoing flow. Capture the
  actual current state, write the packet, validate it, and show a short summary.
- **Publish / send:** complete preparation, then use
  [Slack exchange](references/slack.md). Send only when the human has explicitly
  authorized this handoff's audience and purpose. Naming a channel in project
  configuration is routing information, not send authorization.
- **Resume / pick up:** read [resume procedure](references/resume.md). Verify the
  latest packet, access, version and ownership before editing. Explain what is
  implemented, proposed, blocked and next in plain language.
- **Return / reconcile:** read [return reconciliation](references/reconcile.md).
  Compare the accepted starting point, returned work and current work before integration.
- **Status / review:** read without taking ownership or modifying work.

Read repository instructions and any existing project handoff configuration.
Prefer an existing workflow ID/thread. Ask only for a missing destination,
ambiguous recipient/workflow, necessary policy decision or ownership conflict;
continue independent preparation meanwhile. Never guess Slack IDs or treat an
old channel name as proof of current membership/access.

## Durable handoff

For repository work, keep `handoffs/<workflow-id>/brief.md` and an append-only
`packets/<packet-id>.json` in the team's agreed documentation repository.
Publish artifacts before advertising the handoff as ready. Record each affected
repository separately with branch and exact commit. An uncommitted local diff
is not available to the other person. Do not bulk-add unrelated files, reset,
stash, switch branches, force-push or deploy to make a handoff look complete.
Use normal authorized Git operations; otherwise report the concrete gap.

For Claude chat/Cowork without repository access, use a shared versioned document
or uploaded packet plus reachable artifact links. Mark repository work unverified
and limit the next task to review/design until a code-capable collaborator can
verify it. A skill never adds Git or Slack tools by itself.

Use a named fixture/export or documented deterministic reconstruction for demo
state. A localhost URL, screenshot, browser session, approved setting in one tab,
or person's private chat is not a reproducible shared example. Do not export
cookies, credentials, session storage or private personal or customer data. Do not export
entire chats by default; preserve relevant decisions and rationale in a source-linked
record. A transcript export needs explicit scope and recipient authorization.
Link authoritative evidence in its existing access-controlled home.

Record human decisions separately from evidence, hypotheses and assistant
recommendations. Preserve source dates and uncertainty. Prototype outcomes are
not production implementation; preserve this distinction in every handoff.

## Ownership and revisions

The human currently working remains the owner while a handoff is offered.
The recipient's human instruction to take over authorizes their assistant to
resume; the sender cannot accept for them. An acknowledgement records acceptance,
not stakeholder approval, publication of results or a grant of permissions.

Before publishing or accepting, reread the latest Slack replies and shared
packet history. Use unique packet IDs and a `supersedes` pointer. If two people
have started or histories diverge, stop edits to the overlapping work, report
both versions, and resolve ownership with the humans. Slack acknowledgements
are advisory, not atomic locks. Parallel work needs separate scoped branches.

## Standalone operation

This is a standalone portable skill. It does not depend on an orchestration framework or a particular
model provider. The host supplies its own document, Git and Slack capabilities.
An explicitly requested fresh-agent test may use the host's available runner;
that does not integrate this skill into that runner or transfer human ownership.
Do not enable background delegation, install on another person's account, or
modify another plugin as a side effect of preparing or testing a handoff.

## Tools and validation

Discover available Slack/Git tools by their capabilities, not provider-specific
names. Prefer connected tools; use a configured CLI when appropriate. Each
collaborator authenticates their own account. If Slack posting is unavailable,
produce the exact message for manual posting and report **not sent**.

When Python 3.10+ is available:
`python3 <skill-dir>/scripts/validate_handoff.py <packet.json>`
Add `--ready` before advertising a packet as ready to resume. The validator checks
structure and declared readiness only; the assistant must actually verify remote
access, commit availability and stated checks. Without Python, manually apply
[packet contract](references/packet.md) and disclose that validation mode.

End with: work location, packet ID, readiness, next human owner, exact next step,
and whether Slack delivery was confirmed. Never claim another person's install,
access, acceptance, successful send or runtime execution without evidence.
