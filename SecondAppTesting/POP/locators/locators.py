class MyAccountLocators:

    my_account_id_xpath = "//*[@id='menu-item-22']"
    username_id_xpath = "//*[@id='username']"
    password_id_xpath = "//*[@id='password']"
    login_button_name = "Log in"
    reg_email_id_xpath = "//*[@id='reg_email']"
    reg_password_id_xpath = "//*[@id='reg_password']"
    logout_link_text = "Logout"
    error_msg_xpath = "//ul[@class='woocommerce-error']//li"


class BillingAddressLocators:

    addresses_link_text = "Addresses"
    edit_link_name = page.locator("header").filter(has_text="Billing address Edit").get_by_role("link").click()  # ?????
    first_name_xpath = "//*[@id='account_first_name']"
    last_name_xpath = "//*[@id='account_last_name']"

