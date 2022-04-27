class MoviesPage():

    textbox_search_id = "text_search_id"
    button_genre_xpath_3 = "//*[@id='root']/div/div/div[2]/div[3]"
    button_genre_xpath_2 = "//*[@id='root']/div/div/div[2]/div[2]"
    button_genre_xpath_4 = "//*[@id='root']/div/div/div[2]/div[4]"
    button_genre_xpath_5 = "//*[@id='root']/div/div/div[2]/div[5]"
    button_movie_detail_page_xpath = "//*[@id='root']/div/div/div[3]/div/div/a/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def setValueSearch(self, valueSearch):
        self.driver.find_element_by_id(self.textbox_search_id).send_keys(valueSearch)

    def clickGenre2(self):
        self.driver.find_element_by_xpath(self.button_genre_xpath_2).click()

    def clickGenre3(self):
        self.driver.find_element_by_xpath(self.button_genre_xpath_3).click()

    def clickGenre4(self):
        self.driver.find_element_by_xpath(self.button_genre_xpath_4).click()

    def clickGenre5(self):
        self.driver.find_element_by_xpath(self.button_genre_xpath_5).click()

    def clickMovieDetailPage(self):
        self.driver.find_element_by_xpath(self.button_movie_detail_page_xpath).click()