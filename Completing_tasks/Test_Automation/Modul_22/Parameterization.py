import pytest


# Параметризация с помощью фикстуры:

# def python_string_slicer(str):
#     if len(str) < 50 or "python" in str:
#         return str
#     else:
#         return str[0:50]
#
#
# def generate_id(val):
#     return "params: {0}".format(str(val))
#
#
# @pytest.fixture(scope="function", params=[
#     ("Короткая строка", "Короткая строка"),
#     ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
#      , "Длинная строка, не то чтобы прям очень длинная, но"),
#     ("Короткая строка со словом python", "Короткая строка со словом python"),
#     ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
#      , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"),
# ], ids=generate_id)
# def param_fun_generated(request):
#     return request.param
#
#
# def test_python_string_slicer_generated(param_fun_generated):
#     (input, expected_output) = param_fun_generated
#     result = python_string_slicer(input)
#     print("Входная строка: {0}\r\nВыходная строка: {1}"
#           "\r\nОжидаемое значение: {2}".format(input, result, expected_output))
#     assert result == expected_output


# -----------------------------------------------------------------------------------------------------------------

# Параметризация с помощью pytest.mark.parametrize

# Мы могли решить первую задачу, используя встроенную фикстуру pytest parametrize. Этот способ удобен ещё и тем,
# что позволяет более гибко управлять набором тестов, создаваемых с помощью параметризации.
#
# Если указать несколько меток с разными параметрами, то тест будет запущен со всеми возможными наборами параметров
# (то есть мы имеем декартово произведение). Напишем простой тест, чтобы это продемонстрировать:

# @pytest.mark.parametrize("x", [1, 2, 3])
# @pytest.mark.parametrize("y", [10, 11])
# def test_multiply_params(x, y):
#     print("x: {0}, y: {1}".format(x, y))
#     assert True


# -----------------------------------------------------------------------------------------------------------------

# В фикстуру метке parametrize также можно передать параметр ids, и он точно так же будет ответственен за отображение
# параметров в выводе. Точно так же нам доступны два варианта передачи ids в фикстуру — в виде имени функции или набора
# значений. Для начала давайте посмотрим, как передаётся набор значений:

# @pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
# @pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
# def test_multiply_params(x, y):
#     print("x: {0}, y: {1}".format(x, y))
#     assert True

# -----------------------------------------------------------------------------------------------------------------

# Проделаем аналогичные операции с генератором имён параметров:

# def ids_x(val):
#     return "x=({0})".format(str(val))
#
#
# def ids_y(val):
#     return "y=({0})".format(str(val))
#
#
# @pytest.mark.parametrize("x", [-1, 0, 1], ids=ids_x)
# @pytest.mark.parametrize("y", [100, 1000], ids=ids_y)
# def test_multiply_params(x, y):
#     print("x: {0}, y: {1}".format(x, y))
#     assert True

# -----------------------------------------------------------------------------------------------------------------

