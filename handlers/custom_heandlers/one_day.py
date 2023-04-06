from loader import bot
from loader import api
from telebot.types import Message
from site_API.display import display
from database.common.models import db, History


@bot.message_handler(commands=['one_day'])
def current_weather(message: Message) -> None:
    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            location = data['location']

            response = display(method_endswith='forecast',
                               params={'q': location, 'appid': api, 'cnt': 9, 'units': 'metric', 'lang': 'ru'},
                               method_type='GET'
                               )

        bot.send_message(message.from_user.id, response)

    except Exception as exc:
        response = 'Выберете город и попробуйте снова'
        bot.send_message(message.from_user.id, response)

    with db:
        History.create(name=message.from_user.full_name, telegram_id=message.from_user.id,
                       message=message.text, response=response)