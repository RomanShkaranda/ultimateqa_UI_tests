from selenium import webdriver
import pytest


@pytest.fixture
def create_driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get("https://ultimateqa.com/")
    yield chrome_driver
    chrome_driver.quit()


