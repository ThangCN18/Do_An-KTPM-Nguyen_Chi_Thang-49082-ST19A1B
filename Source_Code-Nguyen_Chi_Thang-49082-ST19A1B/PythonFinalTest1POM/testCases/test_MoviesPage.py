
import sys
import time

sys.path.append("C:/Users/Admin/PycharmProjects/PythonFinalTest1POM")

from pageObjects.MoviesPage import MoviesPage

class TestMoviesPage():
    valueSearch = "Tam sinh tam thế"

    def __init__(self, driver):
        self.driver = driver
        self.test_movies_page = MoviesPage(driver)

    def test_function_search_and_click(self):
        self.test_movies_page.clickGenre2()
        time.sleep(1)
        self.test_movies_page.clickGenre4()
        time.sleep(1)
        self.test_movies_page.clickGenre5()
        time.sleep(1)
        self.test_movies_page.clickGenre3()
        time.sleep(1)
        self.test_movies_page.setValueSearch(self.valueSearch)
        time.sleep(1)
        self.test_movies_page.clickMovieDetailPage()
        time.sleep(1)