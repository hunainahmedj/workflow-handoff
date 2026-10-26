# Return work and reconcile it

Use [the return template](../assets/return.md). The protocol works with Git or
versioned documents; Slack carries notices and links, not the sole work history.

## Record the actual starting point

A recipient records the accepted packet ID plus exact starting versions for every
affected repository, document and demo fixture. The latest notification is not
necessarily their base: a later companion snapshot may never have been integrated.
`supersedes` orders packets; it does not establish Git ancestry or accepted ownership.

## Return a delta

Create a new packet and return record with:
- accepted base packet and artifact versions; returned revisions/branches;
- changed behavior and files, decision IDs added/changed, reasons and sources;
- implemented vs proposed changes, rejected ideas and unresolved questions;
- fixture/schema changes and replay instructions, checks with exact tested versions;
- next human owner requested and any known overlap with work underway.
Do not replace old packets or rewrite a prior accepted decision as if unchanged.
A return is an offer for review, not automatic acceptance or merging.

## Three-way comparison

For each artifact identify **B** (actual accepted base), **R** (returned work),
**C** (receiver's current work). Fetch/read without resetting local edits. Check
remote identities and ancestry; use an isolated integration checkout when needed.
If ancestry/base cannot be established, review manually rather than guessing.

Compare B→R and B→C, then reconcile these independently:
1. Code/files: preserve unrelated changes; resolve actual overlapping changes.
2. Decisions: compare scope, policy, permissions and rationale by stable IDs.
   A clean Git merge does not resolve conflicting human decisions. Routine compatible
   implementation choices can be resolved within existing authorization; a material
   policy conflict needs the relevant human decision, with both choices shown.
3. Demo state: compare named domain fixtures and their schema/version. Do not replace
   a live browser's storage or overwrite changed approvals/results. Use a separate
   demo instance or an explicit compatible migration, preserving the older fixture.
4. Evidence/checks: revalidate affected journeys against the combined result.
   Neither side's passing checks automatically cover the integrated version.

Record accepted/deferred/rejected items, unresolved conflicts, integrated revisions,
checks and ownership in a reconciliation receipt. Publish/send within the human's
existing authority; a return is not blanket permission to merge protected branches,
deploy, or send messages. Keep overlapping work paused only where a genuine conflict
requires human resolution; independent review can continue.

## Example

Alex started from A and returned R. Morgan added a replay checkpoint C based on A.
Compare A→R with A→C. Preserve the checkpoint while applying compatible search
improvements. If R changes which users may view private documents, review that
policy change even when Git finds no conflict. Do not make C Alex's starting point
just because its Slack notice was more recent.
