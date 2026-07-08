# Phase 2: Real Web CI

This phase explains what a professional web-team CI workflow usually does.

Important:

The files in this phase are examples for study.

They are not active in this repository.

## Main goal

By the end of this phase, the student should understand why web teams usually run these checks in CI:

- dependency install
- lint
- typecheck
- unit tests
- build

## Why this phase matters

In many beginner tutorials, CI means only "run tests."

That is too small for web work.

A web application can be broken even when unit tests pass.

Examples:

- code style is broken
- TypeScript types are broken
- the production build fails
- one package lock file is out of sync

This phase teaches the minimum useful web CI mental model.

## Files in this phase

Read these files in order:

1. `phases/02-web-ci/README.md`
2. `phases/02-web-ci/examples/web-ci-example.yml`
3. `docs/01-github-actions-for-beginners.md`

## What is different from Phase 1

Phase 1 used a small Python project so the workflow shape stayed simple.

Phase 2 moves to the workflow shape you would usually see on a frontend or full-stack web team.

## Study example

Open:

```text
phases/02-web-ci/examples/web-ci-example.yml
```

This example shows:

- `actions/setup-node`
- npm dependency caching
- one standard CI job for a web repo
- the common command order:
  1. `npm ci`
  2. `npm run lint`
  3. `npm run typecheck`
  4. `npm test`
  5. `npm run build`

## Why the order matters

This order is common because:

1. install must happen first
2. lint and typecheck are usually faster than tests
3. build often catches integration problems late in the pipeline

If lint fails, there is no reason to continue.

That saves time and money.

## What each command is checking

| Command | What it protects |
|---|---|
| `npm ci` | repeatable dependency install |
| `npm run lint` | code quality and style rules |
| `npm run typecheck` | TypeScript correctness |
| `npm test` | behavior checks |
| `npm run build` | production build health |

## Example mapping to a typical web project

A common `package.json` script setup looks like this:

```json
{
  "scripts": {
    "lint": "eslint .",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "build": "vite build"
  }
}
```

This repository does not contain that web app.

This example exists so the student learns the workflow shape before building their own.

## Practice exercise

Ask the student to explain this workflow in plain language:

```text
When a pull request is opened or code is pushed to main,
GitHub installs dependencies, checks the code, runs tests,
and confirms the app can build.
```

Then ask:

1. Why is `npm ci` better than `npm install` in CI?
2. Why should `build` run in CI?
3. What does caching help with?

## Stop and check

Do not move to Phase 3 until the student can answer:

1. Why are tests alone not enough for web CI?
2. What problem does `npm ci` solve?
3. What is the purpose of a build step in CI?

## Finish line

A student is ready for Phase 3 when they can read a Node-based CI workflow without feeling lost and can explain why each quality check exists.
