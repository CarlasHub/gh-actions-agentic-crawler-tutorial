# Phase 4: Deployments

This phase teaches the difference between CI and deployment workflows.

Students often mix these up.

CI answers:

```text
Is the change safe enough to continue?
```

Deployment answers:

```text
Where should this version go now?
```

## Main goal

By the end of this phase, the student should understand:

- preview deployment workflows
- staging deployment workflows
- production deployment workflows
- environment approvals
- deployment secrets
- why deployment jobs usually depend on build jobs

## Files in this phase

Read these files in order:

1. `phases/04-deployments/README.md`
2. `phases/04-deployments/examples/preview-deploy-example.yml`
3. `phases/04-deployments/examples/production-deploy-example.yml`

## Why this phase matters on web teams

On a web team, passing tests is not the end of the job.

People also need:

- a preview URL for review
- a safe path to staging
- controlled production releases

That means deployment workflows need rules, not just commands.

## Preview deployments

Preview deployments are usually tied to pull requests.

Their job is to give reviewers something real to click.

Typical use:

- designer checks layout
- QA checks behavior
- reviewer checks the feature in a browser

## Production deployments

Production deployments are usually stricter.

They often include:

- an environment with protected secrets
- a manual approval gate
- a concurrency rule so only one production deploy runs at a time
- a build artifact passed from an earlier job

## Study examples

Open these files:

```text
phases/04-deployments/examples/preview-deploy-example.yml
phases/04-deployments/examples/production-deploy-example.yml
```

These examples show:

- jobs connected with `needs`
- environment names
- artifact upload and download
- deployment outputs
- a production concurrency rule

## Important safety rule

Never teach students to put secrets directly into workflow files.

The safe mental model is:

```text
workflow file asks for secrets
GitHub stores secrets
deployment step reads secrets at runtime
```

## Practice exercise

Ask the student:

1. Why is a preview deployment useful before merge?
2. Why is production usually more restricted than preview?
3. Why might a team require approval before production deploy?
4. Why would a deploy job download an artifact instead of rebuilding from scratch?

## Stop and check

Do not move to Phase 5 until the student can explain the difference between:

- CI and deployment
- preview and production
- repository secrets and environment secrets

## Finish line

A student is ready for Phase 5 when they can describe a deployment workflow as a controlled release process instead of "the part after tests."
