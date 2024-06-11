from playwright.sync_api import Page


class IndexPage:
    URL = 'https://tkt.ge'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.movie_buttons = page.locator("a[href='/movies']")

    def load(self) -> None:
        self.page.goto(self.URL)


    def click_on_movie_icon(self) -> None:
        self.movie_buttons.nth(0).click()