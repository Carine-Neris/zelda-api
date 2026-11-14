# Project Discovery Playbook

Use this playbook when building the initial mental model of a repository or performing an explicitly requested architecture refresh.

## Goal

Create a reliable map without reading the entire codebase. Prioritize entry points, architectural boundaries, and one representative user journey. Save durable findings to the project knowledge base as part of the discovery.

## Phase 1: Establish repository shape

Inspect, where present:
- top-level directories and likely application roots;
- README and developer documentation;
- package/dependency manifests and lockfiles;
- build, test, lint, and type-check configuration;
- container and deployment configuration;
- CI workflows;
- existing project/agent instruction files such as `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md`, plus architecture docs and local agent instructions.

Do not inspect secret values. Do not dump the entire repository tree. Use targeted directory listings and searches.

Record:
- languages and frameworks confirmed by manifests/imports/config;
- monolith, modular monolith, services, or monorepo evidence;
- frontend and backend roots;
- test locations;
- local development entry points;
- external dependencies and infrastructure clues.

Do not infer architecture solely from folder names.

## Phase 2: Find runtime entry points

Identify actual startup and routing paths. Depending on the stack, inspect:
- application bootstrap / server entry point;
- frontend app bootstrap and route registration;
- API route registration and controllers/handlers;
- dependency injection / providers;
- middleware, filters, interceptors, or request hooks;
- authentication and authorization boundaries;
- background workers, queues, scheduled tasks, and event consumers;
- database connection and migration setup;
- external client/service initialization.

For each entry point, record its file path and evidence establishing its role.

## Phase 3: Map responsibilities and boundaries

Build a concise map using only layers that actually exist. Possible responsibilities include:
- presentation / pages / components;
- client-side routing and state;
- API client / transport layer;
- routes / controllers / handlers;
- application or use-case services;
- domain logic and business rules;
- repositories / data-access layer;
- schemas / DTOs / serializers;
- database models and migrations;
- integrations / external APIs;
- background processing;
- observability and error reporting.

Do not force the codebase into textbook layered architecture if it does not follow one. Describe actual coupling and exceptions.

## Phase 4: Trace a representative end-to-end flow

Choose a common, meaningful feature that crosses important boundaries. Prefer one read flow and one write flow if repository size and task scope justify both. For a first pass, one complete flow is better than several shallow traces.

Trace:
1. user action or external trigger;
2. browser component/page or initiating client;
3. client-side state and request construction;
4. HTTP method, URL, headers, payload, and expected response when visible;
5. route/controller/handler and middleware/dependencies;
6. validation and authorization;
7. application/business logic;
8. data access and transaction boundaries;
9. external calls or asynchronous handoff;
10. response mapping, client state update, rendering, and error behavior.

Use actual symbol names. If a step is outside the repository or cannot be established, mark it unknown.

## Phase 5: Understand cross-cutting behavior

Inspect only what is relevant to the main paths:
- authentication vs authorization;
- configuration and environment separation;
- error handling and API response conventions;
- logging, tracing, and metrics;
- caching;
- retries, timeouts, idempotency, and async processing;
- database transactions and migrations;
- feature flags and permissions;
- test strategy.

Avoid exposing secrets or sensitive data.

## Phase 6: Produce and persist the project map

Present:

### Executive overview
What the application does, its major runtime parts, and strongest architecture evidence.

### System map
A Mermaid flowchart or compact text diagram showing verified components and relationships. Label inferred edges.

### Component responsibility map
| Area | Responsibility | Main files/symbols | Confidence |

### Request lifecycle
Trace the chosen flow in execution order, linking each step to code.

### Data model / persistence overview
Describe key entities, relationships, ownership, and migrations only when verified.

### Integrations and asynchronous work
List external systems, queues, workers, and event flows with evidence.

### Testing and observability
Explain how behavior is tested and how failures can be observed.

### Unknowns and risks
List important unanswered questions, evidence gaps, and the next most valuable investigation.

### Suggested reading order
Provide 3-7 files or symbols and explain why each one is worth reading next.

Then persist the useful findings:
1. Create the knowledge directory and concise `INDEX.md` if absent.
2. Create/update only detailed notes supported by evidence.
3. Link notes from the index and mark coverage accurately.
4. Record material unknowns in `open-questions.md`.
5. Verify that each written file exists and contains the intended content.

## Refreshing the map

Do not run a full discovery on every Skill invocation. For ordinary tasks, read the index, load relevant notes, and validate only the source paths involved. Perform full discovery again only when explicitly requested, when major structural changes are evident, or when several important notes have become unreliable.
