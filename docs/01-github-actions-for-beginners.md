# 01 - GitHub Actions for Beginners

This page explains GitHub Actions slowly and plainly.

## 1. What is GitHub Actions?

GitHub Actions is GitHub's automation system.

Automation means:

```text
When something happens, run some steps automatically.
```

Example:

```text
When someone opens a pull request, run the tests.
```

That is all. The rest is vocabulary and YAML. YAML is the tax we pay for automation.

## 2. What is a workflow?

A workflow is a file that tells GitHub what to automate.

Workflow files live here:

```text
.github/workflows/
```

Example workflow files:

```text
.github/workflows/ci.yml
.github/workflows/agent-plan.yml
.github/workflows/agent-execute.yml
```

A workflow answers four questions:

1. What is the workflow called?
2. What event starts it?
3. What machine should run it?
4. What steps should happen?

## 3. Look at the CI workflow

Open:

```text
.github/workflows/ci.yml
```

You will see this:

```yaml
name: CI
```

This is the name shown in the GitHub Actions tab.

Then:

```yaml
on:
  push:
    branches:
      - main
  pull_request:
```

This means the workflow runs when:

- code is pushed to `main`
- a pull request is opened or updated

Then:

```yaml
permissions:
  contents: read
```

This means the workflow can read the repository contents, but cannot write changes.

This is safer. Give workflows only the permissions they need. Do not hand the robot the house keys because it made eye contact.

Then:

```yaml
jobs:
  test:
```

A job is a group of steps.

Then:

```yaml
runs-on: ubuntu-latest
```

This means GitHub will run the job on a temporary Ubuntu Linux machine.

That machine is called a runner.

Then steps:

```yaml
steps:
  - name: Checkout repository
    uses: actions/checkout@v4
```

This downloads your repository onto the runner.

Without this, the runner has no project files.

Then:

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: "3.12"
```

This installs Python 3.12 on the runner.

Then:

```yaml
- name: Install project and test tools
  run: pip install -e .[dev]
```

This runs a shell command.

Then:

```yaml
- name: Run tests
  run: pytest
```

This runs tests.

If tests pass, the workflow passes.
If tests fail, the workflow fails.

## 4. Key vocabulary

| Word | Plain meaning |
|---|---|
| GitHub Actions | GitHub automation system |
| Workflow | YAML file that defines automation |
| Event | Thing that starts the workflow |
| Job | Group of steps |
| Runner | Temporary machine that runs the job |
| Step | One command or reusable action |
| Action | Reusable automation block |
| `run` | Run a shell command |
| `uses` | Use a reusable action |

## 5. The tiny mental model

```text
event -> workflow -> job -> runner -> steps -> result
```

Example:

```text
pull request -> CI workflow -> test job -> Ubuntu runner -> pytest -> pass/fail
```

## 6. How to see it working on GitHub

1. Push this project to GitHub.
2. Go to the repository page.
3. Click the **Actions** tab.
4. Click **CI**.
5. Click a workflow run.
6. Click the job.
7. Expand each step.

The logs will show exactly what happened.

## 7. How to make it fail on purpose

Open this file:

```text
tests/test_crawler.py
```

Change one expected value to something wrong.

Commit and push.

The CI workflow should fail.

Then fix the test and push again.

This teaches the most important thing: failed workflows are not always bad. They are alarms. Annoying alarms, but still alarms.

## 8. Do not panic when a workflow fails

When a workflow fails:

1. Open the failed run.
2. Open the failed job.
3. Find the red failed step.
4. Read the last 20-40 lines of logs.
5. Fix the actual problem.
6. Push again.

Do not randomly edit YAML while whispering threats at the screen. It rarely helps, despite tradition.
