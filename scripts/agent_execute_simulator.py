"""Simulate agent execution for teaching.

A real agent might call an LLM, edit code, run tools, and open a PR.

This simulator does something safer for beginners:

1. Reads AGENTS.md.
2. Reads agent-plan.md.
3. Checks that the plan has required sections.
4. Writes AGENT_EXECUTION_REPORT.md.

This gives the workflow something concrete to do without requiring an API key.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from validate_agent_plan import validate_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulate an agent execution run.")
    parser.add_argument("--plan", default="agent-plan.md", help="Path to approved plan")
    parser.add_argument("--agents", default="AGENTS.md", help="Path to AGENTS.md")
    parser.add_argument("--out", default="AGENT_EXECUTION_REPORT.md", help="Output report")
    args = parser.parse_args()

    plan_path = Path(args.plan)
    agents_path = Path(args.agents)
    out_path = Path(args.out)

    if not agents_path.exists():
        print(f"Missing {agents_path}")
        return 1
    if not plan_path.exists():
        print(f"Missing {plan_path}")
        return 1

    missing = validate_plan(plan_path)
    if missing:
        print("Cannot execute. Plan is missing required sections:")
        for section in missing:
            print(f"- {section}")
        return 1

    plan_text = plan_path.read_text(encoding="utf-8")
    agents_text = agents_path.read_text(encoding="utf-8")

    report = f"""# Agent Execution Report

Generated at: {datetime.now(timezone.utc).isoformat()}

## What happened

This was a simulated agent execution run.

The simulator read:

- `{agents_path}`
- `{plan_path}`

It validated the plan and confirmed that the project still has a clear execution path.

## Why this exists

This teaches the shape of agent execution without calling a real AI model.

In a real project, this step could call a coding agent. The important pattern is the same:

```text
approved plan -> controlled workflow -> agent execution -> tests -> PR
```

## Safety checks performed

- Confirmed `AGENTS.md` exists.
- Confirmed the plan exists.
- Confirmed the plan has required sections.
- Prepared this execution report for review.

## Plan preview

```text
{plan_text[:1000]}
```

## Agent instructions preview

```text
{agents_text[:1000]}
```
"""

    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
