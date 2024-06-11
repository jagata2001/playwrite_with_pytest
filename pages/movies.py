from playwright.sync_api import Page


class MoviesPage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def find_movie_and_open(self, movieName: str) -> None:
        movie = self.page.locator(f"//div[@data-testid and @title='{movieName}']")
        movie.click()