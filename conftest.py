from selenium import webdriver
import pytest

from page_objects.main_page import MainPage
from utilities.driver_factory import DriverFactory


@pytest.fixture
def create_driver():
    chrome_driver = DriverFactory.create_driver(1)
    chrome_driver.maximize_window()
    chrome_driver.get("https://ultimateqa.com/")
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def open_main_page(create_driver):
    return MainPage(create_driver)


