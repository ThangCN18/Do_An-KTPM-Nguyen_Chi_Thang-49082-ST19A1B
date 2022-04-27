
class RegisterPage():

    textbox_email_register_xpath = '//*[@id="email"]'
    textbox_username_register_id = "user_name"
    textbox_password_register_id = "_password"
    button_register_id = "btn_register"

    def __init__(self, driver):
        self.driver = driver

    def setRegisterEmail(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_register_xpath).send_keys(email)

    def setRegisterUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_register_id).send_keys(username)

    def setRegisterPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_register_id).send_keys(password)

    def clickRegister(self):
        self.driver.find_element_by_id(self.button_register_id).click()

