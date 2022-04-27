
import sys
import time

sys.path.append("C:/Users/Admin/PycharmProjects/PythonFinalTest1POM")

from pageObjects.LoginPage import LoginPage

class TestLoginPage():

    username = "thang49082"
    password = "thang49082"

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def test_func_login(self):
        self.login_page.setUserName(self.username+"a")
        time.sleep(1)
        self.login_page.setPassword(self.password+"a")
        time.sleep(1)
        self.login_page.clickLogin()
        time.sleep(1)
        self.login_page.setUserNamedeletekey()
        time.sleep(1)
        self.login_page.clickLogin()
        time.sleep(1)
        self.login_page.setPassworddeletekey()
        time.sleep(1)
        self.login_page.clickLogin()

    def test_click_register(self):
        self.login_page.clickRegisterPage()
        time.sleep(1)


    def test_click_logout(self):
        self.login_page.clickLogout()
        time.sleep(1)
