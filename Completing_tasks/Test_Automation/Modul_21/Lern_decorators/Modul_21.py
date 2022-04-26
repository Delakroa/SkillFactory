from decorators import do_twice
import pytest
import requests
from datetime import datetime
from config import email, password


# @do_twice
# def test_twice_without_params():
#     print("Этот вызов без параметров")


# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#     return "Done"


# @do_twice
# def test_twice_2_params(str1, str2):
#     print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))
#
#
# test_twice_without_params()
# test_twice("single")
# test_twice_2_params(1, 2)

# decorated_value = test_twice("single")
# print(decorated_value)


# ------------------------------------------------------------------------------------

# Фикстуры, которая возвращает число:

# @pytest.fixture()
# def some_data():
#     return 42
#
#
# def test_some_data(some_data):
#     assert some_data == 42


# ------------------------------------------------------------------------------------

# Организация setup фикстурах
# @pytest.fixture()
# def get_key():
#     # переменные email и password нужно заменить своими учетными данными
#     response = requests.post(url='https://petfriends1.herokuapp.com/login',
#                              data={"email": email, "pass": password})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
#     return response.request.headers.get('Cookie')
#
#
# def test_getAllPets(get_key):
#     response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
#                             headers={"Cookie": get_key})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
#
#
# # Организация teardown в фикстурах
# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f"\nТест шел: {end_time - start_time}")

# ------------------------------------------------------------------------------------

# Области видимости фикстур.

@pytest.fixture(scope="class", autouse=True)
def session_fixture():
    print("\nclass fixture starts")


@pytest.fixture(scope="function", autouse=True)
def function_fixture():
    print("\nfunction fixture starts")


class TestClass23:

    def test_first(self):
        pass

    def test_second(self):
        pass

# ------------------------------------------------------------------------------------

# Фикстура request

