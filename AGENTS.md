# AGENTS.md

This file contains standing instructions for AI agents working in this repository.

Think of this file as the project handbook.

It applies to every task, not just one task.

## Project overview

This is a teaching project for GitHub Actions and agentic development.

The code is a small Python crawler that reads a fake website map from JSON. It does not make real network requests.

## Agent rules

1. Read this file before making changes.
2. Read `agent-plan.md` before executing a task.
3. Do not change production-like logic without tests.
4. Do not remove tests to make the build pass.
5. Prefer small pull requests.
6. Explain what changed and how it was validated.
7. Do not edit secrets, credentials, or workflow permissions without explicit approval.

## Commands

Install:

```bash
pip install -e .[dev]
```

Run tests:

```bash
pytest
```

Run crawler:

```bash
python -m crawler_tool.cli --start https://example.com/ --site-map examples/site_map.json --exclude /admin --exclude /private
```

## Code style

- Use plain Python.
- Keep functions small.
- Add tests when behaviour changes.
- Prefer clear names over clever names. Clever names are how bugs wear tiny moustaches.

## Pull request expectations

Each PR should include:

- What changed.
- Why it changed.
- How it was tested.
- Any risks or limitations.

## Difference from agent-plan.md

`AGENTS.md` tells the agent how to work in this repository.

`agent-plan.md` tells the agent what to do for one specific task.
