import pytest
from pages.main_page import check_result_case
from pages.registration_page import registration
from testdata.testdata import words_for_search, user_names
from pages.login_page import login
from pages.search_page import non_exist_case
from libs.basic import start


@pytest.mark.parametrize("config_name", words_for_search)
@pytest.mark.parametrize("user_name", user_names)
def test_main(get_driver, config_name, user_name):
    start(get_driver)
    # registration(get_driver, user_name)
    # login(get_driver, user_name)
    check_result_case(get_driver, config_name)


@pytest.mark.parametrize("user_name", user_names)
def test_no_result_case(get_driver, user_name):
    start(get_driver)
    login(get_driver, user_name)
    non_exist_case(get_driver)
