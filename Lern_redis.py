import redis
import json

red = redis.Redis(
    host='redis-19046.c98.us-east-1-4.ec2.cloud.redislabs.com',
    port=19046,
    password='4EkrVV3BxanFsMcG3wt7hmexMnf7v2uD'
)

# red.set('var1', 'value1')  # записываем в кеш строку "value1"
# print(red.get('var1'))  # считываем из кэша данные

# ----------------------------------------------------------------------

# dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаем словарь для записи
# red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превращает наш словарь в строчку
# converted_dict = json.loads(red.get('dict1'))  # с помощью знакомой нам функции превращаем данные полученные из кэша
# # обратно в словарь
#
#
# print(type(converted_dict))  # убеждаемся, что получили действительно словарь
# print(converted_dict)  # ну и выводим его содержание

# ----------------------------------------------------------------------

# red.delete('dict1')  # удаляем ключи с помощью метода .delete()
# print(red.get('dict1'))

# ----------------------------------------------------------------------

# Задание 18.5.4
# Напишите программу, которая будет записывать и кэшировать номера ваших друзей.
# Программа должна уметь воспринимать несколько команд: записать номер, показать
# номер друга в консоли при вводе имени или же удалить номер друга по имени.
# Кэширование надо производить с помощью Redis. Ввод и вывод информации должен быть реализован через консоль
# (с помощью функций input() и print()).

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break
