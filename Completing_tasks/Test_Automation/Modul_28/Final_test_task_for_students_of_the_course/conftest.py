import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language: ru, en, es, ...(etc.)')


@pytest.fixture(scope='function')
def browser(request):
    user_languages = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.принимать языки': user_languages})
    print('\nЗапустите браузер Chrome для теста ...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nвыйти из браузера ...')
    browser.quit()
