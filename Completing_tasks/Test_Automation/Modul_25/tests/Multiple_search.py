#   pytest -v --driver Chrome --driver-path E:\python_libr
# ary\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_25\tests//chromedriver.exe

import pytest
import time
from selenium import webdriver  # подключение библиотеки

driver = webdriver.Chrome()  # получение объекта веб-драйвера для нужного браузера
driver.get('https://petfriends.skillfactory.ru/new_user')

driver.find_element_by_id('name')
driver.find_element_by_name('name')
driver.find_element_by_class_name('btn')
driver.find_element_by_tag_name('input')
driver.find_element_by_css_selector('input.form-control')
driver.find_element_by_link_text('У меня уже есть аккаунт')
driver.find_element_by_xpath('//input[@id="name"]')


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('skillfaktory.qap66@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('7370377')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
