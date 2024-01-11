import allure
import pytest
from playwright.sync_api import Playwright


@pytest.fixture()
def setup(request, playwright: Playwright):
    # Prepare browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # browser = playwright.firefox.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    before_failed = request.session.testsfailed

    # Go to specific WWW address
    page.goto(r"http://www.kurs-selenium.pl/demo/")
    page.set_default_timeout(2000)

    yield page

    if request.session.testsfailed != before_failed:
        allure.attach(page.screenshot(), name="Test failed", attachment_type=allure.attachment_type.PNG)

    context.close()
    browser.close()


# @pytest.fixture()
# def setup(page):
#     page.goto(r"http://www.kurs-selenium.pl/demo/")
#     # page.set_default_timeout(2000)
#
#     yield page
#
#     page.close()
