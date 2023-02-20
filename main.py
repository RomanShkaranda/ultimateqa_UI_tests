from selenium.webdriver.common.by import By


def test_first_test(create_driver):
    element = create_driver.find_element(By.XPATH, "//input[@type='search']")
    assert element.is_displayed() is False


