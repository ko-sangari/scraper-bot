import telebot
from dotenv import dotenv_values

ENV = dotenv_values('.env')

bot = telebot.TeleBot(ENV['TELEGRAM_TOKEN'], parse_mode=None)


def direct_message(telegram_id: int, text: dict) -> None:
    bot.send_message(
        telegram_id,
        f"{text['link']}\n"
        f"{text['location']}\n"
        f"{text['available_from']}\n"
        f"{text['price']} €\n"
        f"{text['tags']}\n"
    )


@bot.message_handler(commands=['start'])
def command_start(message):
    print(f" [INFO]: Telegram ID {message.chat.id}")
    bot.send_message(message.chat.id, f"Your Telegram ID : {message.chat.id}")


def telegram_bot() -> None:
    bot.infinity_polling()


if __name__ == '__main__':
    print(' [INFO]: Telegram Running ...')
    telegram_bot()
    print(' [INFO]: Telegram Closed.')
