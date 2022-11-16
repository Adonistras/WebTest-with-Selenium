from .base_page import BasePage
from .locators import CartLocators


class BaseCartPage(BasePage):
    def should_be_cart(self):
        self.should_be_empty()
        self.should_be_empty_text()

    def should_be_empty_text(self):
        assert 'Ваша корзина пуста' in self.text_value(*CartLocators.IS_EMPTY_TEXT), 'Cart is not empty'

    def should_be_empty(self):
        assert self.is_not_element_present(*CartLocators.ITEM), 'There are some items in cart'
