

def test_search_example(selenium):
    """Найдите в гугле какую-нибудь фразу и сделайте скриншот страницы."""

    # Откройте страницу поиска:
    selenium.get('http://google.com')

    # Найдите поле для ввода поискового текста:
    search_input = selenium.find_element_by_id('lst-ib')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys('my first selenium test for Web UI!')

    # Нажмите Поиск:
    search_button = selenium.find_element_by_name('btnK')
    search_button.click()

    # Сделать скриншот окон браузера:
    selenium.save_screenshot('result.png')

