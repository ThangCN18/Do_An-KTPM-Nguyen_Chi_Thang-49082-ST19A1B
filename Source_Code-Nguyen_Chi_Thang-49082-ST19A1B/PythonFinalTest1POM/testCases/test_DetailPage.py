
import sys
import time

sys.path.append("C:/Users/Admin/PycharmProjects/PythonFinalTest1POM")

from pageObjects.DetailPage import DetailPage

class TestDetailPage():

    valueComment = "Phim Hay quá!!!"

    def __init__(self, driver):
        self.driver = driver
        self.detail_page = DetailPage(driver)

    def test_movie_detail_page(self):
        time.sleep(4)
        self.detail_page.click_stop_movie()
        time.sleep(1)
        self.detail_page.set_value_comment(self.valueComment)
        time.sleep(2)
        self.detail_page.click_comment()
        time.sleep(3)