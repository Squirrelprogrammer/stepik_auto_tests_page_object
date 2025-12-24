from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BTN_ADD_TO_BASKET), "Button for adding to basket is not presented"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_button.click()
        self.solve_quiz_and_get_code()

    def add_product_to_basket_without_captcha(self):
        add_button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_button.click()
        self.should_be_button_add_to_basket()
        self.check_message_disappeared()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear as expected"

    def check_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == product_name_in_basket,\
            f"Product name '{product_name}' is no equal product name in basket '{product_name_in_basket}'"

    def check_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, \
            f"Product price '{product_price}' is no equal product name in basket '{product_price_in_basket}'"
