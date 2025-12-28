from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs a.btn.btn-default')
    BASKET_LINK_INVALID = (By.CLASS_NAME, 'invalid_class_name')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, 'login_form')
    REGISTER_FORM = (By.CLASS_NAME, 'register_form')
    EMAIL_FIELD = (By.NAME, 'registration-email')
    PASSWORD1_FIELD = (By.NAME, 'registration-password1')
    PASSWORD2_FIELD = (By.NAME, 'registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'add-to-basket')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = ('css selector', 'p.price_color')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.ID, 'basket_formset')
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p')
