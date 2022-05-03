import pytest
import requests
from SkillFactory_practice.Completing_tasks.Test_Automation.Modul_19.Task_19_7_2_PetFriends_project.settings import *
from SkillFactory_practice.Completing_tasks.Test_Automation.Modul_19.Task_19_7_2_PetFriends_project.api import \
    PetFriends

# Если мы взглянем на тест-кейсы, которые мы составляли в модуле 20, то вспомним, что мы пытаемся перебрать
# множество значений для одного и того же параметра, что наталкивает нас на мысль, что мы можем взять тесты
# и параметризовать их по параметру, который тестируем в данный момент. Давайте это и попробуем сделать.
#
# Для начала возьмём тест, который получает список питомцев, и попробуем поставить его на рельсы параметризации.
# Для этого обратимся к интеллект-карте, которую мы составляли, и вспомним, какие тесты мы проектировали для этого
# метода для параметра filter:
#
# --пустая строка;
# --my_pets;
# --строка = 255 символов;
# --строка длиной > 1000 символов;
# --кодировка (кириллица, китайские символы);
# --спецсимволы;
# --число.

pf = PetFriends()


@pytest.fixture(autouse=True)
def ket_api_key():
    """ Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, pytest.key = pf.get_api_key(valid_email, valid_password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in pytest.key

    yield

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert pytest.status == 200


@pytest.mark.parametrize("filter", ['', 'my_pets'], ids=['empty string', 'only my pets'])
def test_get_all_pets_with_valid_key(filter):
    """ Проверяем, что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api-ключ и сохраняем в переменную auth_key. Далее, используя этот ключ,
    запрашиваем список всех питомцев и проверяем, что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)

    assert len(result['pets']) > 0
