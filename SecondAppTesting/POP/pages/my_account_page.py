import logging

from playwright.sync_api import Page

from SecondAppTesting.POP.locators.locators import MyAccountLocators


class MyAccountPage:

    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)
        # locators
        self.username_input = MyAccountLocators.username_id_xpath
        self.password_input = MyAccountLocators.password_id_xpath
        self.login_button = MyAccountLocators.login_button_name
        self.reg_email_input = MyAccountLocators.reg_email_id_xpath
        self.reg_password_input = MyAccountLocators.reg_password_id_xpath
        self.logout_link = MyAccountLocators.logout_link_text
        self.error_msg = MyAccountLocators.error_msg_xpath

    def open_page(self):
        self.page.goto("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        self.page.locator(self.username_input).fill(username)
        self.page.locator(self.password_input).fill(password)
        self.page.get_by_text(self.login_button, exact=True).click()

    def create_account(self, email, password):
        self.page.locator(self.reg_email_input).fill(email)
        self.page.locator(self.reg_password_input).fill(password)
        self.page.keyboard.press("Enter")

    def is_logout_link_displayed(self):
        self.page.get_by_text(self.logout_link, exact=True).wait_for(timeout=1000)
        return self.page.get_by_text(self.logout_link, exact=True).is_visible()

    def get_error_msg(self):
        return self.page.locator(self.error_msg).text_content()
