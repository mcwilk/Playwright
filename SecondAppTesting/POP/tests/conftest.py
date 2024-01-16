import allure
import pytest


@pytest.fixture()
def setup(request, page):
    before_failed = request.session.testsfailed

    # Go to specific WWW address
    page.goto("http://seleniumdemo.com/?page_id=7")
    page.set_default_timeout(2000)

    yield page

    if request.session.testsfailed != before_failed:
        allure.attach(page.screenshot(), name="Test failed", attachment_type=allure.attachment_type.PNG)

    page.close()
