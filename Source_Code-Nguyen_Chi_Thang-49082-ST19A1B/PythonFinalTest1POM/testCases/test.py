import time
import unittest
import HtmlTestRunner
from selenium import webdriver

import sys


sys.path.append("C:/Users/Admin/PycharmProjects/PythonFinalTest1POM")
from testCases.test_HomePage import TestHomePage
from testCases.test_LoginPage import TestLoginPage
from testCases.test_MoviesPage import TestMoviesPage
from testCases.test_DetailPage import TestDetailPage
from testCases.test_RegisterPage import TestRegisterPage

class MovieTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\PythonFinalTest1POM\\drivers\\chromedriver.exe")
    baseURL = "http://localhost:3000"

    test_home_page = TestHomePage(driver)
    test_login_page = TestLoginPage(driver)
    test_movies_page = TestMoviesPage(driver)
    test_register_page = TestRegisterPage(driver)
    test_detail_page = TestDetailPage(driver)
    driver.get(baseURL)
    driver.maximize_window()

    def test_movie_play(self):
        self.test_home_page.test_click_login_page()
        time.sleep(2)
        self.test_login_page.test_click_register()
        time.sleep(2)
        self.test_register_page.test_func_register()
        time.sleep(2)
        self.test_login_page.test_func_login()
        time.sleep(2)
        self.test_home_page.test_click_movies_page()
        time.sleep(2)
        self.test_movies_page.test_function_search_and_click()
        time.sleep(2)
        self.test_detail_page.test_movie_detail_page()
        time.sleep(2)
        self.test_login_page.test_click_logout()
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))