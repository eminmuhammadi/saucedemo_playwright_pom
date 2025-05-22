from data.constants import *
from data.locators import *


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input_locator = page.locator(LOCATORS_AUTH_USERNAME)
        self.password_input_locator = page.locator(LOCATORS_AUTH_PASSWORD)
        self.login_button_locator = page.locator(LOCATORS_AUTH_LOGIN_BTN)
        self.error_message_locator = page.locator(LOCATORS_AUTH_ERROR_MESSAGE)

    def goto(self):
        self.page.goto(CONSTANTS_START_URL)

    def login(self, username, password):
        self.username_input_locator.fill(username)
        self.password_input_locator.fill(password)
        self.login_button_locator.click()
        self.page.wait_for_load_state('load')
    
    def check_error_message_exists(self):
        count = self.error_message_locator.count()
        if count > 0:
            return True
        return False

