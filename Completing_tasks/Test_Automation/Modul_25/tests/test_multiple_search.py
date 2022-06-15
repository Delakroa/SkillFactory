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
        print('i =', i, 'names[i].text =', name)
        image = images[i].get_attribute('src')
        desc = descriptions[i].text
        assert image != '' \
               and image != 'https://petfriends.skillfactory.ru/static/images/upload2.jpg' \
               and image != '(unknown)', "Нет фото"
        assert name != '', "Нет имени"
        assert desc != '' and desc != 'None, None лет', "Поле порода и возраст - пустое"
        assert ',' in desc, 'Пропущена запятая в поле "порода, возраст"'
        parts = desc.split(",")
        print('parts[1]=', parts[1])
        assert len(parts[0]) > 0 and parts[0] != 'None', "Нет названия породы"
        assert len(parts[1]) > 0 and parts[1] != 'None лет' and parts[1] != ' лет', "Нет возраста"


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
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#navbarNav > ul > li > a"))).click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "delakroa"

    # количество питомцев
    # сохраняем в переменную data_statistic элементы статистики
    data_statistic = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    # Получаем количество питомцев из данных статистики
    statistic = data_statistic[0].text.split('\n')
    statistic = statistic[1].split(' ')
    statistic = int(statistic[1])
    print('statistic= ', statistic)
    assert statistic > 0, "Нет данных Статистика"

    # Проверяем, что количество строк в таблице равно числу, записанному в статистике
    # count_table - количество строк таблицы определим по количеству элементов с атрибутом img
    images = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'IMG')))
    count_table = len(images) - 1
    print('count_table =', count_table)
    assert count_table >= 0, "Таблица 'Мои питомцы' - пустая"
    assert statistic == count_table, \
        'Данные Статистика не совпадают с количеством строк в таблице Мои питомцы'

    # Назначаем переменную для подсчёта количества питомцев пользователя с фотографией
    pytest.driver.implicitly_wait(5)
    photo_presence = 0

    # определяем количество питомцев с фотографией по непустому значению атрибута scr
    for i in range(count_table):
        photo = images[i].get_attribute('src')
        if photo != '' \
                and photo != 'https://petfriends.skillfactory.ru/static/images/upload2.jpg' and photo != '(unknown)':
            photo_presence += 1
        else:
            photo_presence = photo_presence

    print('photo_presence=', photo_presence, ' count_table // 2 =', count_table // 2)

    # Проверяем, что как минимум половина всех питомцев имеют фотографию
    assert photo_presence >= (count_table // 2), 'Недостаточно питомцев с фотографиями'

    # Проверяем, что у питомцев заполнены все данные: имя, тип, возраст
    # Формируем массив со всеми данными питомцев.
    my_list = []
    # Формируем массив только с именами питомцев
    my_names = []

    # постоянная часть в Xpath
    cXpath = '//*[@id="all_my_pets"]/table/tbody/tr['
    for i in range(1, count_table + 1):
        stroka = ''
        pytest.driver.implicitly_wait(5)
        name = pytest.driver.find_element(By.XPATH, cXpath + str(i) + "]/td[1]").text
        assert name != '', 'У питомца отсутствует имя'
        stroka += name
        my_names.append(stroka)
        tip = pytest.driver.find_element(By.XPATH, cXpath + str(i) + "]/td[2]").text
        assert tip != '' and tip != 'None', 'У питомца отсутствует порода'
        stroka += tip
        age = pytest.driver.find_element(By.XPATH, cXpath + str(i) + "]/td[3]").text
        assert age != '' and age != 'None лет' and age != ' лет', 'У питомца отсутствует возраст'
        stroka += age
        my_list.append(stroka)
    print(my_list)
    print(my_names)
    assert my_list != [], 'Массив пустой'
    assert my_names != [], 'Массив имён пустой'

    # Проверяем, что в списке нет повторяющейся информации о питомцах (имя, порода, возраст)
    # Для этого сформируем новый массив из уникальных строк массива my_list.
    # Если длина массива осталась прежней, значит нет повторяющихся строк.
    my_set = set(my_list)
    print('my_set=', my_set, ' len(my_set)=', len(my_set))
    assert len(my_set) == count_table, 'В списке есть повторяющаяся информация о питомцах'

    # Проверяем, что в списке нет повторяющихся имён питомцев
    # Для этого сформируем новый массив из уникальных строк массива my_names.
    # Если длина массива осталась прежней, значит нет повторяющихся имён.
    my_set_names = set(my_names)
    print('my_set_names=', my_set_names, ' len(my_set_names)=', len(my_set_names))
    assert len(my_set_names) == count_table, 'В списке есть повторяющиеся имена питомцев'
