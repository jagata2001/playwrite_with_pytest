from playwright.sync_api import Page

from index import IndexPage
from movies import MoviesPage
from movie import MoviePage

movie_name = "გოძილა x კონგი: ახალი იმპერია"

def test_get_available_cinema_list(page: Page, index_page: IndexPage, movies_page: MoviesPage, movie_page: MoviePage) -> None:    
    index_page.load()
    index_page.click_on_movie_icon()
    movies_page.find_movie_and_open(movie_name)
    movie_page.wait_to_load()
    cinema_list = movie_page.get_available_cinema_list()
    print(cinema_list)


def test_get_available_min_price_and_time(page: Page, index_page: IndexPage, movies_page: MoviesPage, movie_page: MoviePage) -> None:    
    index_page.load()
    index_page.click_on_movie_icon()
    movies_page.find_movie_and_open(movie_name)
    movie_page.wait_to_load()
    best_choice = movie_page.get_min_price_and_time_available()
    print(best_choice)


