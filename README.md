# GitHub Actions Learning Path for Web Teams

This repository is a teaching project.

It is built to help students learn GitHub Actions in a way that stays concrete instead of abstract.

It now has two layers:

1. A small runnable Python project.
2. A phase-by-phase lesson path for students who want to grow from beginner level to professional web-team workflow knowledge.

The Python crawler is here to make automation real and visible.

The later phases add web-team workflow examples and explanations without pretending this repository is already a full web application.

## Start here

If you are new, anxious, overloaded, or easily lost in large projects, use this order and do not skip ahead:

1. Open `phases/README.md`.
2. Complete `phases/01-foundations/README.md`.
3. Run the local commands in this repository.
4. Watch the active CI workflow on GitHub.
5. Move to the next phase only when the current one makes sense.

That is the rule for this repository:

```text
One phase at a time.
```

## What is active in this repository right now

These files are real and active:

- `.github/workflows/ci.yml`
- `.github/workflows/agent-plan.yml`
- `.github/workflows/agent-execute.yml`
- `crawler_tool/`
- `tests/`
- `scripts/`

These files are study material and examples:

- `phases/`
- `docs/`

Important:

```text
GitHub only runs workflow files that live in .github/workflows/
```

The YAML files inside `phases/*/examples/` are study examples. They do not run automatically in this repository.

## What this repository teaches well

This repository is strong at teaching:

- what a workflow is
- what triggers are
- what jobs and steps are
- how logs look
- how CI failure feels
- how agent planning and execution can be separated

## What this repository does not pretend to be

This is not already a full production web application.

It does not already contain:

- a Node or TypeScript app
- a real frontend build
- a real preview deployment
- a real production deployment
- a real LLM-backed coding agent

Instead, the later phases show students how those workflows are usually designed on web teams.

## Learning path

| Phase | Folder | Main outcome |
|---|---|---|
| 1 | `phases/01-foundations/` | Understand basic GitHub Actions concepts and the active CI workflow in this repo. |
| 2 | `phases/02-web-ci/` | Understand what a real web CI pipeline usually runs. |
| 3 | `phases/03-team-workflow/` | Understand pull request checks, branch protection, path filters, and team workflow discipline. |
| 4 | `phases/04-deployments/` | Understand preview, staging, and production deployment workflow design. |
| 5 | `phases/05-professional-patterns/` | Understand reusable workflows, artifacts, scaling patterns, and security basics. |

## Suggested study pace

If a student finds tooling hard to hold in working memory, use this pace:

- Session 1: Phase 1 only
- Session 2: Repeat Phase 1, then start Phase 2
- Session 3: Phase 2 only
- Session 4: Phase 3
- Session 5: Phase 4
- Session 6: Phase 5

Repeating one phase is normal. It is not failure.

## Project structure

```text
.
├── .github/
│   └── workflows/
│       ├── README.md
│       ├── ci.yml
│       ├── agent-plan.yml
│       └── agent-execute.yml
├── AGENTS.md
├── agent-plan.md
├── crawler_tool/
│   ├── __init__.py
│   ├── cli.py
│   └── crawler.py
├── docs/
│   ├── 01-github-actions-for-beginners.md
│   ├── 02-agentic-development-flow.md
│   ├── 03-file-by-file-tour.md
│   ├── 04-troubleshooting.md
│   └── SOURCES.md
├── examples/
│   ├── config.json
│   └── site_map.json
├── phases/
│   ├── README.md
│   ├── 01-foundations/
│   ├── 02-web-ci/
│   ├── 03-team-workflow/
│   ├── 04-deployments/
│   └── 05-professional-patterns/
├── scripts/
│   ├── agent_execute_simulator.py
│   ├── create_agent_plan.py
│   └── validate_agent_plan.py
├── tests/
│   └── test_crawler.py
└── pyproject.toml
```

## Run the active project locally

You need Python 3.11 or newer.

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

macOS or Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install the project

If your shell is `zsh`, quote the extras part:

```bash
pip install -e '.[dev]'
```

### 4. Run tests

```bash
pytest
```

### 5. Run the crawler

```bash
python -m crawler_tool.cli --start https://example.com/ --site-map examples/site_map.json --exclude /admin --exclude /private
```

Expected result:

- public pages appear in `visited`
- admin and private pages appear in `skipped`

## Read in this order

If you want the shortest useful reading order:

1. `README.md`
2. `phases/README.md`
3. `phases/01-foundations/README.md`
4. `docs/01-github-actions-for-beginners.md`
5. `.github/workflows/ci.yml`
6. `tests/test_crawler.py`
7. `docs/04-troubleshooting.md`

After that:

8. `docs/02-agentic-development-flow.md`
9. `phases/02-web-ci/README.md`
10. `phases/03-team-workflow/README.md`
11. `phases/04-deployments/README.md`
12. `phases/05-professional-patterns/README.md`

## For teachers or mentors

This repository is designed to support mixed-ability learners.

The best way to use it is:

1. Give one phase at a time.
2. Ask the student to explain the workflow in plain language.
3. Ask the student to predict what will happen before they run anything.
4. Let the student inspect logs slowly.
5. Revisit the same phase before adding more moving parts.

## Core message

Students do not need to know everything at once.

They need a stable path, real examples, repeated vocabulary, and enough context to understand why each workflow exists.
