import telebot

from config import BOT_TOKEN, OW_TOKEN
from weather import get_weather


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_command(message):
        msg = f'Hi, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! Enter any city. I send you ' \
              f'its weather '
        bot.send_message(message.chat.id, "Hi! Enter any city. I send you its weather")

    @bot.message_handler()
    def get_message(message):
        msg = message.text
        try:
            answer = get_weather(msg, OW_TOKEN)
            bot.send_message(message.chat.id, answer)
        except:
            bot.send_message(message.chat.id, "\U00002620 Check city's name \U00002620")

    bot.polling(none_stop=True)


if __name__ == '__main__':
    telegram_bot(BOT_TOKEN)
