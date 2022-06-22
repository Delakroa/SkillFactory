#!/usr/bin/python3
# -*- encoding=utf8 -*-


# Этот пример показывает, как мы можем управлять неудачными тестами и
# делать снимки экрана после любого неудачного теста.

import pytest
import allure
import uuid


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Эта функция помогает обнаружить, что какой-то тест не пройден.
    # и передать эту информацию для разборки:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):
    browser = selenium
    browser.set_window_size(1400, 1000)

    # Вернуть экземпляр браузера в тестовый пример:
    yield browser

    # Сделайте разрыв (этот код будет выполняться после каждого теста):

    if request.node.rep_call.failed:
        # Сделайте снимок экрана, если тест не пройден:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Сделайте скриншот для локальной отладки:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Прикрепите скриншот к отчету Allure:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            # Для счастливой отладки:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass  # просто игнорируйте любые ошибки здесь


def get_test_case_docstring(item):
    """ Эта функция получает строку документа из тестового примера и форматирует ее.
        чтобы отображать эту строку документации вместо имени тестового примера в отчетах.
    """

    full_name = ''

    if item._obj.__doc__:
        # Удалите лишние пробелы из строки документа:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Сгенерируйте список параметров для параметризованных тестовых случаев:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Создать список на основе Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Добавьте dict со всеми параметрами к имени тестового примера:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ Эта функция изменяет имена тестовых случаев «на лету».
        во время выполнения тестовых случаев.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Эта функция изменяла имена тестовых случаев «на лету».
        когда мы используем параметр --collect-only для pytest
        (чтобы получить полный список всех существующих тестов).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # Если в тестовом примере есть строка документа, нам нужно изменить ее имя на
            # это строка документа для отображения удобочитаемых отчетов и для
            # автоматически импортировать тестовые случаи в систему управления тестированием.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
