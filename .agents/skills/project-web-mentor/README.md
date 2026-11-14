# Project Web Mentor v2.0.1

A cross-agent Agent Skill for understanding an unfamiliar software project, investigating tasks before implementation, learning web engineering through the actual codebase, and maintaining a reusable, evidence-based project knowledge base.

## What's included

- **Memory initialization:** checks for project knowledge at the beginning of relevant invocations and bootstraps it when needed.
- **Incremental recall:** reads a short index first and opens only notes related to the current task.
- **Automatic knowledge capture:** updates useful architectural discoveries and verified flows after meaningful investigations.
- **Drift validation:** checks notes against current source code before relying on them and marks conflicting notes for review.
- **Evidence metadata:** records source paths/symbols, confidence, verification date, and commit identifier when available.
- **Cross-agent storage:** keeps the project knowledge in a neutral repository path that Claude Code and Antigravity can share.

## Package contents

- `SKILL.md`: core instructions and operating contract.
- `references/project-knowledge-playbook.md`: memory initialization, migration, incremental recall, freshness validation, and automatic capture rules.
- `references/knowledge-notes-template.md`: index, architecture, and request-flow templates.
- `references/project-discovery-playbook.md`: baseline architecture discovery and refresh.
- `references/task-analysis-playbook.md`: task investigation before coding.
- `references/web-engineering-learning-map.md`: targeted web-engineering topics.
- `references/rpa-to-web-transition.md`: bridge from RPA mental models to web application engineering.
- `references/developer-context.md`: starting learning profile and teaching preferences.
- `EVALUATION.md`: acceptance tests for the Skill's behavior.
- `CHANGELOG.md`: version history.

## Install in Claude Code

For one repository, place the `project-web-mentor/` directory here:

```text
<repository>/
└── .claude/
    └── skills/
        └── project-web-mentor/
            ├── SKILL.md
            └── references/
```

For personal use across repositories, Claude Code also supports:

```text
~/.claude/skills/project-web-mentor/
```

## Install in Google Antigravity

For one workspace, place the same `project-web-mentor/` directory here:

```text
<workspace-root>/
└── .agents/
    └── skills/
        └── project-web-mentor/
            ├── SKILL.md
            └── references/
```

For global use, Antigravity App and IDE support:

```text
~/.gemini/config/skills/project-web-mentor/
```

Antigravity CLI uses its own global skills directory:

```text
~/.gemini/antigravity-cli/skills/project-web-mentor/
```

Refer to the official [Antigravity Agent Skills documentation](https://antigravity.google/docs/skills) for the current locations and surface-specific details. Claude Code's project and personal locations are documented in the [Claude Code Skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills).

## Shared project-memory location

Regardless of whether the Skill is invoked by Claude Code or Antigravity, its default project knowledge directory is:

```text
<repository>/docs/ai/project-knowledge/
```

This contains the `INDEX.md` plus only the detailed architecture, module, domain, integration, decision, question, and request-flow notes that have useful verified content. The knowledge stays in the repository, not inside either agent's Skill installation folder.

If the repository already has a maintained architecture/documentation location, the Skill should respect it and record the selected location in `INDEX.md` rather than creating a competing knowledge base.

### Migration from the previous v2.0 path

The previous package used `.claude/project-knowledge/`. On its first relevant invocation, v2.0.1 checks the new `docs/ai/project-knowledge/` location first. If that does not exist but legacy knowledge is present, the Skill migrates useful notes to the new location, verifies the copied files, and leaves the legacy source untouched. It does not silently overwrite conflicts or maintain two active knowledge bases.

## First run

From the repository root, invoke:

```text
/project-web-mentor Map this repository. Build the initial project knowledge base and trace one important request flow. Do not change application code.
```

The Skill performs an initial discovery and saves verified findings. For a narrow task in a repository without project knowledge, it performs only the necessary investigation and starts a partial knowledge base rather than scanning everything.

## Normal task use

```text
/project-web-mentor I received this ticket. Help me understand the current behavior, the relevant architecture, and the safest implementation options before I code: [ticket]
```

It reads `INDEX.md`, selects relevant notes, validates them against the current code, then investigates the task. It does not rebuild the entire architecture map on each call.

## Knowledge storage and Git

The default `docs/ai/project-knowledge/` path is repository-local and can be versioned with the project. Check whether it is ignored or excluded by the repository's Git rules. The Skill will not change `.gitignore`, commit, or push anything automatically. If the team should share the knowledge base, add the generated notes to version control according to the project's normal review process.

The current code is always the source of truth. Notes are a navigational aid and may be marked `NEEDS_REVIEW` when code changes invalidate them.

## Important distinction: Skill vs memory

- The **Skill** stores repeatable instructions and workflows.
- **Project Knowledge** stores repository-specific architecture and flow notes under `docs/ai/project-knowledge/` by default.
- **Claude Code Auto Memory** may store preferences and recurring feedback, but it is not a substitute for this explicit architectural knowledge base.
- Project instruction files such as `CLAUDE.md`, `AGENTS.md`, or `GEMINI.md` should remain concise. This Skill does not automatically add large architecture documents to them.

## Scope and limitations

This package uses the open Agent Skills folder format (`SKILL.md` plus sibling references) and is designed for Claude Code and Google Antigravity. It requires the agent to have permission to read repository files and write inside the project knowledge directory. Actual writes may still be subject to the host's permission settings. If file writing is unavailable or denied, the Skill must say that knowledge was not persisted.
