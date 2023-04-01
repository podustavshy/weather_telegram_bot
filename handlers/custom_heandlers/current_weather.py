from loader import bot
from loader import api
from telebot.types import Message
from site_API import display


@bot.message_handler(commands=['current_weather'])
def current_weather(message: Message) -> None:
    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            location = data['location']

        bot.send_message(message.from_user.id,
                         display.display(method_endswith='weather',
                                         params={'q': location, 'appid': api, 'units': 'metric', 'lang': 'ru'},
                                         method_type='GET'
                                         ))

    except Exception as exc:
        bot.send_message(message.from_user.id, 'Выберете город и попробуйте снова')
