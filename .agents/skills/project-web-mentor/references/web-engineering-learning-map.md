# Web Engineering Learning Map

Use this as a menu for targeted teaching. Do not teach every topic at once. Pick the smallest set needed to understand the current feature or task.

## 1. Browser and frontend runtime

Topics:
- browser responsibilities: parsing, rendering, JavaScript execution, storage, and networking;
- DOM, component tree, rendering lifecycle, and event handling;
- client-side routing and navigation;
- local UI state vs server state;
- loading, success, empty, and error states;
- forms, validation, controlled inputs, and accessibility basics.

Questions to help the developer reason:
- Which state belongs in the browser, and which is authoritative on the server?
- What causes this component to render again?
- What happens when the user navigates away while a request is pending?

## 2. HTTP and API design

Topics:
- request/response model;
- methods and semantics: GET, POST, PUT, PATCH, DELETE;
- status codes, headers, body, content types;
- resource-oriented API design;
- validation and serialization;
- pagination, filtering, sorting, and versioning;
- idempotency and safe retries;
- CORS, cookies, caching, and browser security boundaries.

Questions:
- What is the resource or action represented by this endpoint?
- What does the status code communicate to the client?
- Could a retry repeat a side effect?

## 3. Backend request lifecycle

Topics:
- server startup and routing;
- middleware, dependencies, filters, and interceptors;
- controller/handler vs application service vs domain logic;
- synchronous vs asynchronous execution;
- dependency injection and lifecycle scope;
- exception handling and response mapping.

Questions:
- What executes before the handler?
- Where is the business rule enforced?
- Which layer owns this decision, and how do tests show that?

## 4. Data and persistence

Topics:
- relational modeling and normalization;
- ORM models vs API schemas/DTOs;
- repositories and query composition;
- transactions, isolation, and consistency;
- indexes, query plans, and N+1 behavior;
- migrations and backward compatibility;
- ownership and authorization at the data boundary.

Questions:
- What data is authoritative?
- Which operations must succeed or fail together?
- Does this query load more data than the page needs?

## 5. Identity, security, and trust boundaries

Topics:
- authentication vs authorization;
- sessions vs tokens at a conceptual level;
- cookie attributes and browser credential behavior;
- CSRF, XSS, and CORS as distinct concepts;
- input validation and output encoding;
- secret management and least privilege.

Questions:
- Who is the caller, and what are they allowed to do?
- Where is authorization enforced, not merely hidden in the UI?
- Which boundary receives untrusted input?

## 6. Distributed behavior and integrations

Topics:
- external API calls;
- timeouts, retries, backoff, and circuit breakers;
- queues, workers, events, and scheduled jobs;
- idempotency and duplicate delivery;
- eventual consistency and status tracking;
- partial failure and compensation.

Questions:
- What if the dependency is slow or unavailable?
- What happens if the same event arrives twice?
- Does the user wait for the work, or is it asynchronous?

## 7. Delivery, operations, and quality

Topics:
- environments and configuration;
- Docker/container basics;
- CI/CD and deployment lifecycle;
- logs, metrics, traces, and correlation IDs;
- unit, integration, contract, and end-to-end testing;
- feature flags and safe rollout.

Questions:
- How would a failure be detected and diagnosed?
- Which environment/configuration is this code using?
- What is the smallest test that proves the behavior?

## Teaching format

For a selected concept, use this sequence:
1. **Problem:** what practical problem does this concept solve?
2. **Mental model:** explain it in plain language.
3. **In this project:** point to the concrete implementation and evidence.
4. **Under the hood:** show the protocol/runtime/framework detail that matters.
5. **Failure modes:** explain common mistakes and symptoms.
6. **Recognition:** tell the developer what clues to look for next time.

Introduce jargon only when useful and define it on first use. Clearly distinguish web standards from the framework's implementation choices.
