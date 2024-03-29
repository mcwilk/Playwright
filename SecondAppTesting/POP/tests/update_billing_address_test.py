import os
import random

import pytest

from SecondAppTesting.POP.pages.billig_address_page import BillingAddressPage
from SecondAppTesting.POP.pages.my_account_page import MyAccountPage


PASSWORD = os.environ['PASSWORD']


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        suffix = str(random.randint(1, 10000))
        my_account_page = MyAccountPage(self.page)
        billing_address_page = BillingAddressPage(self.page)

        my_account_page.open_page()
        my_account_page.create_account(f"autotester{suffix}@gmail.com", PASSWORD)

        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("Andreas", "Doe")
        billing_address_page.select_country("Portugal")
        billing_address_page.set_address("Street 12", "1000-205", "Lisbon")
        billing_address_page.set_phone_number("111222333")
        billing_address_page.save_address()

        assert billing_address_page.get_message_text() == "Address changed successfully."
