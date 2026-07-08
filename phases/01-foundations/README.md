# Phase 1: Foundations

This phase is for students who are new to GitHub Actions or new to automation work.

It uses the active files in this repository.

Do not skip this phase.

## Main goal

By the end of this phase, the student should be able to say:

```text
GitHub Actions runs a workflow when an event happens.
The workflow runs jobs.
The jobs run steps.
The logs show what happened.
```

## Why this phase exists

Many students get lost because GitHub Actions introduces several new words at once.

This phase keeps the workflow simple on purpose.

The project is a tiny Python crawler, but the real lesson is the automation around it.

## What to open

Open these files in this exact order:

1. `README.md`
2. `docs/01-github-actions-for-beginners.md`
3. `.github/workflows/ci.yml`
4. `tests/test_crawler.py`
5. `docs/04-troubleshooting.md`

## Vocabulary to learn first

Learn these words before doing anything harder:

- workflow
- event
- runner
- job
- step
- action
- log
- pass
- fail

If the student cannot explain those words yet, stay in this phase.

## What the active CI workflow does

The active CI workflow is `.github/workflows/ci.yml`.

It does four simple things:

1. Starts on `push` and `pull_request`
2. Checks out the repository
3. Sets up Python
4. Installs dependencies and runs `pytest`

That is enough to teach the basic shape of CI.

## Why the project uses Python here

This repository is preparing students for web-team workflow design, but Phase 1 keeps the code small and quiet.

If the first lesson also included a full frontend toolchain, many students would lose track of what GitHub Actions is actually doing.

The Python crawler is a teaching support tool, not the final target career stack.

## Practice steps

### Step 1: Run the tests locally

```bash
pytest
```

Meaning:

- if tests pass locally, the project is in a good state right now
- if tests fail locally, CI will likely fail too

### Step 2: Read the workflow top to bottom

Open `.github/workflows/ci.yml`.

Ask these questions:

1. What event starts the workflow?
2. What permissions does it have?
3. What machine does it run on?
4. What exact commands or actions run?

### Step 3: Watch a real run on GitHub

After pushing the repository to GitHub:

1. Open the **Actions** tab.
2. Open the **CI** workflow.
3. Open one run.
4. Open the `Run Python tests` job.
5. Expand each step.

The student should say out loud what each step is doing.

### Step 4: Make the workflow fail on purpose

Change one expectation in `tests/test_crawler.py` so the test becomes wrong.

Then:

1. run `pytest`
2. see it fail
3. fix the test
4. run `pytest` again

This is important.

Students need to learn that a failed workflow is information, not punishment.

## Stop and check

Do not move to Phase 2 until the student can answer these questions:

1. What is the difference between a workflow and a job?
2. What is the difference between `uses` and `run`?
3. Why does CI run tests automatically?
4. Where do you look first when a workflow fails?

## Common confusion

### "Do I need to understand all of YAML?"

No.

At this stage, the student only needs to understand:

- indentation matters
- `on` means what starts the workflow
- `jobs` contains the work
- `steps` contains the step-by-step actions

### "Do I need to understand Python?"

Not deeply.

The student only needs to know that `pytest` is the test command for this repository.

### "What if I feel behind?"

Repeat this phase.

That is normal.

## Finish line

A student is ready for Phase 2 when they can:

- explain the active CI workflow in plain language
- run `pytest` locally
- find the failing step in a GitHub Actions run
- say why CI is useful on a team
