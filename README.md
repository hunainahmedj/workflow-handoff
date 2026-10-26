# Workflow Handoff

Keep the context when work moves between people and AI assistants.

**workflow-handoff** is a portable Agent Skill, also packaged as a Claude Code
plugin. It prepares a versioned brief, preserves decisions and the journey so far,
and helps reconcile returned work. Use it for walkthroughs, testing, research,
reviews, design or implementation. Finding that something already works is a valid
outcome; a handoff does not turn exploration into a redesign project.

## Install

Python 3.10+ is needed for the optional installer and offline validator. The skill
itself is Markdown. It has no runtime packages, bundled connectors or background
services. Choose one installation method per host to avoid duplicate skills.

### Codex: portable skill

```sh
git clone https://github.com/hunainahmedj/workflow-handoff.git
cd workflow-handoff
python3 scripts/install_skill.py --target codex
```

This copies the skill to `~/.agents/skills/workflow-handoff`. Open a new Codex chat
if it is not discovered immediately. Invoke it with:

> Use $workflow-handoff to prepare this workflow for Alex. Let me review it before sending.

### Claude Code: plugin

In Claude Code:

```text
/plugin marketplace add hunainahmedj/workflow-handoff
/plugin install workflow-handoff@workflow-handoff-marketplace
```

Start a new session if needed. Invoke `/workflow-handoff:workflow-handoff`, followed
by your request. To try the cloned plugin without installing it:

```sh
claude --plugin-dir /absolute/path/to/workflow-handoff
```

### Claude Code: skill only

From the cloned repository:

```sh
python3 scripts/install_skill.py --target claude
```

This installs to `~/.claude/skills/workflow-handoff`; invoke `/workflow-handoff`.
Do not also install the plugin in the same host. Other Agent Skills-compatible
hosts can use `skills/workflow-handoff/` according to their own installation rules.
Claude chat/Cowork can review accessible briefs; Git or Slack operations require
their own supported tools. This package does not add those capabilities.

### Update or remove

For marketplace installs, use the host's plugin update/uninstall controls.
For copied skills, compare your installed copy with the new version first. Move
any local customisations to a backup, then run the installer after removing the
old `workflow-handoff` directory. The installer refuses to overwrite an existing
file, directory or symlink. Remove only that installed skill directory to uninstall.

## Use normal language

You do not have to memorize mode names:

- **Prepare:** “Prepare this workflow for Alex; I want to review the brief first.”
- **Send:** “Send the reviewed handoff to Alex in #project-collaboration.”
- **Resume:** “Read this handoff, explain where we stopped, and continue my review.”
- **Return:** “Prepare my changes for Morgan, with the starting version and reasons.”

Preparation writes a draft. Sending needs explicit authorization. The recipient's
own instruction authorizes their assistant to take over. A notice is not a lock,
permission to deploy, or proof that later supplements were incorporated.

## What gets preserved

- Purpose and scope, with the example separated from the broader task.
- Steps actually taken, detours, decisions, reasons and unanswered questions.
- What works, what is only proposed and which environment was checked.
- Exact code/document revisions and a reproducible demo fixture when needed.
- Current human owner and the immediate question at hand.
- A return record comparing the actual base, returned work and current work.

Keep project dossiers in your own private or shared workspace, **outside this
package**. The included [brief](skills/workflow-handoff/assets/brief.md),
[packet](skills/workflow-handoff/assets/handoff.json) and
[return](skills/workflow-handoff/assets/return.md) are reusable templates.
No full chat export is required. A small generic example is in [examples/](examples/).

## Connect tools separately

Each collaborator authenticates their own Git, document and optional Slack tools.
Choose a shared document location and one Slack thread per workflow, when using
Slack. The skill discovers available capabilities; it contains no account IDs,
channels, credentials or project defaults. It works in prepare/review mode without
Slack. If sending is unavailable, it prepares text for manual delivery and says
**not sent**. It never broadens access to make a link reachable.

## Validate

```sh
python3 skills/workflow-handoff/scripts/validate_handoff.py examples/review-draft.json
python3 -m unittest discover -s tests -v
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

Use `--ready` with a real packet only after verifying its shared artifacts. The
validator checks structure and declared readiness offline; it cannot prove remote
access, ownership, factual accuracy or the recipient's understanding. The example
is intentionally an unshared draft, so it must fail `--ready`.

## Compatibility and limits

The shared skill follows the [Agent Skills format](https://agentskills.io/specification).
Codex uses its [documented skill locations](https://learn.chatgpt.com/docs/build-skills).
Claude packaging follows the [plugin manifest](https://code.claude.com/docs/en/plugins-reference)
and [marketplace](https://code.claude.com/docs/en/plugin-marketplaces) conventions.
These are separate installation surfaces sharing one skill source, not a claim
that one plugin manifest works in every host. Automated tests cover packet rules
and installation; [testing notes](TESTING.md) distinguish them from live behavior.

MIT licensed. See [LICENSE](LICENSE), [contributing](CONTRIBUTING.md) and
[security](SECURITY.md).
