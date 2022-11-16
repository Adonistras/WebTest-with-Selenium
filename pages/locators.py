from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    GOODS_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    REAL_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    ADD_TO_CART_LINK = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    GOODS_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, '#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a > i')


class CartLocators:
    IS_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    ITEM = (By.CSS_SELECTOR, "#basket_formset > div")


class LoginLocators:
    REGISTER_INPUT_LOGIN = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_INPUT_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')
