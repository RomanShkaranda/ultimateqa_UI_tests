from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_field = (By.XPATH, "//input[@type='search']")

    def is_main_page_opened(self):
        return self._is_visible(self.__search_field)

