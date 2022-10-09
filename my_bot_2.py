import telebot

token = '5583576601:AAFvQ5w4DKF7QjkaPdrPwBD7PawClE6VCes'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    pilaf = telebot.types.InlineKeyboardButton(text='Хочу плов', callback_data='1')
    shashlik = telebot.types.InlineKeyboardButton(text='Хочу шашлык', callback_data='2')
    keyboard.add(pilaf)
    keyboard.add(shashlik)
    return keyboard


@bot.message_handler(commands=['start'])
def start_bot(msg):
    keyboard = create_keyboard()
    bot.send_message(msg.chat.id, 'Какие планы на обед?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == '1':
            img = open('pilaf.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Отличное решение!',
                reply_markup=keyboard
            )
            img.close()
        elif call.data == '2':
            img = open('shashlik.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Отличное решение!',
                reply_markup=keyboard
            )
            img.close()


if __name__ == '__main__':
    bot.polling(none_stop=True)