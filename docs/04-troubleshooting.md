# 04 - Troubleshooting

This page helps when things fail.

They will fail. This is normal.

## Problem: I do not know where to start

Start here and stop there:

1. Open `phases/README.md`.
2. Open `phases/01-foundations/README.md`.
3. Run `pytest`.
4. Read `.github/workflows/ci.yml`.

Do not open later phases yet.

## Problem: I do not see workflows in the Actions tab

Check:

1. Is the folder named exactly `.github/workflows/`?
2. Are the files ending in `.yml` or `.yaml`?
3. Did you push the files to GitHub?
4. Is GitHub Actions enabled for the repository?

## Problem: CI fails at install step

Look for:

- Python version problem
- typo in `pyproject.toml`
- missing dependency
- broken package install

Try locally:

```bash
pip install -e '.[dev]'
```

If your shell is not `zsh`, the unquoted version may also work.

## Problem: CI fails at test step

Run locally:

```bash
pytest
```

Fix the failing test or code.

Do not delete the test unless the test is truly wrong.

## Problem: agent-plan workflow cannot open a pull request

Check repository settings:

1. Go to repository **Settings**.
2. Go to **Actions**.
3. Go to **General**.
4. Find **Workflow permissions**.
5. Allow GitHub Actions to create and approve pull requests if your repo requires that.

Also check the workflow has:

```yaml
permissions:
  contents: write
  pull-requests: write
```

## Problem: agent-execute workflow fails because no changes were committed

The current workflow creates `AGENT_EXECUTION_REPORT.md`, so there should be a change.

If you already ran it and the same branch or file exists, use a new run.

The branch name includes the workflow run ID, so it should usually be unique.

## Problem: YAML error

YAML is sensitive to indentation.

Use spaces, not tabs.

Bad:

```yaml
jobs:
 test:
```

Better:

```yaml
jobs:
  test:
```

## Problem: I am overwhelmed

Use only this path first:

1. Read `README.md`
2. Read `phases/README.md`
3. Read `phases/01-foundations/README.md`
4. Run `pytest`
5. Read `.github/workflows/ci.yml`
6. Watch one GitHub Actions run

Stop there if needed.

That is a complete study session.
