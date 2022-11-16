from .base_page import BasePage
from .locators import MainPageLocators
from .product_page import CartPage


class MainPage(BasePage):
    def add_to_cart(self):
        add_to_cart_link = self.browser.find_element(*MainPageLocators.ADD_TO_CART_LINK)
        add_to_cart_link.click()
        self.solve_quiz_and_get_code()
        return CartPage(browser=self.browser, url=self.browser.current_url)
