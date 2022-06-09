#!/usr/bin/python3
# -*- encoding=utf8 -*-

# Вы можете найти очень простой пример использования Selenium с PyTest в этом файле.
#
# Дополнительная информация о pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# Как запустить:
#  1) Загрузите драйвер google для Chrome здесь:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Установить все требования:
#     pip install -r requirements.txt
#  3) Запустить тесты:
#     python3 -m pytest -v --driver Chrome --driver-path
#     E:\python_library\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_24\tests
#     \chromedriver.exe test_selenium_simple.py


import time


def test_search_example(selenium):
    """Найдите в гугле какую-нибудь фразу и сделайте скриншот страницы."""

    # Откройте страницу поиска:
    selenium.get('https://www.google.ru/')

    time.sleep(5)  # просто для демонстрационных целей, НЕ повторяйте это на реальных проектах!

    # Найдите поле для ввода поискового текста:
    search_input = selenium.find_element_by_xpath('//input[@class="gLFyf gsfi"]')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys('my first selenium test for Web UI!')

    time.sleep(5)  # просто для демонстрационных целей, НЕ повторяйте это на реальных проектах!

    # Нажмите Поиск:
    search_button = selenium.find_element_by_class_name('gNO89b')
    search_button.click()

    time.sleep(5)  # просто для демонстрационных целей, НЕ повторяйте это на реальных проектах!

    # # Сделать скриншот окон браузера:
    selenium.save_screenshot('result.png')
