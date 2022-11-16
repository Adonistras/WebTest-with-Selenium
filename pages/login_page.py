from .base_page import BasePage
from .locators import MainPageLocators, LoginLocators
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in WebDriver.current_url, "Login url is not presented"

    def should_be_login_form(self):
        self.is_element_present(*MainPageLocators.LOGIN_FORM)
        assert True, "Login form is not presented"

    def should_be_register_form(self):
        self.is_element_present(*MainPageLocators.REGISTER_FORM)
        assert True, "Register form is not presented"

    def register_new_user(self, email, password):
        self.input(*LoginLocators.REGISTER_INPUT_LOGIN, email)
        self.input(*LoginLocators.REGISTER_INPUT_PASSWORD, password)
        self.input(*LoginLocators.REGISTER_INPUT_PASSWORD2, password)
        self.browser.find_element(*LoginLocators.REGISTER_BUTTON).click()


