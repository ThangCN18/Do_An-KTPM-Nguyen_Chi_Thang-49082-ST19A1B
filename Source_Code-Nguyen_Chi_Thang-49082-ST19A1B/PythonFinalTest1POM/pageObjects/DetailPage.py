class DetailPage():

    button_stop_movie_xpath = "//*[@id='root']/div/div/div[1]/div/video"
    textbox_comment_xpath = "//*[@id='root']/div/div/div[2]/form/input"
    btn_comment_xpath = "//*[@id='root']/div/div/div[2]/form/button"

    def __init__(self, driver):
        self.driver = driver

    def click_stop_movie(self):
        self.driver.find_element_by_xpath(self.button_stop_movie_xpath).click()

    def set_value_comment(self, valueComment):
        self.driver.find_element_by_xpath(self.textbox_comment_xpath).send_keys(valueComment)

    def click_comment(self):
        self.driver.find_element_by_xpath(self.btn_comment_xpath).click()