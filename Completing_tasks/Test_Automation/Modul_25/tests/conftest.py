# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as chrome_options
# from link import *
#
#
# @pytest.fixture
# def get_chrome_options():
#     """Опции браузера"""
#     options = chrome_options()
#     options.add_argument('chrome')  # Use headless if you do not a browser UI
#     options.add_argument('--start-maximized')
#     options.add_argument('--window-size=1650,900')
#     return options
#
#
# @pytest.fixture
# def get_webdriver(get_chrome_options):
#     """Вебдрайвер"""
#     options = get_chrome_options
#     driver = webdriver.Chrome(executable_path='E:/python_library/chromedriver.exe', options=options)
#     return driver
#
#
# @pytest.fixture(scope='function')
# def setup(request, get_webdriver):
#     driver = get_webdriver
#     url = pet_friends_login
#     if request.cls is not None:
#         request.cls.driver = driver
#     driver.get(url)
#     yield driver
#     driver.quit()
