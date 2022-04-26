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

# 21.5 Встроенные фикстуры pytest

# Данная фикстура помечает тест как пропущенный, то есть при запуске тест не будет выполняться. Например,
# у нас написан определенный тест на регистрацию, но мы знаем, что в приложении существует баг,
# который не собираются исправлять в ближайшее время. Такой тест имеет смысл пропускать,
# иначе каждый запуск тестов будет неудачным из-за этого теста.
# Простой декоратор над тестовой функцией позволит нам сделать это:

# @pytest.mark.skip(reason="Баг в продукте - <ссылка>")
# def test_one(): # …  Это наш тест, который находит тот самый баг

# -------------------------------------------------------------------------------------------------------

# pytest.mark.skipif

# Фикстура делает то же самое, что и предыдущая, но мы имеем возможность управлять игнорируемыми тестами.
# Довольно простые примеры, которые хорошо иллюстрируют, как можно пользоваться такой фикстурой —
# это пропуск тестов в случае, когда версия Python ниже определенной.

# @pytest.mark.skipif(sys.version_info < (3, 6), reason="Тест требует python версии 3.6 или выше")
# def test_python36_and_greater():

# Ещё одной приятной особенностью языка является вынесение таких вот проверок в определенное место.
# То есть мы можем создать переменную, в которой будет выполняться проверка версии языка, оборачивать
# в фикстуру pytest и далее использовать её в тестах в виде декоратора:

# minversion = pytest.mark.skipif(
#     sys.version_info < (3, 6), reason="at least mymodule-1.1 required"
# )
#
# @minversion
# def test_python36_and_greater():

# Этот код написан в одном файле, но ничего не мешает вынести наш декоратор в отдельный файл и
# импортировать его в нужных файлах с тестами.
#
# Перечисленные фикстуры могут применяться аналогичным образом к целым классам с тестами. Например,
# это удобно применять, когда у нас имеется несколько файлов с тестами для различных операционных систем,
# но мы не знаем заранее, на компьютере с какой ОС будет запускаться пачка тестов.

# ----------------------------------------------------------------------------------------------

# pytest.mark.xfail
#
# Помечает тест как падающий. Например, вы написали тест, который отлично работает на локальной машине,
# прошли код-ревью, и вот он уже оказался в ветке с остальными тестами. Однако по какой-то причине этот тест довольно
# часто завершается с ошибкой в инфраструктуре организации. Чтобы не забыть починить такой тест,
# удобно пометить его как нестабильный, используя фикстуру xfail:

# @pytest.mark.xfail
# def test_flaky():

# В данном случае тест прошел успешно, поэтому его состояние помечено как XPASS. При неудачном прохождении теста
# статус будет XFAILED. Так же, как и в фикстуре skipif, мы можем пометить тест xfail при определенных условиях.
# Для этого в качестве первого аргумента в декоратор нужно передать условие, при котором тест будет принимать статус
# xfail:

# @pytest.mark.xfail(sys.platform == "win32", reason="Ошибка в системной библиотеке") # На платформе Windows ожидаем,
# # что тест будет падать
# def test_not_for_windows():

# Как мы видим, для этого теста указан также reason.
# Если мы хотим быть более конкретными в причинах падения, то мы можем указать такую причину в аргументе raises
# фикстуры xfail. Например, следующий тест будет помечен xfail только в том случае, если произойдет исключение
# типа RuntimeException, в противном случае тест будет выполняться как обычно (помечаться passed, если пройдет
# успешно, и failed, если пройдет неуспешно):

# @pytest.mark.xfail(raises=RuntimeError)
# def test_x_status_runtime_only():

# ----------------------------------------------------------------------------------------------

# Пользовательские группы

# Этот механизм ничем не отличается от предыдущих — необходимо написать, что мы помечаем тест, и дать имя группы
# (@pytest.mark.auth). Далее необходимо в проекте создать файл pytest.ini, туда внести информацию об описанных в
# тестах группах. Давайте разберём непосредственно в коде. У нас есть четыре теста, два из них на аутентификацию
# пользователя, остальные два — это тесты мероприятий. В каждой такой группе соответственно API и UI тесты:

@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
    pass


@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
    pass


@pytest.mark.api
@pytest.mark.event
def test_event_api():
    pass


@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
    pass


# В корне проекта создадим файл pytest.ini и добавим туда описание наших категорий. Тесты будут запускаться и без
# этого файла, но его наличие избавит нас от постоянных предупреждений в отчетах:

[pytest]
markers =
   api: тесты API
   ui: тесты UI
   event: тесты мероприятий
   auth: тесты авторизации

# Все, что нам осталось сделать — это научиться фильтровать такие тесты. Например, если нам нужно запустить только API
# тесты, то в консоли надо набрать:

pytest test.py -v -m "api" # test.py замените на имя своего файла в проекте


# Можно отбирать тесты по нескольким группам сразу, используя логические операторы. Например, если мы хотим запустить
# только UI тесты авторизации, то команда в консоли будет выглядеть так:

pytest test.py -v -m "ui and auth"


# А если нам нужно запустить все виды тесты на модули авторизации и мероприятий, то команда для запуска будет следующая:
pytest test.py -v -m "auth or event"