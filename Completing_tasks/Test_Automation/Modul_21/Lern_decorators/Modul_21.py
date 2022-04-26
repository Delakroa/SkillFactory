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

# @pytest.fixture(scope="class", autouse=True)
# def session_fixture():
#     print("\nclass fixture starts")
#
#
# @pytest.fixture(scope="function", autouse=True)
# def function_fixture():
#     print("\nfunction fixture starts")
#
#
# class TestClass23:
#
#     def test_first(self):
#         pass
#
#     def test_second(self):
#         pass


# ------------------------------------------------------------------------------------

# Фикстура request

# @pytest.fixture()
# def request_fixture(request):
#     print(request.fixturename)
#     print(request.scope)
#     print(request.function.__name__)
#     print(request.cls)
#     print(request.module.__name__)
#     print(request.fspath)
#     if request.cls:
#         return f"\n У теста {request.function.__name__} класс есть\n"
#     else:
#         return f"\n У теста {request.function.__name__} класса нет\n"
#
#
# def test_request_1(request_fixture):
#     print(request_fixture)
#
#
# class TestClassRequest:
#
#     def test_request_2(self, request_fixture):
#         print(request_fixture)

# ------------------------------------------------------------------------------------

# Разберём на практике

# Попробуем применить на практике указание области видимости фикстур и фикстуру request.
# Как мы уже раньше заметили, нам приходится регулярно перед тестами получать id сессии, для того чтобы отправить
# запросы в Дом Питомца.
# Попробуем фикстуре, в которой мы получаем токен указать более глобальный scope.

# @pytest.fixture(scope="class")
# def get_key(request):
#     # переменные email и password нужно заменить своими учетными данными
#     response = requests.post(url='https://petfriends1.herokuapp.com/login',
#                              data={"email": email, "pass": password})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
#     print("\nreturn auth_key")
#     return response.request.headers.get('Cookie')
#
#
# @pytest.fixture(autouse=True)
# def request_fixture(request):
#     if 'Pets' in request.function.__name__:
#         print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")
#
#
# class TestClassPets:
#
#     def test_getAllPets2(self, get_key):
#         response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
#                                 headers={"Cookie": get_key})
#         assert response.status_code == 200, 'Запрос выполнен неуспешно'
#         assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
#
#     def test_getMyPets2(self, get_key):
#         response = requests.get(url='https://petfriends1.herokuapp.com/my_pets',
#                                 headers={"Cookie": get_key})
#         assert response.status_code == 200, 'Запрос выполнен неуспешно'
#         assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'
#
#     def test_anotherTest(self):
#         pass

# -----------------------------------------------------------------------------------------------------------------


