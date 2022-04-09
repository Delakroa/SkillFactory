import requests


class PetFriends:
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

    def get_list_of_pets(self, auth_key, filter):
        """Получить список домашних животных"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

