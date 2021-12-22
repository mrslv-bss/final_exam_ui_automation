from selenium.webdriver.common.by import By
from pages.main_page import search_course

no_results_text_loc = (By.CLASS_NAME, "products__list-no-results")


def non_exist_case(get_driver):
    """
    1. Search non-existing course
    2. Check searched course in found titles
    """
    search_course(get_driver, "NON_EXISTING_COURSE_NAME")
    no_result_element = get_driver.find_elements(*no_results_text_loc)
    assert len(no_result_element)
