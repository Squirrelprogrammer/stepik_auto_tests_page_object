from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, 'login_form')
    REGISTER_FORM = (By.CLASS_NAME, 'register_form')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'add-to-basket')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = ('css selector', 'p.price_color')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
