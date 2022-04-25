class Client:
    """Класс клиент"""

    def __init__(self, name, lastname, balance):
        """Инициализация атрибутов класса клиент"""
        self.name = name
        self.lastname = lastname
        self.balance = balance

    def client_general(self):
        """Возвращение информации клиента"""
        return print("Клиент:", self.name, self.lastname,
                     "Баланс:", self.balance)


new_user_1 = Client("Иван", "Петров", 50)
new_user_2 = Client("Петя", "Лямочкин", 350)
new_user_3 = Client("Борис", "Борисович", 230)

users = [new_user_1, new_user_2, new_user_3]
for user in users:
    print(user.client_general())


# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
#
# При выводе в консоль вы должны получить: “Иван Петров, г.Москва, статус "Наставник"
