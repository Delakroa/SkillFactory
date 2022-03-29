import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> ' \
           '<в какую перевести> ' \
           '<количество переводимой валюты> \nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты :'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('Слишком много параметров.')

    quote, base, amount = values
    total_base = CryptoConverter.convert(quote, base, amount)

    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


# @bot.message_handler()
# def echo_test(message: telebot.types.Message):
#     bot.send_message(message.chat.id, "Привет")


# @bot.message_handler(filter)
# def function_name(message):
#     bot.reply_to(message, "Это обработчик сообщений")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass


# Обрабатываются все документы и аудиозаписи
# @bot.message_handler(content_type=['document', 'audio'])
# def handle_docs_audio(message):
#     pass


# Приветственное сообщение с привязкой к пользователю
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message, f"Добро пожаловать,\ c{message.chat.username}")


# @bot.message_handler(content_types=['photo', ])
# def say_lmao(message: telebot.types.Message):
#     bot.reply_to(message, 'Nice meme XDD')


# Бот постоянно работает
print("Бот запущен")
bot.polling()
print("Бот отключен")
