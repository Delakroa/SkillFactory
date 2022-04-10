import json.decoder

import requests


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
