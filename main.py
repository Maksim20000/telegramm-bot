import telebot, random
from telebot import types

config = '6982169408:AAHMqnb3SvLH2zbY5VGOxeivib7y3us-RsA'

bot = telebot.TeleBot(config)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('котейка.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Как дела?')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, f'Добро пожаловать, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 10)))

        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Все круто)', reply_markup=markup)
            print(message.chat.type)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'ВОТ И ОТЛИЧНИНЬКО')

        if call.data == 'bad':
            bot.send_message(call.message.chat.id, 'грусненько((')

bot.polling(none_stop=True)
