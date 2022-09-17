# 5786234216:AAHWs_UT0ltxAqZMw1Me_1P_N1SK8ge7hUA
import telegram
import requests
import re
import telebot


# Первое, что нужно сделать это подключить токен бота:
bot = telebot.TeleBot('5786234216:AAHWs_UT0ltxAqZMw1Me_1P_N1SK8ge7hUA')

#  Теперь объявим метод для получения текстовых сообщений:
@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.chat.id, 'правила группы, и теги для поиска инф в описании')

"""
Теперь наш бот будет постоянно спрашивать у сервера Телеграмма 
«Мне кто-нибудь написал?», и если мы напишем нашему боту, 
то Телеграмм передаст ему наше сообщение. """

# что бы он постоянно работал
bot.polling(none_stop=True)

# левая функция не используется
def get_data():
    rec = requests.get()