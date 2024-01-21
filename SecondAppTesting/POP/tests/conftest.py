import allure
import pytest


@pytest.fixture()
def setup(request, page):
    before_failed = request.session.testsfailed
    request.cls.page = page

    yield

    if request.session.testsfailed != before_failed:
        allure.attach(page.screenshot(), name="Test failed", attachment_type=allure.attachment_type.PNG)

    page.close()
