"""A tiny offline crawler used for teaching GitHub Actions.

This crawler does not make HTTP requests.

Instead, it reads a fake website map like this:

{
  "https://example.com/": ["https://example.com/about"],
  "https://example.com/about": []
}

That makes the tests fast, safe, and predictable.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
from urllib.parse import urlparse


@dataclass(frozen=True)
class CrawlResult:
    """The result returned by the crawler."""

    start_url: str
    visited: tuple[str, ...]
    skipped: tuple[str, ...]


def normalise_exclude_path(path: str) -> str:
    """Return a clean exclude path.

    Examples:
    - "admin" becomes "/admin"
    - "/admin/" becomes "/admin"
    - "/" stays "/"
    """

    cleaned = path.strip()
    if not cleaned:
        return ""
    if not cleaned.startswith("/"):
        cleaned = "/" + cleaned
    if cleaned != "/":
        cleaned = cleaned.rstrip("/")
    return cleaned


def should_exclude_url(url: str, exclude_paths: Iterable[str]) -> bool:
    """Return True if a URL path should be excluded.

    This uses prefix matching.

    If `/admin` is excluded, these are skipped:
    - https://example.com/admin
    - https://example.com/admin/settings

    But this is not skipped:
    - https://example.com/administrator-notes
    """

    path = urlparse(url).path or "/"
    normalised_excludes = [normalise_exclude_path(p) for p in exclude_paths]

    for excluded in normalised_excludes:
        if not excluded:
            continue
        if excluded == "/":
            return True
        if path == excluded or path.startswith(excluded + "/"):
            return True

    return False


def same_domain(url: str, start_url: str) -> bool:
    """Return True if `url` has the same host as `start_url`."""

    return urlparse(url).netloc == urlparse(start_url).netloc


def crawl_site(
    start_url: str,
    site_map: dict[str, list[str]],
    exclude_paths: Iterable[str] | None = None,
    max_pages: int = 50,
) -> CrawlResult:
    """Crawl a fake site map from a start URL.

    Args:
        start_url: URL where crawling starts.
        site_map: Dictionary mapping a URL to the links found on that URL.
        exclude_paths: Paths that must not be visited.
        max_pages: Safety limit to stop infinite crawling.

    Returns:
        CrawlResult containing visited and skipped URLs.
    """

    if max_pages < 1:
        raise ValueError("max_pages must be at least 1")

    excludes = tuple(exclude_paths or ())
    queue: list[str] = [start_url]
    visited: list[str] = []
    skipped: list[str] = []
    seen: set[str] = set()

    while queue and len(visited) < max_pages:
        current = queue.pop(0)

        if current in seen:
            continue
        seen.add(current)

        if not same_domain(current, start_url):
            skipped.append(current)
            continue

        if should_exclude_url(current, excludes):
            skipped.append(current)
            continue

        visited.append(current)

        for link in site_map.get(current, []):
            if link not in seen:
                queue.append(link)

    return CrawlResult(
        start_url=start_url,
        visited=tuple(visited),
        skipped=tuple(skipped),
    )
