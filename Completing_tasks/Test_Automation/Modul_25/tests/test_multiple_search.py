#   pytest -v --driver Chrome --driver-path E:\python_libr
# ary\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_25\tests//chromedriver.exe

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from link import *


@pytest.fixture(autouse=True)
def testing():
    """Хром драйвер"""
    pytest.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # Неявное ожидание
    pytest.driver.implicitly_wait(5)
    # Переходим на страницу авторизации
    pytest.driver.get(pet_friends_login)

    yield

    pytest.driver.quit()


def test_all_pets():
    # Авторизация на сайте.
    # Вводим email
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, btn_click).click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, all_card_deck_image)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, all_card_deck_names)
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, all_card_deck_descriptions)

    for i in range(len(names)):
        name = names[i].text
        image = images[i].get_attribute('src')
        desc = descriptions[i].text
        assert image != '' and image != '(unknown)'
        assert name != '', "Нет имени"
        assert desc != '' and desc != 'None, None лет'
        assert ',' in desc
        parts = desc.split(",")
        assert len(parts[0]) > 0 and parts[0] != 'None'
        assert len(parts[1]) > 0 and parts[1] != 'None лет' and parts[1] != ' лет'


def test_my_pets():
    wait = WebDriverWait(pytest.driver, 5)
    # Авторизация на сайте.
    # Вводим email
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(valid_email)

    # Вводим пароль
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, btn_click))).click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Заходим на страницу своих питомцев
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, my_pets))).click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "delakroa"

    # количество питомцев
    # сохраняем в переменную data_stats элементы статистики
    data_stats = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, profile_statistics)))

    # Получаем количество питомцев из данных статистики
    statistic = data_stats[0].text.split('\n')
    statistic = statistic[1].split(' ')
    statistic = int(statistic[1])
    assert statistic > 0

    # Проверяем, что количество строк в таблице равно числу, записанному в статистике
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'IMG')))
    count_table = len(images) - 1
    assert count_table >= 0
    assert statistic == count_table

    # Назначаем переменную для подсчёта количества питомцев пользователя с фотографией
    pytest.driver.implicitly_wait(5)
    photo_presence = 0

    # определяем количество питомцев с фотографией по непустому значению атрибута scr
    for i in range(count_table):
        photo = images[i].get_attribute('src')
        if photo != '' and photo != '(unknown)':
            photo_presence += 1
        else:
            photo_presence = photo_presence

    # Проверяем, что как минимум половина всех питомцев имеют фотографию
    assert photo_presence >= (count_table // 2)

    # Проверяем, что у питомцев заполнены все данные: имя, тип, возраст
    my_list = []
    my_names = []

    # постоянная часть в Xpath
    xxpath = '//*[@id="all_my_pets"]/table/tbody/tr['
    for i in range(1, count_table + 1):
        line = ''
        pytest.driver.implicitly_wait(5)
        name = pytest.driver.find_element(By.XPATH, xxpath + str(i) + "]/td[1]").text
        assert name != '', 'У питомца отсутствует имя'
        line += name
        my_names.append(line)
        tip = pytest.driver.find_element(By.XPATH, xxpath + str(i) + "]/td[2]").text
        assert tip != '' and tip != 'None', 'У питомца отсутствует порода'
        line += tip
        age = pytest.driver.find_element(By.XPATH, xxpath + str(i) + "]/td[3]").text
        assert age != '' and age != 'None лет' and age != ' лет', 'У питомца отсутствует возраст'
        line += age
        my_list.append(line)
    assert my_list != [], 'Массив пустой'
    assert my_names != [], 'Массив имён пустой'

    # Проверяем, что в списке нет повторяющейся информации о питомцах (имя, порода, возраст)
    my_set = set(my_list)
    assert len(my_set) == count_table

    # Проверяем, что в списке нет повторяющихся имён питомцев
    my_set_names = set(my_names)
    assert len(my_set_names) == count_table
