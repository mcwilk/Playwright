import logging

from playwright.sync_api import Page

from FirstAppTestingWithPOP.locators.locators import SearchHotelLocators


class SearchHotelPage:

    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def set_city(self, city):
        self.page.get_by_role("link", name=SearchHotelLocators.search_hotel_link_name).click()
        self.page.locator(SearchHotelLocators.search_hotel_input_id).get_by_role("textbox").fill(city)
        self.page.locator(SearchHotelLocators.location_match_span_xpath.replace('city', city)).click()



