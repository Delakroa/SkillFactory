#   pytest -v --driver Chrome --driver-path E:\python_libr
# ary\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_25\tests//chromedriver.exe
import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from link import *


@pytest.fixture(autouse=True)
def test_show_all_pets(selenium):
    """Множественный поиск"""
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # Неявное ожидание.
    selenium.implicitly_wait(10)
    # Переходим на страницу авторизации.
    selenium.get(pet_friends_login)

    # Вводим email.
    selenium.find_element_by_id('email').send_keys(valid_email)

    # Вводим пароль.
    selenium.find_element_by_id('pass').send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт.
    selenium.find_element_by_css_selector(btn_click).click()

    # Проверяем, что мы оказались на главной странице пользователя.
    assert selenium.find_element_by_tag_name('h1').text == "PetFriends"

    # Переходим на страницу моих питомцев.
    selenium.get(pet_friends_my_pets)

    # Проверяем, что мы точно оказались на странице моих питомцев.
    assert selenium.find_element_by_tag_name('h2').text == "delakroa"

    # Ищем наших питомцев (картинка, имя, описание).
    # Явное ожидание.
    # images = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(card_deck))
    images = selenium.find_elements_by_css_selector(card_deck)
    names = selenium.find_elements_by_css_selector(card_deck)
    descriptions = selenium.find_elements_by_css_selector(card_deck)

    # for i in range(len(names)):  # Старый (неудачный) способ работы с массивами.
    for i in enumerate(names):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

    selenium.quit()

#     names = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
#     descriptions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
