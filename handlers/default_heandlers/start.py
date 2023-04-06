from telebot.types import Message
from database.common.models import db, History
from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    response = f"Привет, {message.from_user.full_name}!"

    bot.reply_to(message, response)

    with db:
        History.create(name=message.from_user.full_name, telegram_id=message.from_user.id,
                       message=message.text, response=response)

