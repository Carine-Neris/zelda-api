# Task Analysis Playbook

Use this playbook before implementing a bug fix or feature in an unfamiliar or complex codebase.

## 1. Consult project knowledge, then translate the task into behavior

Before searching the code, read the project knowledge `INDEX.md` and only the notes relevant to this ticket. Treat them as a map, not as truth: validate the current behavior against source code and tests. If no index exists, initialize a small, scoped knowledge base as findings are verified; do not force a full-repository discovery for a narrow ticket.


Summarize:
- current behavior;
- desired behavior;
- actor and trigger;
- acceptance criteria;
- constraints and non-goals.

Separate ticket facts from assumptions. Avoid converting a vague ticket directly into a code change.

## 2. Find the current behavior

Search for the user-facing label, route, endpoint, domain term, event, model, or nearby test. Follow references from the most concrete entry point. Prefer symbol/reference search over guessing file names.

Record the path with evidence:

`trigger → frontend state/action → request/client → API route → validation/auth → service/use case → persistence/integration → response → UI state`

Adapt this path to the actual architecture. Some systems do not have a separate service or repository layer.

## 3. Identify the relevant contracts

Inspect the boundaries the task touches:
- request/response schema and API compatibility;
- domain invariants and validation;
- frontend component props and state transitions;
- database constraints, relationships, and transaction behavior;
- permissions and data ownership;
- events, queues, retries, and idempotency;
- external service contracts and failure behavior.

Explain what each contract protects and what could break if it changes.

## 4. Search for existing patterns

Find one or two analogous implementations. Compare:
- code organization;
- naming and error conventions;
- validation and authorization;
- transaction boundaries;
- async behavior;
- tests and fixtures.

Do not copy a nearby pattern blindly. Check whether its domain assumptions match the current task.

## 5. Map impact and edge cases

Consider, where relevant:
- success, empty, loading, and error states;
- duplicate submissions and retries;
- missing, malformed, stale, or unauthorized data;
- concurrency and partial failure;
- pagination, sorting, and filtering;
- backwards compatibility;
- migration and rollback implications;
- observability and supportability.

Prioritize realistic risks rather than listing every imaginable edge case.

## 6. Present options before implementation

For each viable option, state:
- what would change;
- why it fits or conflicts with current architecture;
- benefits and costs;
- operational or compatibility risks;
- how it can be tested.

Then recommend the smallest coherent solution. Avoid speculative abstraction and unrelated refactoring.

## 7. Verification plan

List tests at the right levels:
- unit tests for isolated rules;
- integration tests for persistence, API, or service boundaries;
- frontend/component tests for user-visible state;
- end-to-end tests for critical journeys, if the project has them;
- manual checks only when automation is absent or insufficient.

Inspect existing commands before suggesting one. Mark commands that mutate local state or access external services. Never run destructive or shared-environment commands without explicit permission.

## 8. Update reusable project knowledge

After the investigation, automatically update the smallest relevant project-knowledge note when the work confirmed a reusable flow, contract, module responsibility, convention, decision, or meaningful open question. Update `INDEX.md` to point to the note. Do not save generic explanations, guesses as facts, transient debugging chatter, or large code excerpts. If no durable project-specific information was discovered, do not write anything. Follow `references/project-knowledge-playbook.md` for evidence, freshness, and write rules.

## Standard task-investigation output

### Task in plain language
### What the repository does today
### Relevant execution path
### Important concepts to understand
### Files/symbols likely involved
### Existing patterns and tests
### Options and recommendation
### Risks / unknowns
### Verification plan
### One knowledge checkpoint (optional)

Do not start writing code unless the user asks for implementation. If they do ask, preserve this reasoning in a brief preface and implement only the agreed scope.
