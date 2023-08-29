import telebot

#bot=telebot.TeleBot("TOKEN")
bot=telebot.TeleBot("Token")
@bot.message_handler(commands=['start'])

def enviar(message):
    bot.reply_to(message, "Hola! ¿Como puedo ayudarte?")

@bot.message_handler(func=lambda message:True)
def mensaje(message):
    bot.reply_to(message, message.text)

bot.polling()