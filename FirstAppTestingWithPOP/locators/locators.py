class SearchHotelLocators:

    search_hotel_link_name = "Search by Hotel or City Name"
    search_hotel_input_id = "#select2-drop"
    location_match_span_xpath = "//span[text()='city']"
    check_in_placeholder = "Check in"
    check_out_placeholder = "Check out"
    travellers_input_id = "#travellersInput"
    adult_input_id = "#adultInput"
    child_input_id = "#childInput"
    search_button_name = " Search"


class SearchResultLocators:

    hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
    hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"
