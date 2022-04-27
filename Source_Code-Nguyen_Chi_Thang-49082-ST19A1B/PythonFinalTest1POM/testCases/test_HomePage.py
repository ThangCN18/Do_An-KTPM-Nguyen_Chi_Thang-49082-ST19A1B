
import sys
import time

sys.path.append("C:/Users/Admin/PycharmProjects/PythonFinalTest1POM")

from pageObjects.HomePage import HomePage

class TestHomePage():

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        time.sleep(1)

    def test_click_login_page(self):
        self.home_page.click_login_page()
        time.sleep(1)

    def test_click_movies_page(self):
        self.home_page.click_movies_page()
        time.sleep(1)
