from .pages.base_page import BasePage
from .pages.cart_page import BaseCartPage
from .test_product_page import links
import pytest


@pytest.mark.parametrize('link', links)
class TestGuestCanAddProduct:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, link):
        page = BasePage(browser, link)
        page.open()
        page.go_to_cart()
        page = BaseCartPage(browser, browser.current_url)
        page.should_be_empty_text()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        page = BasePage(browser, link)
        page.open()
        page.go_to_cart()
        page = BaseCartPage(browser, browser.current_url)
        page.should_be_empty()