import re
from playwright.sync_api import Page
import pytest

from index import IndexPage
from movies import MoviesPage
from movie import MoviePage

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": {
            "cookies": [
                {
                    "name": "cf_clearance",
                    "value": "yq_R0a.fYwDrDOOMOPQ2YCOfJIVo8OnwNG5IgAY4A1M-1712152547-1.0.1.1-G4qjB2QYQGuhG1n64dn8fpCopHRo6xwtlC.XooMhuO.sxp2.ivHz6aOYl8U2ToBtjZkaEJy1ePm1FoodeWtQXg",
                    "path": "/",
                    "domain": ".tkt.ge",
                }
            ]
        },
        "user_agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

@pytest.fixture
def index_page(page: Page) -> IndexPage:
    return IndexPage(page)

@pytest.fixture
def movies_page(page: Page) -> MoviesPage:
    return MoviesPage(page)

@pytest.fixture
def movie_page(page: Page) -> MoviePage:
    return MoviePage(page)

