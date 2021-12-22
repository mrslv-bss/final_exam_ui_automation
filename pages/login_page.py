from libs.basic import send_keys, click
from pages.main_page import sign_in_button_loc, avatar_login_loc
from selenium.webdriver.common.by import By
import json

login_email_loc = (By.ID, "user[email]")
login_password_loc = (By.ID, "user[password]")
login_remember_checkbox_loc = (By.ID, "user[remember_me]")
login_sign_in_button_loc = (By.XPATH, "//input[@value='Sign in']")
login_error_alert_loc = (By.XPATH, "//li[contains(text(), 'Invalid email or password.')]")
login_successful_loc = (By.XPATH, "//p[@class='message-text']")


def login(get_driver, user):
    click(get_driver, sign_in_button_loc)
    with open('cred.json') as f:
        credentials = json.load(f)
    send_keys(get_driver, login_email_loc, credentials[user]['email'])
    send_keys(get_driver, login_password_loc, credentials[user]['password'])
    if credentials[user]['remember']:
        click(get_driver, login_remember_checkbox_loc)
    click(get_driver, login_sign_in_button_loc)
    alert_check = get_driver.find_elements(*login_error_alert_loc)
    assert len(alert_check) == 0, "Invalid email or password"
    login_status_check = get_driver.find_elements(*avatar_login_loc)
    assert len(login_status_check), "Unsuccessful login"
