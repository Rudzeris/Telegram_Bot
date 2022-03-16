import telebot


bot = telebot.telebot("5185800841:AAGFilwyMnpbdLcy4PavNjPAMqqGANcNJTI")


@bot.message_hadler(content_types=['text'])
def get_text_message(message):
    bot.send_message(message.from_user.id, f"кто здесь")