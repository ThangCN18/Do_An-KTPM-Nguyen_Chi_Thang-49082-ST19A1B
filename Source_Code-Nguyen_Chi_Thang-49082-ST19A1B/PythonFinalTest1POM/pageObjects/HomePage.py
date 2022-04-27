class HomePage():

    button_login_page_id = "login_page"
    button_movies_page_xpath = "//*[@id='navbarText']/ul/li[2]/a"

    def __init__(self, driver):
        self.driver = driver

    def click_login_page(self):
        self.driver.find_element_by_id(self.button_login_page_id).click()

    def click_movies_page(self):
        self.driver.find_element_by_xpath(self.button_movies_page_xpath).click()