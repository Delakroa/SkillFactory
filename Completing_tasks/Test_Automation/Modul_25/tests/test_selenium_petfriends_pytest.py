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

#   pytest -v --driver Chrome --driver-path E:\python_libr
# ary\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_25\tests//chromedriver.exe


import time


def test_pet_friends(selenium):
    """ Найдите в гугле какую-нибудь фразу и сделайте скриншот страницы. """

    # Открыть базовую страницу PetFriends:
    selenium.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # просто для демонстрационных целей, НЕ повторяйте это на реальных проектах!

    # Найдите поле для ввода поискового текста:
    btn_new_user = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_new_user.click()

    btn_exist_acc = selenium.find_element_by_link_text("У меня уже есть аккаунт")
    btn_exist_acc.click()

    field_email = selenium.find_element_by_id("email")
    field_email.click()
    field_email.clear()
    field_email.send_keys("skillfaktory.qap66@gmail.com")

    field_pass = selenium.find_element_by_id("pass")
    field_pass.click()
    field_pass.clear()
    field_pass.send_keys("7370377")

    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    time.sleep(5)  # просто для демонстрационных целей, НЕ повторяйте это на реальных проектах!

    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Сделать скриншот окна браузера:
        selenium.save_screenshot('result_pet_friends.png')
    else:
        raise Exception("login error")

