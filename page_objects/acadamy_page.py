from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AcademyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __signup_button = (By.XPATH, "//button[@class='formkit-signup']")
    __first_name_field = (By.XPATH, "//input[@name='fields[first_name]']")
    __last_name_field = (By.XPATH, "//input[@name='fields[last_name]']")
    __email_field = (By.XPATH, "//input[@name='email_address']")
    __phone_number_field = (By.XPATH, "//input[@name='fields[phone]']")

    def is_signup_visible(self):
        return self._is_visible(self.__signup_button)

    def input_first_name(self):
        self._send_keys(self.__first_name_field, 'testtest')
        return self

    def input_last_name(self):
        self._send_keys(self.__last_name_field, 'asd')
        return self

    def input_email(self):
        self._send_keys(self.__email_field, 'asd@email.com')
        return self

    def input_phone_number(self):
        self._send_keys(self.__phone_number_field, '1234567890')
        return self

    def input_all_data(self):
        self.input_first_name().input_last_name().input_email().input_phone_number()

