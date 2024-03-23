import telebot

from core.settings import settings


bot = telebot.TeleBot(settings.TELEGRAM_TOKEN, parse_mode=None)


def direct_message(text: dict) -> None:
    for user_id in settings.TELEGRAM_IDS:
        bot.send_message(
            user_id,
            f"{text['city']} | "
            f"{text['rent']} € | "
            f"{text['area']}\n"
            f"{text['link']}\n",
        )


@bot.message_handler(commands=["start"])
def command_start(message):
    print(f" [INFO]: Telegram ID {message.chat.id}")
    bot.send_message(message.chat.id, f"Your Telegram ID : {message.chat.id}")


def telegram_bot() -> None:
    bot.infinity_polling()


if __name__ == "__main__":
    print(" [INFO]: Telegram Running ...")
    telegram_bot()
    print(" [INFO]: Telegram Closed.")
