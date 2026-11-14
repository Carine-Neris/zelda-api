# Project Knowledge Notes Template

Use this template when creating or refreshing project knowledge. Keep notes short, navigable, and linked to source evidence. The current code remains the source of truth.

## Metadata block

Add this block near the top of each detailed note:

```markdown
> Status: PARTIAL
> Last verified: YYYY-MM-DD or not recorded
> Verified at commit: <short-sha> or not recorded
> Scope: <what this note covers and what it does not cover>
```

Allowed statuses: `CURRENT`, `PARTIAL`, `NEEDS_REVIEW`, `NOT MAPPED`.

## INDEX.md template

```markdown
# Project Knowledge Index

> Knowledge format: 2.0
> Project: <repository label>
> Knowledge location: `docs/ai/project-knowledge/`
> Last meaningful update: <date or not recorded>
> Last verified commit: <short-sha or not recorded>

## Verified project snapshot
- Languages/frameworks: <verified only>
- Application shape: <verified only>
- Main runtime components: <verified only>

## Knowledge map
| Area | Note | Coverage | Last verified |
|---|---|---|---|
| Architecture | [architecture-overview.md](architecture-overview.md) | PARTIAL | YYYY-MM-DD |
| Modules | [module-map.md](module-map.md) | NOT MAPPED | — |
| Data/domain | [data-and-domain.md](data-and-domain.md) | NOT MAPPED | — |
| Integrations/async | [integrations-and-async.md](integrations-and-async.md) | NOT MAPPED | — |

## Request flows
- [Flow name](request-flows/flow-name.md) — coverage and status

## Not mapped / needs revalidation
- <area and why it matters>

## Recent updates
- YYYY-MM-DD: <small, durable change to the knowledge base>

## Usage rule
Read this index first, then load only the notes relevant to the current task. Validate claims against current source code before relying on them.
```

## Architecture note template

```markdown
# Architecture Overview

> Status: PARTIAL
> Last verified: YYYY-MM-DD
> Verified at commit: <short-sha or not recorded>
> Scope: <scope>

## Executive overview
<What the system does and the strongest evidence.>

## Runtime components and boundaries
| Component | Responsibility | Evidence | Confidence |
|---|---|---|---|

## Entry points
| Trigger | Entry point | Next boundary | Evidence | Confidence |
|---|---|---|---|---|

## System map
<Mermaid diagram or concise text map; label inferred edges.>

## Request lifecycle
<One representative trace or a link to a dedicated flow note.>

## Tests and observability
<Verified test locations, logging, metrics, and tracing.>

## Confirmed / inferred / unknown
- CONFIRMED:
- INFERRED:
- UNKNOWN:
```

## Request-flow note template

```markdown
# <Flow name>

> Status: PARTIAL
> Last verified: YYYY-MM-DD
> Verified at commit: <short-sha or not recorded>
> Scope: <trigger and outcome covered>

## User/business outcome
<What the flow accomplishes.>

## Execution path
1. Trigger:
2. Client/browser:
3. HTTP/API contract:
4. Server entry point / middleware:
5. Validation and authorization:
6. Application/domain behavior:
7. Persistence or external side effect:
8. Async handoff, if any:
9. Response and UI state:

## Contracts and failure behavior
<Relevant payloads, invariants, errors, retries, idempotency, etc.>

## Tests and verification
<Tests and how behavior can be verified.>

## Evidence
- `path/to/file.ext` — `SymbolName` — what it confirms

## Confidence
- CONFIRMED:
- INFERRED:
- UNKNOWN:
```

## Maintenance rules

- Keep each note focused on one topic or flow.
- Link to source files/symbols instead of copying code.
- Use evidence paths relative to repository root.
- Keep confirmed facts, inferences, and unknowns separate.
- Re-check references when the relevant code changes.
- Prefer targeted updates to rewriting whole documents.
- Preserve manual notes and user-authored sections.
- Never include credentials, customer data, personal data, production secrets, or raw environment values.
