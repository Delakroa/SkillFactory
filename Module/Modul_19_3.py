import json.decoder
import requests


def get_api_key(email: str, passwd: str):
    headers = {
        'email': email,
        'password': passwd,
    }
    res = requests.get(url="https://petfriends1.herokuapp.com/login", headers=headers)
    status = res.status_code
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result.count()


print(get_api_key('skillfaktory*****@gmail.com', '*******'))
