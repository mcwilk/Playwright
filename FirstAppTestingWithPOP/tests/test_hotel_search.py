import pytest

from FirstAppTestingWithPOP.pages.search_hotel_page import SearchHotelPage


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    def test_hotel_search(self, setup):
        page = setup

        search_hotel_page = SearchHotelPage(page)
        search_hotel_page.set_city("Dubai")

