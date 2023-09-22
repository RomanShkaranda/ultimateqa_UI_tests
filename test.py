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
    academy_page.input_first_name()
    time.sleep(5)

def test_input_email(open_academy_page):
    academy_page = open_academy_page
    academy_page.input_email()
    time.sleep(5)

def test_dropdown_select(open_academy_page):
    open_academy_page = open_academy_page
    open_academy_page.select_option_by_text()
    



