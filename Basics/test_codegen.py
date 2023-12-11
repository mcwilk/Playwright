from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    input_phrase = "Sample search text"
    # Prepare browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Debugging
    # page.pause()

    # Go to specific WWW address
    page.goto("https://antoogle.testoneo.com/")


    # Find and act on webelements
    page.get_by_placeholder("Search phrase").click()
    page.get_by_placeholder("Search phrase").fill(input_phrase)
    page.get_by_role("button", name="Search!").click()

    assert page.inner_text("#item0") == input_phrase, f'Actual value \"{page.inner_text("#item0")}\" not equals to ' \
                                                      f'expected value: \"{input_phrase}\"'

    # expect(page.get_by_role("button", name="Search!")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
