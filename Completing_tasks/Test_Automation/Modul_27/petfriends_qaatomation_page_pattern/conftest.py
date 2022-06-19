#!/usr/bin/python3
# -*- encoding=utf8 -*-

# Это пример показывает, как мы можем управлять неудачными тестами
# и сделайте скриншоты после любого неудачного тестового примера.

import pytest
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
    # Эта функция помогает обнаружить, что какой -то тест вышел из строя
    # и передайте эту информацию Tapdown:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)

    # Вернуть экземпляр браузера для тестирования примера:
    yield browser

    # Do Teardown (этот код будет выполнен после каждого теста):

    if request.node.rep_call.failed:
        # Сделайте съемки экрана, если тест не удался:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Сделайте Screen Shot для локальной отладки:
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
            pass # просто игнорируйте здесь любые ошибки


def get_test_case_docstring(item):
    """ Эта функция получает строку DOC от тестового примера и отформатирует ее
        Чтобы показать этот Docstring вместо названия тестового примера в отчетах.
    """

    full_name = ''

    if item._obj.__doc__:
        # Удалить дополнительные пробелы из строки DOC:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Сгенерировать список параметров для параметризованных тестовых случаев:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Создать список на основе DICT:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Добавить дикта со всеми параметрами к названию тестового примера:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ Эта функция изменяет имена тестовых случаев "на лету"
        Во время выполнения тестовых случаев.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Эта функция изменила имена тестовых случаев "на лету"
        Когда мы используем параметр только для Pytest только для Pytest
        (Чтобы получить полный список всех существующих тестовых случаев).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # Если в тестировании есть строка DOC, нам нужно изменить его имя на
            # это Doc String, чтобы показать читаемые человеческие отчеты и
            # автоматически импортируйте тестовые примеры в систему управления тестированием.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')