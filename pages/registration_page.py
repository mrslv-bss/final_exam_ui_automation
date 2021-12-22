from selenium.webdriver.common.by import By
from libs.basic import click, send_keys
from testdata.testdata import first_name, last_name
from pages.main_page import sign_in_button_loc, avatar_login_loc
import json


create_account_button_loc = (By.XPATH, "//a[contains(text(), 'Create a new account')]")
register_first_name_loc = (By.ID, "user[first_name]")
register_last_name_loc = (By.ID, "user[last_name]")
register_email_loc = (By.ID, "user[email]")
register_password_loc = (By.ID, "user[password]")
register_terms_checkbox_loc = (By.ID, "user[terms]")
register_sign_up_button_loc = (By.XPATH, "//input[@value='Sign up']")
register_email_error_alert_loc = (By.XPATH, "//li[contains(text(), 'Email has already been taken')]")
register_email_error_alert_second__loc = (By.XPATH, "//li[contains(text(), 'Email is invalid')]")


def registration(get_driver, user):
    click(get_driver, sign_in_button_loc)
    click(get_driver, create_account_button_loc)
    with open('cred.json') as f:
        credentials = json.load(f)
    send_keys(get_driver, register_first_name_loc, first_name)
    send_keys(get_driver, register_last_name_loc, last_name)
    send_keys(get_driver, register_email_loc, credentials[user]['email'])
    send_keys(get_driver, register_password_loc, credentials[user]['password'])
    click(get_driver, register_terms_checkbox_loc)
    click(get_driver, register_sign_up_button_loc)
    alert_check = get_driver.find_elements(*register_email_error_alert_loc)
    assert len(alert_check) == 0, "Already taken"
    alert_check = get_driver.find_elements(*register_email_error_alert_second__loc)
    assert len(alert_check) == 0, "Invalid email"
    login_status_check = get_driver.find_elements(*avatar_login_loc)
    assert len(login_status_check), "Unsuccessful register"
