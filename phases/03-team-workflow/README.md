# Phase 3: Team Workflow

This phase teaches the workflow rules that matter when more than one person is changing the codebase.

The core idea is simple:

```text
A team workflow is not only about running commands.
It is about deciding when they run, what they block, and which changes matter.
```

## Main goal

By the end of this phase, the student should understand:

- why pull request checks exist
- why required checks matter
- why branch protection is not the same as CI
- why path filters and concurrency reduce noise

## Files in this phase

Read these files in order:

1. `phases/03-team-workflow/README.md`
2. `phases/03-team-workflow/examples/pull-request-checks-example.yml`
3. `docs/04-troubleshooting.md`

## What this phase adds

Phase 2 answered:

```text
What should CI run?
```

Phase 3 answers:

```text
When should it run?
What should it block?
How do teams stop duplicate or irrelevant runs?
```

## Study example

Open:

```text
phases/03-team-workflow/examples/pull-request-checks-example.yml
```

This example introduces:

- `pull_request` as the main review event
- `paths` filters
- `concurrency`
- separate jobs with `needs`

## Concepts that students often mix up

### CI checks

These are the jobs that run.

Example:

- lint
- tests
- build

### Branch protection

This is a GitHub repository setting.

It decides whether a branch can be merged without passing required checks.

Important:

```text
The workflow file defines checks.
Repository settings decide which checks are required.
```

### Path filters

Path filters stop a workflow from running when changed files do not matter to that workflow.

Example:

- docs-only changes should not always trigger expensive frontend tests

### Concurrency

Concurrency prevents old runs from wasting time when a new commit replaces them.

Example:

- a student pushes three commits to the same pull request
- the oldest runs are no longer useful
- GitHub can cancel them

## Practice exercise

Ask the student to explain this sentence:

```text
We only want this workflow to run for pull requests that touch the web app,
and we want old runs for the same pull request to stop when a newer commit arrives.
```

Then ask the student to point to:

1. the event block
2. the path filters
3. the concurrency block
4. the first job that must pass before the next one can start

## Stop and check

Do not move to Phase 4 until the student can answer:

1. Why is CI not the same thing as branch protection?
2. Why would a team use path filters?
3. Why would a team cancel in-progress runs?
4. What does `needs` do?

## Finish line

A student is ready for Phase 4 when they can look at a pull request workflow and explain which part controls triggering, blocking, job order, and noise reduction.
