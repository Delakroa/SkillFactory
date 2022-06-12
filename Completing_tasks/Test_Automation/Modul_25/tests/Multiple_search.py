#   pytest -v --driver Chrome --driver-path E:\python_libr
# ary\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_25\tests//chromedriver.exe

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DRIVER_PATH = 'E:/python_library/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


# @pytest.fixture(autouse=True)
def test_show_all_pets():
    """Множественный поиск"""
    # Переходим на страницу авторизации.
    driver.get('https://petfriends.skillfactory.ru/login')

    # Вводим email.
    driver.find_element_by_id('email').send_keys('skillfaktory.qap66@gmail.com')

    # Вводим пароль.
    driver.find_element_by_id('pass').send_keys('7370377')

    # Нажимаем на кнопку входа в аккаунт.
    driver.find_element_by_css_selector('button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element_by_tag_name('h1').text == "PetFriends"

    # Переходим на страницу моих питомцев
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    # Проверяем, что мы точно оказались на странице моих питомцев
    assert driver.find_element_by_tag_name('h2').text == "delakroa"

    # Ищем наших питомцев (картинка, имя, описание)
    images = driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = driver.find_elements_by_css_selector('.card-deck .card-img-top')
    descriptions = driver.find_elements_by_css_selector('.card-deck .card-img-top')

    # for i in range(len(names)):  # Старый (неудачный) способ работы с массивами.
    for i in enumerate(names):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

    # print(names)

    driver.quit()


def test_attributes():
    """Пока использовать не будем"""
    images = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    names = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    descriptions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

    pass
