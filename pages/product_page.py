from .base_page import BasePage
from .locators import MainPageLocators


class CartPage(BasePage):
    def should_be_cart_page(self):
        self.should_be_message()
        self.should_be_price()

    def should_be_message(self):
        text = self.text_value(*MainPageLocators.CART_MESSAGE)
        goods_name = self.text_value(*MainPageLocators.GOODS_NAME)
        assert text == goods_name, "Cart after adding not presented or good_names don't match"

    def should_be_price(self):
        price = self.text_value(*MainPageLocators.GOODS_PRICE)
        real_price = self.text_value(*MainPageLocators.REAL_PRICE)
        assert price == real_price, "Prices are not matching"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.CART_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*MainPageLocators.CART_MESSAGE), \
            "Success message is presented, and should disappear"



