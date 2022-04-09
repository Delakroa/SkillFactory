import requests


class PetFriends:
    def __init__(self):
        """Инициализация сайта дом питомца"""
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email, password):
        """Получение аутентификационнго ключа"""
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
