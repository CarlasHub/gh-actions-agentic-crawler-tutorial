from crawler_tool.crawler import crawl_site, normalise_exclude_path, should_exclude_url


SITE_MAP = {
    "https://example.com/": [
        "https://example.com/about",
        "https://example.com/admin",
        "https://example.com/private/profile",
        "https://other.example.net/off-site",
    ],
    "https://example.com/about": [
        "https://example.com/contact",
        "https://example.com/admin/settings",
    ],
    "https://example.com/contact": [],
    "https://example.com/admin": [],
    "https://example.com/admin/settings": [],
    "https://example.com/private/profile": [],
}


def test_normalise_exclude_path_adds_leading_slash():
    assert normalise_exclude_path("admin") == "/admin"


def test_normalise_exclude_path_removes_trailing_slash():
    assert normalise_exclude_path("/admin/") == "/admin"


def test_should_exclude_url_exact_path():
    assert should_exclude_url("https://example.com/admin", ["/admin"])


def test_should_exclude_url_nested_path():
    assert should_exclude_url("https://example.com/admin/settings", ["/admin"])


def test_should_not_exclude_similar_prefix_word():
    assert not should_exclude_url("https://example.com/administrator-notes", ["/admin"])


def test_crawl_skips_excluded_paths_and_other_domains():
    result = crawl_site(
        start_url="https://example.com/",
        site_map=SITE_MAP,
        exclude_paths=["/admin", "/private"],
        max_pages=20,
    )

    assert "https://example.com/" in result.visited
    assert "https://example.com/about" in result.visited
    assert "https://example.com/contact" in result.visited

    assert "https://example.com/admin" not in result.visited
    assert "https://example.com/admin/settings" not in result.visited
    assert "https://example.com/private/profile" not in result.visited
    assert "https://other.example.net/off-site" not in result.visited

    assert "https://example.com/admin" in result.skipped
    assert "https://example.com/private/profile" in result.skipped
    assert "https://other.example.net/off-site" in result.skipped


def test_crawl_respects_max_pages():
    result = crawl_site(
        start_url="https://example.com/",
        site_map=SITE_MAP,
        exclude_paths=[],
        max_pages=1,
    )

    assert result.visited == ("https://example.com/",)
