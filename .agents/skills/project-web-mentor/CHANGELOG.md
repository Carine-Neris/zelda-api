# Changelog

## 2.0.1

- Changed the default project knowledge directory to `docs/ai/project-knowledge/` so Claude Code and Antigravity share one neutral repository-local memory.
- Updated all instructions, templates, evaluation cases, and installation guidance for both agents.
- Added a safe one-time migration path from the legacy `.claude/project-knowledge/` directory.
- Generalized project-instruction references to include `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md`.

## 2.0.0

- Added repository-local project knowledge with first-run initialization.
- Added incremental recall: index first, relevant notes only.
- Added source validation and note freshness states.
- Added automatic capture of durable, verified discoveries.
- Added evidence, verification date, and optional commit metadata.
- Added rules to keep project knowledge separate from the Skill installation directory.
- Updated discovery, task-investigation, knowledge templates, README, and evaluation prompts.
