import pytest
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .test_product_page import links


@pytest.mark.parametrize('link', links)
@pytest.mark.user_guest
class TestGuestSomeTestes:
    def test_guest_should_see_login_link(self, browser, link):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    """Подход с реализацией PageObject"""
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()