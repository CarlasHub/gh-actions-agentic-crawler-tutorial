# 03 - File-by-File Tour

This page explains the important folders in the repository.

The project now has two kinds of material:

1. active project files
2. study material for later phases

Keeping those two groups separate helps students understand what is real, what is runnable, and what is only an example.

## Active workflow folder: `.github/workflows/`

This folder contains the workflows GitHub can actually run in this repository.

Files:

- `ci.yml`
- `agent-plan.yml`
- `agent-execute.yml`
- `README.md`

Only workflow files inside `.github/workflows/` are active on GitHub.

## Student roadmap folder: `phases/`

This folder is the guided curriculum.

Folders:

- `phases/01-foundations/`
- `phases/02-web-ci/`
- `phases/03-team-workflow/`
- `phases/04-deployments/`
- `phases/05-professional-patterns/`

Each phase has a `README.md` lesson.

Some phases also contain `examples/` folders with workflow templates for study.

These example workflows do not run automatically.

## Reference docs folder: `docs/`

This folder contains supporting explanations.

Files:

- `01-github-actions-for-beginners.md`
- `02-agentic-development-flow.md`
- `03-file-by-file-tour.md`
- `04-troubleshooting.md`
- `SOURCES.md`

These are support documents, not the main phase path.

## `AGENTS.md`

Standing instructions for AI agents working in this repository.

This is for repository behavior and change rules.

## `agent-plan.md`

A task-specific plan example.

This shows how a single task can be described before execution.

## `crawler_tool/`

The fake crawler logic used by the active Python project.

Important files:

- `crawler.py`
- `cli.py`

This code exists so the CI workflow has something real to test.

## `examples/`

Sample data for the crawler.

Files:

- `site_map.json`
- `config.json`

This is fake website data, not real network crawling.

## `tests/`

Tests for the crawler.

GitHub Actions runs these through `pytest`.

This folder is part of the active project.

## `scripts/`

Support scripts for the agent workflow teaching flow.

Files:

- `create_agent_plan.py`
- `validate_agent_plan.py`
- `agent_execute_simulator.py`

These are active scripts used by the example agent workflows.
