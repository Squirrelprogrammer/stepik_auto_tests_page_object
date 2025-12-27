from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Products are presented, but should not be"

    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Message 'Your basket is empty' is not presented, but should be"
