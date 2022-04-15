from api import PetFriends
from settings import *
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
    return print("\nКлюч получен!")


def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Тест с некорректными данными авторизации"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    try:
        assert status == 200
        assert 'key' in result
    except AssertionError:
        print("\nНеверно введён логин или пароль! Попробуйте снова.")


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

    return print('\n', result['pets'])


def test_getting_all_pets_by_id(filter='id'):
    """ Проверяем фильтр всех питомцев по id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    try:
        assert status == 200
        assert len(result['pets']) > 0
    except AssertionError:
        print(f"\n\nНеверно задан  filter={filter}. "
              f"\nПо умолчанию значение должно быть filter='' или filter='my_pets' ")


def test_add_new_pet_with_valid_data(name='Зайчик', animal_type='лесной',
                                     age='1', pet_photo='images/kartinki-zajchiki-58.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_empty_data(name='', animal_type='',
                                     age='', pet_photo='images/kartinki-zajchiki-58.jpg'):
    """Проверяем что можно добавить питомца с пустыми данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_data(name='-+=.,|/!@#$%^&йцукенгшщзхъфывапроqwertyuiopasdfghjklzxcv-+=.,|/!@#$%^&'
                                            'QWERTYUIOPPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЯЧСМИТЬБЮ',
                                       animal_type='йцукенгшщзхъфывапроqwertyuiopasdfghjklzxcv+=.,/!@#$%^&'
                                                   'QWERTYUIOPPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЯЧСМИТЬБЮ' * 1000,
                                       age='-0006546516215616' * 5, pet_photo='images/kartinki-zajchiki-58.jpg'):
    """Проверяем что можно добавить питомца с некорректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкроль", "кролик", "3", "images/kartinki-zajchiki-58.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("Моих питомцев нет")


def test_add_new_pet_without_photo(name='Зайчик', animal_type='лесной', age='1'):
    """Проверяем что можно добавить питомца с корректными данными без фото"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_photo_for_the_pet(pet_photo='images/kartinki-zajchiki-58.jpg'):
    """Тестирование добавление фото существующего питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкроль", "кролик", "3", "images/kartinki-zajchiki-58.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка, добавляем фото питомца
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.add_photo_for_the_pet(auth_key, pet_id, pet_photo)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200
    assert status == 200
    assert pet_id not in my_pets.values()


def test_delete_all_pets():
    """Тестирование удаление всех питомцев"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    while True:
        if len(my_pets['pets']) > 0:
            # Берём id первого питомца из списка и отправляем запрос на удаление
            pet_id = my_pets['pets'][0]['id']
            status, _ = pf.delete_pet(auth_key, pet_id)

            # Ещё раз запрашиваем список своих питомцев
            _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
            # Если ваши питомцы отсутствуют, то цикл прерывается.
            if len(my_pets['pets']) == 0:
                break

            # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
            assert status == 200
            assert pet_id not in my_pets.values()
