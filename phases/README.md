# Phase Guide

This folder is the student roadmap.

Each phase has one job:

```text
Learn one layer of GitHub Actions without getting buried by the next layer.
```

## Read this before opening any phase

1. Do one phase at a time.
2. Do not open the next phase just because the folder exists.
3. Repeat a phase if the words still feel foggy.
4. Keep notes in plain language.
5. Ask, "What problem is this workflow solving?" before asking, "What does this YAML line do?"

## The five phases

| Phase | Folder | What the student should understand before moving on |
|---|---|---|
| 1 | `01-foundations/` | What a workflow is, what starts it, what a job is, and how to read a failed run. |
| 2 | `02-web-ci/` | Why web teams run lint, typecheck, tests, and builds in CI. |
| 3 | `03-team-workflow/` | Why pull request checks, path filters, concurrency, and branch protection matter. |
| 4 | `04-deployments/` | How preview, staging, and production workflows differ. |
| 5 | `05-professional-patterns/` | How larger teams reuse workflows, pass artifacts, and tighten security. |

## What is active and what is example-only

Active workflows:

- `.github/workflows/ci.yml`
- `.github/workflows/agent-plan.yml`
- `.github/workflows/agent-execute.yml`

Example workflows:

- `phases/*/examples/*.yml`

GitHub will not run the example workflows from this folder unless someone copies them into `.github/workflows/`.

That is intentional. Students need safe reading examples before they need more active automation.

## If the student gets lost

Use this reset path:

1. Go back to `01-foundations/README.md`.
2. Open `.github/workflows/ci.yml`.
3. Answer these three questions:
   - What event starts this workflow?
   - What command does it run?
   - What would make it fail?
4. Run `pytest` locally.
5. Stop there if needed.

That is enough for one study session.
