# Project Knowledge Playbook

This playbook defines how to create, read, validate, and maintain the repository-local knowledge base used by Project Web Mentor v2.0.1.

## 1. Default location and scope

Default location: `docs/ai/project-knowledge/` at the repository root. This path is neutral across Claude Code and Antigravity, so both agents can reuse the same project knowledge.

If the repository already has a maintained architecture/documentation area, use that location instead when it is clearly the project convention. Record the chosen location in the index. Do not create duplicate documentation trees.

**One-time migration from v2.0:** if the default location is absent, check the former `.claude/project-knowledge/` location. When it contains project knowledge, copy/migrate useful notes into the new default location, preserve manual content, verify the result, and leave the legacy source untouched as a fallback. If both locations exist, treat `docs/ai/project-knowledge/` as canonical and reconcile conflicts carefully; never silently overwrite either version.

This knowledge base is repository-specific. Never place it inside a globally installed Skill directory. Do not modify application code or project configuration as part of knowledge maintenance.

## 2. Memory initialization

Before investigating:

1. Resolve the repository root.
2. Check for `INDEX.md` in the configured knowledge directory.
3. If present, read only the index first and select the notes relevant to the current request.
4. If absent, initialize a minimal index and create notes as verified information becomes available.

The amount of discovery depends on the request:

- Broad onboarding / architecture mapping: perform the project-discovery workflow and establish the baseline map.
- Specific task or code question: inspect only the relevant path and write a small, scoped memory entry. Add missing areas to the index as `NOT MAPPED` rather than scanning the entire repository.
- Generic web lesson: do not initialize project memory unless the project itself is relevant.

## 3. Progressive recall

Every invocation should follow this sequence:

```text
Read INDEX.md
    ↓
Select relevant note(s)
    ↓
Inspect relevant source files and tests
    ↓
Compare notes with current code
    ↓
Answer the user's question
    ↓
Update only reusable findings
```

Keep `INDEX.md` concise (target: roughly 50-100 lines). It is a routing table, not a duplicate architecture document. Do not load every detailed note unless the request genuinely spans the whole system.

Use file search, symbol/reference search, and targeted reads. Avoid dumping the repository tree or reading unrelated modules.

## 4. Freshness and drift detection

For the notes relevant to a task:

- Confirm the referenced files still exist.
- Confirm key symbols, route registrations, and dependencies still exist.
- Inspect implementation and tests that directly affect the task.
- When available and useful, inspect `git status --short` or a targeted `git diff -- <relevant-paths>` to identify uncommitted changes. These are read-only checks.
- Optionally record the current short commit SHA using `git rev-parse --short HEAD`.

Do not mark an entire knowledge base stale merely because the repository has a new commit. Revalidate the relevant paths and behavior. If the current code differs from a note, trust the code and update only the affected section.

Use these note states:

- `CURRENT`: claims were checked against the relevant source in this investigation.
- `PARTIAL`: some claims were checked, but coverage is incomplete.
- `NEEDS_REVIEW`: one or more claims conflict with code or could not be confirmed.
- `NOT MAPPED`: the area has not yet been investigated.

A `Last verified` date is not proof of correctness by itself. Never describe a note as current unless source validation happened.

## 5. Evidence and claim quality

Every substantive architectural claim should have evidence wherever possible:

- repository-relative path;
- symbol, class, function, route, component, or configuration key;
- line range when the tool exposes a stable range and it helps navigation;
- test or documentation reference when relevant.

Classify claims:

- `CONFIRMED`: directly supported by source code, configuration, tests, or maintained documentation.
- `INFERRED`: interpretation supported by evidence but not explicitly guaranteed by the repository.
- `UNKNOWN`: not established yet.

Do not turn an inference into a fact just because it appears in an older note. Do not infer intent from architecture alone; write "the code currently does X" rather than "the original author intended X" unless a decision record supports it.

## 6. Automatic capture rules

After a meaningful investigation or implementation, automatically update the knowledge base when at least one of these conditions is true:

- a previously unmapped architectural boundary was verified;
- a request flow was traced across multiple layers;
- a task clarified an API, domain, persistence, identity, integration, or asynchronous contract;
- a repeated convention was confirmed by multiple examples or project documentation;
- a user correction invalidated an existing note;
- a technical decision or constraint was explicitly confirmed;
- a meaningful open question was identified with a concrete next step.

Do not write for every trivial question. Do not save generic explanations, temporary debugging chatter, speculative assumptions as facts, large source excerpts, secrets, tokens, customer information, or personal data.

Write the smallest possible change:

1. Update or add the relevant detailed note.
2. Update `INDEX.md` links, coverage status, and recent update summary.
3. Update `open-questions.md` only when a durable unresolved question exists.
4. Preserve manual content and avoid unrelated rewrites.

If a file write is denied by the environment, explain that the discovery was completed but the memory was not persisted. Do not claim success.

## 7. Knowledge base structure

Create files only when useful:

```text
docs/ai/project-knowledge/
├── INDEX.md
├── architecture-overview.md
├── module-map.md
├── data-and-domain.md
├── integrations-and-async.md
├── technical-decisions.md
├── open-questions.md
└── request-flows/
    ├── authentication.md
    └── <flow-name>.md
```

### INDEX.md

Contains:
- repository/project label and detected stack (only verified facts);
- purpose and chosen knowledge location;
- links to detailed notes;
- mapped / partially mapped / not mapped areas;
- last meaningful update and last verified commit when available;
- a short recent-update list (keep only the most useful few entries).

### architecture-overview.md

Contains:
- system purpose when established;
- runtime components and major boundaries;
- startup and routing entry points;
- request lifecycle overview;
- Mermaid diagram based only on verified components/relationships;
- tests and observability overview;
- confirmed facts, inferences, and unknowns.

### module-map.md

Contains a concise table of important areas, responsibility, primary files/symbols, dependencies, and confidence. Avoid cataloguing every folder.

### data-and-domain.md

Contains verified domain concepts, key entities, API schemas/DTOs, ownership, persistence, migrations, and transaction boundaries. Do not reproduce database dumps or customer records.

### integrations-and-async.md

Contains external systems, API clients, queues, workers, events, scheduled jobs, timeout/retry behavior, idempotency, and partial-failure boundaries.

### request-flows/<name>.md

One note per meaningful flow. Prefer behavior-based names such as `sign-in.md`, `create-order.md`, or `export-report.md`.

### technical-decisions.md

Only capture decisions supported by explicit documentation, code constraints, or user/team confirmation. Include context, decision, rationale/evidence, trade-offs, and status. Mark inferred rationale clearly.

### open-questions.md

Keep only unresolved questions that matter for future work. For each, include why it matters, what is already known, and the next evidence/action needed. Remove an item when resolved.

## 8. Git and sharing guidance

The default `docs/ai/project-knowledge/` directory may be ignored or excluded by a repository's `.gitignore` or other source-control rules. Do not change those rules automatically. In the final response after initialization, tell the developer if the memory directory appears ignored or untracked only when that status was actually checked. The legacy `.claude/project-knowledge/` path is supported only for the one-time v2.0 migration described above; do not continue maintaining two parallel knowledge bases.

If knowledge should be shared with the team, the developer can move the knowledge base to the repository's maintained documentation location or explicitly add it to version control. Do not commit, push, or change Git state on the developer's behalf.

## 9. Response transparency

After a relevant investigation, add one concise note to the answer:

- what knowledge file was created/updated;
- what was captured;
- or why no durable memory update was needed.

Never say "saved" unless the file write succeeded and the result was verified.
