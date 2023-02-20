from selenium.webdriver.common.by import By


def test_is_main_page_opened(open_main_page):
    main_page = open_main_page
    assert not main_page.is_main_page_opened()



