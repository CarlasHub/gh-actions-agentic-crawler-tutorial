# Agent Plan: Add and Validate Exclude Paths for the Crawler

## Status

Planning example. Human review recommended before execution.

## Goal

Make sure the crawler can skip excluded paths such as `/admin`, `/private`, and `/logout` while crawling a fake website map.

## Context

The project is a teaching project for GitHub Actions and agentic development.

The crawler reads a fake site map from JSON. It does not visit the real internet.

## Assumptions

- A URL should be skipped if its path begins with an excluded path.
- Excluded paths are configured through CLI flags or config values.
- The crawler should stay on the same domain as the start URL.
- Tests should prove that excluded paths are not visited.

## Proposed steps

1. Read `AGENTS.md`.
2. Read this plan.
3. Inspect `crawler_tool/crawler.py`.
4. Inspect `crawler_tool/cli.py`.
5. Inspect `tests/test_crawler.py`.
6. Run tests with `pytest`.
7. If changes are needed, update crawler logic and tests.
8. Run tests again.
9. Open a pull request with a clear summary.

## Files likely to change

- `crawler_tool/crawler.py`
- `crawler_tool/cli.py`
- `tests/test_crawler.py`
- `docs/02-agentic-development-flow.md`

## Risks

- Excluding paths too broadly could skip valid pages.
- Excluding paths too narrowly could allow private pages to be crawled.
- A real crawler would need robots.txt, rate limiting, user-agent handling, and network safety. This teaching project does not implement those.

## Validation

Run:

```bash
pytest
```

Expected result:

- Tests pass.
- Pages under `/admin` and `/private` are not visited.
- Public pages are still visited.

## Approval

Human approval required before real agent execution: yes.
