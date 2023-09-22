from utilities.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class AcademyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __learnmore_button = (By.XPATH, "//button[@id='form-button']")
    __first_name_field = (By.XPATH, "//input[@name='form_submission[name]']")
    __email_field = (By.XPATH, "//input[@name='form_submission[email]']")
    __dropdown_element = (By.XPATH, "//select[@data-parsley-id='6515']")

    def is_signup_visible(self):
        return self._is_visible(self.__learnmore_button)

    def input_first_name(self):
        self._send_keys(self.__first_name_field, 'testtest')
        return self

    def input_email(self):
        self._send_keys(self.__email_field, 'asd@email.com')
        return self
    
    def select_option_by_text(self):
        dropdown_element = self.__dropdown_element
        select = Select(dropdown_element)
        select.select_by_visible_text("Canada")
            

    # to fix
    # def input_all_data(self):
    #     self.input_first_name().input_last_name().input_email().input_phone_number()

