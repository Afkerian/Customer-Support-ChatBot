import telebot

#bot=telebot.TeleBot("TOKEN")
bot=telebot.TeleBot("6169344427:AAHwrimcGn_CGCZSQB0RNGeK6qMreO5xUcQ")
@bot.message_handler(commands=['start'])

def enviar(message):
    bot.reply_to(message, "Hola! ¿Como puedo ayudarte?")

@bot.message_handler(func=lambda message:True)
def mensaje(message):
    bot.reply_to(message, message.text)

bot.polling()