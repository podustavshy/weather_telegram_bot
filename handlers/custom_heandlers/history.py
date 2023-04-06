from loader import bot
from telebot.types import Message
from database.common.models import db, History


@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    with db:
        query = History.select().where(
            History.name == message.from_user.full_name and
            History.telegram_id == message.from_user.id
        ).limit(10).order_by(History.id.desc())

        response = ''
        for entry in query:
            response += f'{entry.created_at}\n{entry.message}\n{entry.response}\n\n'

        bot.send_message(message.from_user.id, response)

        History.create(name=message.from_user.full_name, telegram_id=message.from_user.id,
                       message=message.text, response=response)
