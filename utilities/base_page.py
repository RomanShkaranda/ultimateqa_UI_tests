from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 0)

    def __wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _is_visible(self, locator):
        try:
            self.__wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False
