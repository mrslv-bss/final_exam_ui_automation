from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.basic import send_keys, click


search_field_loc = (By.XPATH, "//input[@type='search']")
next_page_button_loc = (By.XPATH, "//a[@aria-label='Next page']")
sign_in_button_loc = (By.XPATH, "//a[contains(text(), 'Sign In')]")
items_loc = (By.XPATH, "//li[@class='products__list-item']//h3")
avatar_login_loc = (By.CLASS_NAME, "header__user-avatar")


def search_course(get_driver, text):
    send_keys(get_driver, search_field_loc, text)
    send_keys(get_driver, search_field_loc, Keys.ENTER)


def find_page_elements(get_driver):
    item_text_list = []
    page_elements = get_driver.find_elements(*items_loc)
    for item in page_elements:
        (item_text_list.append(item.text))
    return item_text_list


def check_result_case(get_driver, config_name):
    """
    1. Search Any course
    2. Check searched course in found titles
    """
    search_course(get_driver, config_name)
    elements = find_page_elements(get_driver)
    while len(get_driver.find_elements(*next_page_button_loc)) > 0:
        click(get_driver, next_page_button_loc)
        elements.append(find_page_elements(get_driver))
        for title in elements:
            assert config_name.upper() in title, title
