import json.decoder

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """API библиотека к веб приложению Pet Friends"""

    def __init__(self):
        """Инициализация сайта дом питомца"""
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email: str, password: str = ""):
        """Метод делает запрос к API сервера и возвращает статус запроса и результата в формате JSON
        с уникальным ключём пользователя, найденного по указанным email и паролем"""
        headers = {
            'email': email,
            'password': password
        }

        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком найденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления об успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер об обновлении данных питомца по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлёнными данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


# Первая часть практического задания 19.7.2

# У нас есть готовая библиотека с реализацией основных методов, но остались ещё два нереализованных метода.
# Это и будет первым практическим заданием: посмотреть документацию к имеющимся API-методам на сайте
# https://petfriends1.herokuapp.com/apidocs/#/default/put_api_pets__pet_id_. Найти методы,
# которые ещё не реализованы в библиотеке, и написать их реализацию в файле api.py.

# Эти запросы нужно написать реализацию
# POST /api/create_pet_simple
# POST /api/pets/set_photo/{pet_id}

# Вторая часть задания:

# Как вы уже изучали ранее, видов тестирования много, соответственно, и тест-кейсов может быть очень много.
# Мы с вами написали пять простых позитивных тестов, проверяющих функционал с корректными данными,
# с ожиданием того, что всё пройдёт хорошо. Наша задача — убедиться, что система возвращает статус с кодом 200.
# Но как будет реагировать тестируемое приложение, если мы в параметрах передадим слишком большое значение или вообще
# его не передадим? Что будет, если мы укажем неверный ключ авторизации и так далее?
#
# Подумайте над вариантами тест-кейсов и напишите ещё 10 различных тестов для данного REST API интерфейса.
# Готовые тест-кейсы разместите на GitHub и пришлите ссылку.
