# 02 - Agentic Development Flow

This page explains how agents work with GitHub Actions in this project.

## 1. What is agentic development?

Agentic development means an AI agent helps with software work.

The agent might:

- read an issue
- inspect code
- make a plan
- edit files
- run tests
- open a pull request

The important rule is:

```text
Planning and execution should be separate.
```

Why? Because humans need to review what the agent plans before it changes things. Painful but wise.

## 2. The two important markdown files

### `AGENTS.md`

This is the project handbook for agents.

It says how agents should work in this repository.

Examples:

- run `pytest`
- keep changes small
- do not remove tests
- explain validation

### `agent-plan.md`

This is the plan for one specific task.

It says what the agent intends to do for this task.

Examples:

- goal
- assumptions
- proposed steps
- likely files to change
- risks
- validation

## 3. Difference between them

| File | Question it answers |
|---|---|
| `AGENTS.md` | How should agents work in this repo? |
| `agent-plan.md` | What should the agent do for this task? |

Analogy:

```text
AGENTS.md = employee handbook
agent-plan.md = work order for today's job
```

## 4. Agentic flow in this project

```text
task idea
  ↓
agent-plan.yml
  ↓
agent-plan.md pull request
  ↓
human reviews the plan
  ↓
agent-execute.yml
  ↓
execution report pull request
  ↓
CI tests
  ↓
human review
```

## 5. Workflow 1: agent-plan.yml

Open:

```text
.github/workflows/agent-plan.yml
```

This workflow is started manually using `workflow_dispatch`.

It asks for a task description.

Example task:

```text
Improve the crawler exclude path behaviour and update tests.
```

Then it:

1. Checks out the repository.
2. Sets up Python.
3. Runs `scripts/create_agent_plan.py`.
4. Validates the plan.
5. Creates a branch.
6. Opens a pull request containing the plan.

This is planning, not execution.

## 6. Workflow 2: agent-execute.yml

Open:

```text
.github/workflows/agent-execute.yml
```

This workflow is also started manually.

It reads an approved plan, then:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Reads `AGENTS.md`.
5. Reads `agent-plan.md`.
6. Validates the plan.
7. Runs the simulated agent execution.
8. Runs tests.
9. Opens a pull request with an execution report.

This is execution after planning.

## 7. Why the agent execution is simulated

This project does not call a real AI model.

That is deliberate.

A real coding agent may need:

- an API key
- billing
- network access
- more security controls
- more careful permissions

The simulator teaches the workflow shape safely.

The pattern is what matters:

```text
approved plan -> controlled execution -> tests -> PR
```

## 8. Where a real agent would go

In `agent-execute.yml`, this step runs the simulator:

```yaml
- name: Simulate agent execution
  run: python scripts/agent_execute_simulator.py --plan "${{ inputs.plan_path }}"
```

A real project might replace it with something like:

```yaml
- name: Run real coding agent
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  run: ./scripts/run-real-agent.sh "${{ inputs.plan_path }}"
```

The exact command depends on your agent tool.

## 9. Permissions

Planning workflow:

```yaml
permissions:
  contents: write
  pull-requests: write
```

Execution workflow:

```yaml
permissions:
  contents: write
  pull-requests: write
  actions: read
```

Why not give everything?

Because workflows can be attacked or misconfigured. Least privilege means each workflow receives only the access it needs.

Tiny permissions, fewer disasters. Deeply unfashionable, deeply useful.

## 10. The safest agentic rule

Use this rule:

```text
No execution before a reviewed plan.
```

Then use this rule too:

```text
No merge before tests and human review.
```

Agents can help. They should not become invisible maintainers with unchecked power.
