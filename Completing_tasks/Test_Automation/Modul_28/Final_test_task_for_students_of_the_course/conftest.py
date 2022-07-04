import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language: ru, en, es, ...(etc.)')


@pytest.fixture(scope='function')
def browser(request):
    user_languages = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_languages})
    print('\nStart chrome browser for test ...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser ...')
    browser.quit()
