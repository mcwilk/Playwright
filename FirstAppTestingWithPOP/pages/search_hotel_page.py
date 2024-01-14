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

    def set_date_range(self, check_in, check_out):
        self.page.get_by_role("textbox", name=SearchHotelLocators.check_in_placeholder).fill(check_in)
        self.page.get_by_role("textbox", name=SearchHotelLocators.check_out_placeholder).fill(check_out)

    def set_travellers(self, adults, children):
        self.page.locator(SearchHotelLocators.travellers_input_id).click()
        # self.page.locator(SearchHotelLocators.adult_input_id).fill("")
        self.page.locator(SearchHotelLocators.adult_input_id).fill(adults)
        # self.page.locator(SearchHotelLocators.child_input_id).fill("")
        self.page.locator(SearchHotelLocators.child_input_id).fill(children)

    def perform_search(self):
        self.page.get_by_role("button", name=SearchHotelLocators.search_button_name).click()


