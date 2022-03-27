import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handlers(filter)
def function_name(message):
    bot.reply_to(message, "This is message handler")


bot.polling(none_stop=True)

