from telebot.types import Message
from database.common.models import db, History
from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    text = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    response = '\n'.join(text)

    bot.reply_to(message, response)

    with db:
        History.create(name=message.from_user.full_name, telegram_id=message.from_user.id,
                       message=message.text, response=response)