"""Teaching crawler package."""

from .crawler import CrawlResult, crawl_site, should_exclude_url

__all__ = ["CrawlResult", "crawl_site", "should_exclude_url"]
