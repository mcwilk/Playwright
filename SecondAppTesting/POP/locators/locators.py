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
    edit_link_name_xpath = "//header[@class='woocommerce-Address-title title']//a"
    first_name_xpath = "//*[@id='billing_first_name']"
    last_name_xpath = "//*[@id='billing_last_name']"
    country_xpath = "//*[@id='select2-billing_country-container']"
    country_search_xpath = "//input[@class='select2-search__field']"
    address_1_xpath = "//*[@id='billing_address_1']"
    post_code_xpath = "//*[@id='billing_postcode']"
    city_xpath = "//*[@id='billing_city']"
    phone_xpath = "//*[@id='billing_phone']"
    save_address_button_xpath = "//button[@value='Save address']"
    message_xpath = "//div[@class='woocommerce-message']"
