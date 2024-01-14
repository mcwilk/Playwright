import logging

from playwright.sync_api import Page

from FirstAppTestingWithPOP.locators.locators import SearchResultLocators


class SearchResultsPage:

    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def get_hotel_names(self):
        hotels = self.page.locator(SearchResultLocators.hotel_names_xpath)
        hotel_names = [hotels.nth(num).text_content() for num in range(hotels.count())]

        self.logger.info("Available hotels are:")
        for name in hotel_names:
            self.logger.info(name)

        return hotel_names

    def get_hotel_prices(self):
        prices = self.page.locator(SearchResultLocators.hotel_prices_xpath)
        hotel_prices = [prices.nth(num).text_content() for num in range(prices.count())]

        self.logger.info("Hotel prices are:")
        for price in hotel_prices:
            self.logger.info(price)

        return hotel_prices