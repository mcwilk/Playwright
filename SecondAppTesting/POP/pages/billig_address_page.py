import logging

from playwright.sync_api import Page

from SecondAppTesting.POP.locators.locators import BillingAddressLocators


class BillingAddressPage:

    def __init__(self, page: Page):
        self.page = page
        # locators
        self.first_name_input = BillingAddressLocators.first_name_xpath
        self.last_name_input = BillingAddressLocators.last_name_xpath
        self.addresses_link = BillingAddressLocators.addresses_link_text
        self.edit_link = BillingAddressLocators.edit_link_name_xpath
        self.country_select = BillingAddressLocators.country_xpath
        self.country_search = BillingAddressLocators.country_search_xpath
        self.address_input = BillingAddressLocators.address_1_xpath
        self.post_code_input = BillingAddressLocators.post_code_xpath
        self.city_input = BillingAddressLocators.city_xpath
        self.phone_input = BillingAddressLocators.phone_xpath
        self.save_address_button = BillingAddressLocators.save_address_button_xpath
        self.msg_div = BillingAddressLocators.message_xpath

    def open_edit_billing_address(self):
        self.page.get_by_text(self.addresses_link, exact=True).click()
        self.page.locator(self.edit_link).first.click()

    def set_personal_data(self, f_name, l_name):
        self.page.locator(self.first_name_input).fill(f_name)
        self.page.locator(self.last_name_input).fill(l_name)

    def select_country(self, country):
        self.page.locator(self.country_select).click()
        # self.page.pause()
        self.page.locator(self.country_search).fill(country)
        self.page.keyboard.press("Enter")

    def set_address(self, street, postcode, city):
        self.page.locator(self.address_input).fill(street)
        self.page.locator(self.post_code_input).fill(postcode)
        self.page.locator(self.city_input).fill(city)

    def set_phone_number(self, number):
        self.page.locator(self.phone_input).fill(number)

    def save_address(self):
        self.page.locator(self.save_address_button).click()

    def get_message_text(self):
        return self.page.locator(self.msg_div).text_content().strip()
