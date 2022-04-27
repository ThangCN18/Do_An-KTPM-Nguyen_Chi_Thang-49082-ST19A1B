from selenium.webdriver import Keys


class LoginPage():

    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_id = "login_submit"
    button_logout_id = "btn_logout"
    button_register_page_id = "btn_register_page"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setUserNamedeletekey(self):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(Keys.END, Keys.BACKSPACE)

    def setPassworddeletekey(self):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(Keys.END, Keys.BACKSPACE)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.button_logout_id).click()

    def clickRegisterPage(self):
        self.driver.find_element_by_id(self.button_register_page_id).click()