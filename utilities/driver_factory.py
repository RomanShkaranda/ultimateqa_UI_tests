from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id):
        if int(driver_id) == DriverFactory.CHROME:
            options = Options()
            # add if you want headless and no sandbox
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif int(driver_id) == DriverFactory.FIREFOX:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        elif int(driver_id) == DriverFactory.EDGE:
            driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver

