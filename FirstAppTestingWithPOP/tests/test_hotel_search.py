import allure
import pytest

from FirstAppTestingWithPOP.pages.search_hotel_page import SearchHotelPage
from FirstAppTestingWithPOP.pages.search_results_page import SearchResultsPage


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("Test method: test_hotel_search")
    @allure.description("Test checking if 'search' option works as expected")
    def test_hotel_search(self, setup):
        page = setup

        search_hotel_page = SearchHotelPage(page)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("09/09/2019", "09/13/2019")
        search_hotel_page.set_travellers("4", "3")
        search_hotel_page.perform_search()

        result_page = SearchResultsPage(page)
        hotel_names = result_page.get_hotel_names()
        hotel_prices = result_page.get_hotel_prices()

        # Asserts
        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        assert hotel_prices[0] == "€20.24"
        assert hotel_prices[1] == "€46"
        assert hotel_prices[2] == "€73.60"
        assert hotel_prices[3] == "€138"

        assert hotel_prices == ["€20.24", "€46", "€73.60", "€138"]
