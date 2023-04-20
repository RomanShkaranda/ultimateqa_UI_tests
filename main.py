import time


def test_is_main_page_opened(open_main_page):
    main_page = open_main_page
    assert not main_page.is_main_page_opened()


def test_click(open_main_page):
    main_page = open_main_page
    main_page.click_java_sdet_academy_list_item()


def test_academy_page(open_academy_page):
    academy_page = open_academy_page
    assert academy_page.is_signup_visible(), 'Signup button is not located'


def test_input_first_name(open_academy_page):
    academy_page = open_academy_page
    academy_page.input_all_data()



