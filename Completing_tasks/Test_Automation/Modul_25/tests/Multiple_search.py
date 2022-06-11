#   pytest -v --driver Chrome --driver-path E:\python_libr
# ary\SkillFaktory\SkillFactory_practice\Completing_tasks\Test_Automation\Modul_25\tests//chromedriver.exe
import pytest
from selenium import webdriver  # подключение библиотеки
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver_path = 'E:/python_library/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)


@pytest.fixture(autouse=True)
def testing():
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield

    driver.quit()


def test_show_all_pets():
    # Вводим email
    driver.find_element_by_id('email').send_keys('skillfaktory.qap66@gmail.com')
    # Вводим пароль
    driver.find_element_by_id('pass').send_keys('7370377')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_attributes():
    driver.get('https://petfriends.skillfactory.ru')
    images = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    names = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    descriptions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

