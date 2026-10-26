# Preserve the whole workflow, not just its current screen

## Four distinct scopes

Name the product capability and intended users/contexts/environments first. Then identify
the workstream, the concrete demonstration, and the recipient's immediate task.
A narrow example is not a product boundary. Preserve explicit exclusions too.

Preserve the mode of work as well: exploring, testing, reviewing, designing or
implementing. For an exploratory walkthrough, the goal is to understand and verify
the existing workflow against needs and evidence. A valid finding is that the
functionality already exists and works. Do not presume a gap, redesign, or a need
to build from scratch. Confirm a suspected gap in the relevant environment before
proposing a change; a prototype omission is not proof of a production omission.

Record the journey actually taken up to handover, including detours, what prompted
them and what was learned. Do not require or invent an end-to-end future journey.
Future steps are optional hypotheses or explicitly agreed plans, labelled as such;
they may change with findings. State the current question or next investigation,
not a fixed remaining sequence. Preserve a fixed plan when the user actually chose one.

Keep a layered dossier in the shared docs home:
- `brief.md`: purpose/mode, scope, journey so far, present checkpoint, current question.
- `decisions.md`: stable decision IDs, choice/status, deciding human, reason,
  alternatives rejected or deferred, implications, source and supersession links.
- `journey.md`: significant steps already taken, what was learned and why the next
  step followed; include stopped/rejected approaches that affect future choices.
- `return.md`: delta from the accepted checkpoint and reconciliation information.
For small tasks these may be sections in one file; do not multiply empty files.
Link canonical domain evidence and specs instead of copying their full contents.

## Evidence and history

Separate human direction, domain evidence, assistant recommendation, demonstration
values, implemented/verified behavior and unanswered questions. A demonstration
approval is not a stakeholder's approval. Record a source date/revision and uncertainty.
Do not invent rationale, rejected alternatives, exact dates or missing chat history.
Say "reason not recorded" and identify the specific missing context. Label recovered
history as reconstructed, with its sources. Preserve material steps, not every tool call.

Keep the original scope and decisions when updating a checkpoint. A new packet's
start document must lead to the complete dossier, not just its latest supplement.
Mark outdated checkpoint claims superseded without deleting historical packets.

## Chat excerpts

The brief is the entry point, not a substitute for important reasoning. Curate
relevant user decisions with nearby reasoning and source references when useful;
remove unrelated/private content. Do not export entire chats by default. If the
human authorizes a transcript, keep it a versioned supplementary source with
explicit recipient access, not the instructions or source of current authority.

## Comprehension check

Before calling an important handoff context-complete, have the receiver explain:
1. Full outcome, product scope, example and current assignment separately.
2. Journey taken so far, reasons for detours and where the work paused.
3. Accepted decisions, reasons and what remains uncertain, citing the dossier.
4. What is implemented in which environment and what is only a proposal.
5. Current question or agreed next action, what is tentative, and existing constraints.
6. Starting artifact versions and how return changes will be reconciled.

A fresh-agent test receives only the shared dossier and skill, not the coordinator's
chat or expected answers. Record inputs, actual harness/model, output, gaps and
result. A failed login or unavailable provider is **not run**, not a pass. Do not
silently replace the requested harness. Artifact validation and comprehension are
separate checks; neither establishes product correctness or stakeholder approval.
