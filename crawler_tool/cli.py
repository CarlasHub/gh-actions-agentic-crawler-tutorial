"""Command-line interface for the teaching crawler."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .crawler import crawl_site


def load_site_map(path: Path) -> dict[str, list[str]]:
    """Load the fake website map from JSON."""

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("site map must be a JSON object")
    return data


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Crawl a fake website map.")
    parser.add_argument("--start", required=True, help="Start URL, for example https://example.com/")
    parser.add_argument("--site-map", required=True, type=Path, help="Path to fake site map JSON")
    parser.add_argument("--exclude", action="append", default=[], help="Path to exclude. Can be used more than once.")
    parser.add_argument("--max-pages", type=int, default=50, help="Maximum number of pages to visit")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    site_map = load_site_map(args.site_map)
    result = crawl_site(
        start_url=args.start,
        site_map=site_map,
        exclude_paths=args.exclude,
        max_pages=args.max_pages,
    )

    print(json.dumps({
        "start_url": result.start_url,
        "visited": list(result.visited),
        "skipped": list(result.skipped),
    }, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
