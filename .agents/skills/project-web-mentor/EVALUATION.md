# Project Web Mentor v2.0.1 Evaluation

Run these acceptance tests in a representative repository. The goal is to verify that the Skill teaches and investigates while maintaining useful project knowledge without repeating expensive full scans.

## 1. Initial architecture discovery and memory bootstrap

Prompt:

> Map this repository. Build the initial project knowledge base and trace one important request flow. Do not change application code.

Expected behavior:
- checks for an existing knowledge index;
- if none exists, inspects manifests, docs, entry points, routes, representative modules, and tests;
- maps the real architecture rather than imposing a template;
- cites paths and symbols;
- separates confirmed facts, inferences, and unknowns;
- creates `docs/ai/project-knowledge/INDEX.md` and only the detailed notes supported by evidence;
- does not edit application code or inspect secrets;
- verifies the knowledge files were written and reports their paths.

## 2. Incremental recall on a second invocation

Prompt, in a new session:

> I have a task related to the flow you mapped. Help me understand where the behavior lives and what could be affected. Do not implement it yet.

Expected behavior:
- reads `INDEX.md` first;
- opens only the relevant flow/module notes;
- does not repeat a full repository inventory;
- validates relevant notes against current source code and tests;
- investigates only the necessary files;
- updates only notes that gained durable information.

## 3. Stale note / code drift detection

Preparation: rename or change a symbol referenced in one knowledge note, or provide a note that is deliberately out of date.

Prompt:

> Investigate this task using the existing project knowledge. Tell me whether the notes still match the code.

Expected behavior:
- detects missing paths/symbols or changed behavior;
- trusts current code over the note;
- marks the affected note `NEEDS_REVIEW` or corrects the specific section after verification;
- does not mark unrelated notes stale;
- reports what was revalidated and what remains unchecked.

## 4. Task investigation

Prompt:

> Here is a feature ticket: [paste ticket]. Help me understand what needs to happen and where the existing behavior lives. Do not implement it yet.

Expected behavior:
- translates the ticket into observable behavior;
- separates acceptance criteria from assumptions;
- consults relevant project notes;
- traces current behavior and relevant contracts;
- finds analogous tests or implementations;
- recommends a small plan and identifies unknowns;
- captures new, reusable findings automatically;
- does not generate a patch.

## 5. Web concept explanation

Prompt:

> Explain what happens between this frontend action and the API response. I want to understand the HTTP and browser concepts involved, not just what each function does.

Expected behavior:
- traces actual code path;
- explains browser/client/server boundaries;
- distinguishes HTTP behavior from framework behavior;
- uses relevant Django comparisons only if accurate;
- identifies likely failure modes and how to verify them;
- updates project knowledge only if a reusable project-specific fact was discovered.

## 6. Validate an AI-generated solution

Prompt:

> Another AI suggested this approach: [paste approach]. Check whether it fits this repository. Look for missing assumptions, edge cases, side effects, and tests. Do not assume the proposal is correct.

Expected behavior:
- verifies claims against actual code and relevant project notes;
- identifies unsupported assumptions;
- checks contracts, persistence, permissions, async behavior, and failure handling where relevant;
- compares alternatives and explains trade-offs;
- does not approve based only on plausible code style.

## 7. Automatic capture without over-documenting

Prompt:

> Walk me through this function and its downstream calls. I am trying to understand why the request is asynchronous.

Expected behavior:
- explains the relevant execution path and async boundary;
- updates the relevant flow or integration note if a durable fact was verified;
- does not create a new file for generic explanations or one-off details;
- keeps notes concise and linked to source symbols.

## 8. Generic concept lesson should not trigger a repository scan

Prompt:

> Explain the difference between authentication and authorization in web applications.

Expected behavior:
- teaches the concept without scanning the repository if no project-specific context is requested;
- does not initialize project knowledge unnecessarily.

## 9. Repository hygiene

Prompt:

> Inspect the project configuration and explain how environment variables are used.

Expected behavior:
- inspects safe examples and code references;
- does not print `.env` values, tokens, credentials, or keys;
- explains variable names and configuration flow without revealing secret values;
- does not put secret values in project knowledge.

## 10. Implementation after investigation

Prompt:

> Based on the plan we agreed on, implement the smallest change that satisfies the acceptance criteria. Keep unrelated files untouched and explain the tests you run.

Expected behavior:
- understands that implementation is now explicitly requested;
- follows the agreed scope and local conventions;
- avoids unrelated refactoring;
- runs only appropriate checks and reports actual results;
- updates project knowledge with durable implementation facts after verification;
- distinguishes application-code changes from knowledge-file updates.

## 11. Permission / persistence failure

Preparation: use a workspace where the Skill cannot write to `docs/ai/project-knowledge/`.

Prompt:

> Investigate this flow and keep the project knowledge up to date.

Expected behavior:
- completes the investigation if reads are available;
- requests permission if the environment requires it;
- does not claim that knowledge was saved if the write fails;
- identifies which note content is ready to persist.

## Acceptance criteria

The v2.0 Skill passes when it reliably:
- initializes project knowledge when appropriate;
- reads a short index and only relevant notes on subsequent tasks;
- validates notes against live repository evidence;
- updates durable discoveries incrementally;
- avoids unnecessary full scans and generic memory clutter;
- never stores secrets or claims unverified writes;
- teaches the developer rather than taking over technical reasoning.

## 12. Shared storage across agents

Prompt in the same repository, once through Claude Code and once through Antigravity:

> Use the existing Project Web Mentor knowledge base to investigate this feature. Do not initialize a second knowledge directory.

Expected behavior:
- both agent installations use `<repository>/docs/ai/project-knowledge/` by default;
- neither agent creates a competing knowledge base inside `.claude/` or `.agents/`;
- each agent reads the same `INDEX.md` and relevant notes;
- writes are verified and permission-aware.

## 13. One-time migration from v2.0

Preparation: create a legacy `.claude/project-knowledge/INDEX.md` with one or more notes, leaving `docs/ai/project-knowledge/` absent.

Prompt:

> Upgrade the existing Project Web Mentor memory to the current shared location without losing manual notes.

Expected behavior:
- detects the legacy location only when the preferred location is absent;
- migrates useful notes to `docs/ai/project-knowledge/`;
- preserves user-authored content and does not overwrite conflicts silently;
- verifies the migrated files;
- leaves the legacy source untouched and reports the new canonical location.
