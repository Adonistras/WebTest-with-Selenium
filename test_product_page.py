from .pages.login_page import LoginPage
from .pages.product_page import CartPage
from .pages.main_page import MainPage
import pytest

links = [

      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
       pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                   marks=pytest.mark.xfail(reason='some_bug')),
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


@pytest.mark.skip
@pytest.mark.parametrize('link', links)
class TestWithImpossibleBugs:
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = MainPage(self, browser, link)
        page.open()
        page = page.add_to_cart()
        page.should_be_cart_page()


    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = MainPage(self, browser, link)
        page.open()
        page = page.add_to_cart()
        page.should_not_be_success_message()


    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = MainPage(browser, link)
        page.open()
        page = page.add_to_cart()
        page.should_disappear()


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email='adonistras@mail.ru', password='filippos3dg')
        page.should_be_authorized_user()
        yield

    @pytest.mark.parametrize('link', links)
    def test_user_can_add_product_to_basket(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page = page.add_to_cart()
        page.should_be_cart_page()

    @pytest.mark.parametrize('link', links)
    def test_user_cant_see_success_message(self, browser, link):
        page = CartPage(browser, link)
        page.open()
        page.should_not_be_success_message()
