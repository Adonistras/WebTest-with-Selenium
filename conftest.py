from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(executable_path='../../chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()


"""Запуск без окна"""
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path='../../chromedriver.exe', options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
