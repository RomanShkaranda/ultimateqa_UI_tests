from utilities.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AcademyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __get_early_access = (By.XPATH, "//button[@class='formkit-signup']")
    __first_name_field = (By.XPATH, "//input[@name='fields[first_name]']")
    __email_field = (By.XPATH, "//input[@name='email_address']")
    __dropdown_element = (By.XPATH, "//select[@data-parsley-id='6515']")

    def is_early_access_visible(self):
        return self._is_visible(self.__get_early_access)

    def input_first_name(self):
        self._send_keys(self.__first_name_field, 'testtest')
        return self

    def input_email(self):
        self._send_keys(self.__email_field, 'asd@email.com')
        return self


