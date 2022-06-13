#   pytest -v --driver Chrome --driver-path E:\python_libr
# ary\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_25\tests//chromedriver.exe

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from link import *


def test_show_all_pets(selenium):
    """Множественный поиск"""
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

    # Ищем наших питомцев (картинка, имя, описание).
    # Явное ожидание.
    images = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    names = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    descriptions = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

    # for i in enumerate(images):
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

    selenium.quit()

# def pets_authorization(selenium):
# Переходим на страницу моих питомцев.
# selenium.get(pet_friends_my_pets)

# Проверяем, что мы точно оказались на странице моих питомцев.
# assert selenium.find_element_by_tag_name('h2').text == "delakroa"
