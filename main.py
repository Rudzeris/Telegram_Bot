import telebot
import datetime

bot = telebot.TeleBot('5185800841:AAGFilwyMnpbdLcy4PavNjPAMqqGANcNJTI')



@bot.message_handler(content_types=['text'])
def get_text_message(message):
    username = message.from_user.username
    msg=''
    f = open(f'log {username}.txt', 'a')
    if message.text == 'Привет':
        msg = f'Привет {username}! Хочешь анекдот?'
        bot.send_message(message.from_user.id, msg)
    elif message.text == 'Нет' or message.text == 'нет':
        msg = f'Пидора ответ.\tНу, давай. Хотя бы улыбнешься.\tСогласен?'
        bot.send_message(message.from_user.id, msg)
    elif message.text == 'Да' or message.text == 'да':
        msg = f'Пизда!\tХа! Повёлся.'
        bot.send_message(message.from_user.id, msg)
    elif message.text == 'хочу' or message.text == 'Хочу':
        msg = f'Нужно писать "Да" или "Нет"'
        bot.send_message(message.from_user.id, msg)
    elif message.text == 'Сука' or message.text == 'сука' or message.text == 'бля' or message.text == 'Бля':
        msg = f'Пхахах!\tДолбоеб.'
        bot.send_message(message.from_user.id, msg)
    f.write(f'{datetime.datetime.now()}:\t{message.text}\n')
    if msg=='':
        f.write(f'{datetime.datetime.now()}:\t{msg}\n')
    f.close()

bot.polling()
