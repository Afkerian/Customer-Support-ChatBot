import telebot
import configparser
import os
from config import cargar_configuracion
from response import response

config = cargar_configuracion()

apy_key = config.get('API_KEY', 'KEY')


#bot=telebot.TeleBot("TOKEN")
bot=telebot.TeleBot(apy_key)

@bot.message_handler(commands=['start'])
def enviar(message):
    bot.reply_to(message, "Hola! ¿Como puedo ayudarte?")

@bot.message_handler(func=lambda message:True)
def mensaje(message):
    print(f'Usuario: {message.from_user.first_name} \nGPT: {message.text}')
    bot.reply_to(message, response(message.text))

bot.polling()