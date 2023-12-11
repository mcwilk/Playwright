def test_first_search_element(page):
    input_phrase = "Sample search text"

    # Go to specific WWW address
    page.goto("https://antoogle.testoneo.com/")

    # Find and act on webelements
    page.get_by_placeholder("Search phrase").click()
    page.get_by_placeholder("Search phrase").fill(input_phrase)
    page.get_by_role("button", name="Search!").click()

    assert page.inner_text("#item0") == input_phrase, f'Actual value \"{page.inner_text("#item0")}\" not equals to ' \
                                                      f'expected value: \"{input_phrase}\"'
