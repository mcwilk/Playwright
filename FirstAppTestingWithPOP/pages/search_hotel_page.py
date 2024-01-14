import logging

import allure
from playwright.sync_api import Page

from FirstAppTestingWithPOP.locators.locators import SearchHotelLocators


class SearchHotelPage:

    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    @allure.step("Setting city name to '{1}'")
    def set_city(self, city):
        self.logger.info(f"Setting city {city}")
        self.page.get_by_role("link", name=SearchHotelLocators.search_hotel_link_name).click()
        self.page.locator(SearchHotelLocators.search_hotel_input_id).get_by_role("textbox").fill(city)
        self.page.locator(SearchHotelLocators.location_match_span_xpath.replace('city', city)).click()
        allure.attach(self.page.screenshot(), name="set_city", attachment_type=allure.attachment_type.PNG)

    @allure.step("Setting date range from '{1}' to '{2}'")
    def set_date_range(self, check_in, check_out):
        self.logger.info(f"Setting check in {check_in} and check out {check_out} dates")
        self.page.get_by_role("textbox", name=SearchHotelLocators.check_in_placeholder).fill(check_in)
        self.page.get_by_role("textbox", name=SearchHotelLocators.check_out_placeholder).fill(check_out)
        allure.attach(
            self.page.screenshot(), name="set_date_range", attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Setting travellers: adults '{1}' and children '{2}'")
    def set_travellers(self, adults, children):
        self.logger.info(f"Setting travellers: {adults} adults and {children} children")
        self.page.locator(SearchHotelLocators.travellers_input_id).click()
        # self.page.locator(SearchHotelLocators.adult_input_id).fill("")  # NOT NEEDED in Playwright
        self.page.locator(SearchHotelLocators.adult_input_id).fill(adults)
        # self.page.locator(SearchHotelLocators.child_input_id).fill("")  # NOT NEEDED in Playwright
        self.page.locator(SearchHotelLocators.child_input_id).fill(children)
        allure.attach(
            self.page.screenshot(), name="set_travellers", attachment_type=allure.attachment_type.PNG
        )

    def perform_search(self):
        self.logger.info("Performing search...")
        self.page.get_by_role("button", name=SearchHotelLocators.search_button_name).click()


