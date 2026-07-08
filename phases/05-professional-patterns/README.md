# Phase 5: Professional Patterns

This phase teaches the workflow patterns that become important when a team, codebase, or platform grows.

This is the phase where students start thinking like maintainers instead of just workflow readers.

## Main goal

By the end of this phase, the student should understand:

- reusable workflows
- artifacts
- scaling common CI across repositories
- security basics for Actions
- why larger teams avoid copy-pasting workflow logic everywhere

## Files in this phase

Read these files in order:

1. `phases/05-professional-patterns/README.md`
2. `phases/05-professional-patterns/examples/reusable-node-ci-example.yml`
3. `phases/05-professional-patterns/examples/use-reusable-ci-example.yml`

## Why this phase matters

Small projects can survive messy workflows.

Larger teams cannot.

Without reuse and clear security rules, teams usually end up with:

- duplicated YAML
- inconsistent checks across repositories
- secrets spread too widely
- slow maintenance when CI logic changes

## Reusable workflows

A reusable workflow lets one workflow call another workflow with `workflow_call`.

This is useful when many repositories need the same CI behavior.

Example:

- several frontend repositories
- one shared Node CI workflow
- each repository calls the same tested workflow

## Artifacts

Artifacts are files saved by one job so another job can use them later.

Examples:

- test reports
- build output
- screenshots
- deployment bundles

The key idea is simple:

```text
Build once.
Reuse the result.
```

## Security basics students should know

Students do not need deep cloud security knowledge yet, but they do need these rules:

1. Give workflows the smallest permission set that works.
2. Do not store secrets directly in workflow files.
3. Prefer short-lived credentials when your platform supports them.
4. Review third-party actions before trusting them.

## Study examples

Open:

```text
phases/05-professional-patterns/examples/reusable-node-ci-example.yml
phases/05-professional-patterns/examples/use-reusable-ci-example.yml
```

These examples show:

- `workflow_call`
- inputs for reuse
- a shared Node CI workflow
- a repository workflow that calls the shared workflow

The caller example uses:

```text
./.github/workflows/reusable-node-ci.yml
```

That path is what a real repository would use after copying the reusable workflow into its active workflow folder.

## Practice exercise

Ask the student:

1. Why would a company want one reusable CI workflow instead of ten copied versions?
2. What kind of files should be uploaded as artifacts?
3. Why should permissions stay small?
4. What problem does `workflow_call` solve?

## Final readiness check

A student is ready to work with GitHub Actions on a professional web team at entry level when they can:

- read an existing workflow without getting lost
- explain why a workflow triggers
- explain the purpose of each job
- debug a failing step from logs
- describe how CI differs from deployment
- explain why required checks and branch protection matter
- explain why teams reuse workflows and restrict permissions

## Finish line

At the end of this phase, the student should not feel like they know everything.

They should feel like workflows are understandable systems instead of magic files.
