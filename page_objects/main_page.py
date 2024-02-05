from page_objects.acadamy_page import AcademyPage
from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_field = (By.XPATH, "//input[@type='search']")
    __logo_button = (By.XPATH, "//*[@class='wp-image-216051 entered lazyloaded']")
    __java_SDET_academy_list_item = (By.XPATH, "//li[@class='et_pb_menu_page_id-218093 menu-item menu-item-type-custom menu-item-object-custom menu-item-218093']")

    def is_main_page_opened(self):
        return self._is_visible(self.__search_field)

    def click_logo(self):
        return self._click(self.__logo_button)

    def click_java_sdet_academy_list_item(self):
        self._click(self.__java_SDET_academy_list_item)
        return AcademyPage(self._driver)


