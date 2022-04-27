
import sys
import time

sys.path.append("C:/Users/Admin/PycharmProjects/PythonFinalTest1POM")

from pageObjects.RegisterPage import RegisterPage

class TestRegisterPage():

    email = "thang49082@donga.edu.vn"
    username = "thang49082"
    password = "thang49082"

    def __init__(self, driver):
        self.driver = driver
        self.test_register_page = RegisterPage(driver)

    def test_func_register(self):
        self.test_register_page.setRegisterEmail(self.email)
        self.test_register_page.setRegisterUserName(self.username)
        self.test_register_page.setRegisterPassword(self.password)
        self.test_register_page.clickRegister()