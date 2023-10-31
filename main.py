import telebot

config = '6982169408:AAHMqnb3SvLH2zbY5VGOxeivib7y3us-RsA'

bot = telebot.TeleBot(config)


@bot.message_handler(content_types=['text'])
def lalala(massage):
    bot.send_message(massage.chat.id, massage.text)

bot.polling(none_stop=True)
