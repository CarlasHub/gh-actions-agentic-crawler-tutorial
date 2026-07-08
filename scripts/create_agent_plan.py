"""Create a simple agent-plan.md from a task description.

This is not a real AI planner.
It is a safe teaching script that produces a predictable plan.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = """# Agent Plan: {title}

## Status

Draft plan created by the planning workflow.

## Goal

{task}

## Context

This repository is a teaching project for GitHub Actions and agentic development.

The project contains a fake crawler that reads a site map from JSON and skips excluded paths.

## Assumptions

- The task should keep the crawler offline and testable.
- The agent should read `AGENTS.md` before execution.
- The agent should run tests before opening a pull request.
- Any behaviour change should include tests.

## Proposed steps

1. Read `AGENTS.md`.
2. Read this plan.
3. Inspect the crawler code.
4. Inspect the tests.
5. Make the smallest useful change.
6. Run `pytest`.
7. Summarise changes in a pull request.

## Files likely to change

- `crawler_tool/crawler.py`
- `crawler_tool/cli.py`
- `tests/test_crawler.py`
- `docs/02-agentic-development-flow.md`

## Risks

- The agent could change more than the task requires.
- Exclude path behaviour could become too broad or too narrow.
- Tests could pass while missing real-world crawler concerns.

## Validation

Run:

```bash
pytest
```

Expected result:

- All tests pass.
- Excluded paths are skipped.
- Public pages are still visited.

## Approval

Human approval required before execution: yes.

## Generated at

{generated_at}
"""


def title_from_task(task: str) -> str:
    words = task.strip().split()
    if not words:
        return "Untitled Task"
    return " ".join(words[:8]).rstrip(".,")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an agent plan from a task description.")
    parser.add_argument("--task", required=True, help="Task description")
    parser.add_argument("--out", default="agent-plan.md", help="Output file path")
    args = parser.parse_args()

    out = Path(args.out)
    plan = TEMPLATE.format(
        title=title_from_task(args.task),
        task=args.task.strip(),
        generated_at=datetime.now(timezone.utc).isoformat(),
    )
    out.write_text(plan, encoding="utf-8")
    print(f"Created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
