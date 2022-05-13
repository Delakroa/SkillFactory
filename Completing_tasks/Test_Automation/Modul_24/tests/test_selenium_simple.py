#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_simple.py
#

import time


def test_search_example(selenium):
    """Найдите в гугле какую-нибудь фразу и сделайте скриншот страницы."""

    # Откройте страницу поиска:
    selenium.get('http://google.com')

    time.sleep(10)  # просто для демонстрационных целей, НЕ повторяйте это на реальных проектах!

    # Найдите поле для ввода поискового текста:
    search_input = selenium.find_element_by_id('input')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys('my first selenium test for Web UI!')

    time.sleep(10)  # просто для демонстрационных целей, НЕ повторяйте это на реальных проектах!

    # Нажмите Поиск:
    search_button = selenium.find_element_by_name('btnK')
    search_button.click()

    time.sleep(10)  # просто для демонстрационных целей, НЕ повторяйте это на реальных проектах!

    # Сделать скриншот окон браузера:
    selenium.save_screenshot('result.png')
