import os
from loader import bot
from loader import api
from telebot.types import Message
from site_API.graph_display import graph_display


@bot.message_handler(commands=['five_days'])
def five_days(message: Message) -> None:
    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            location = data['location']

            graph_display(method_endswith='forecast',
                          params={'q': location, 'appid': api, 'cnt': 41, 'units': 'metric', 'lang': 'ru'},
                          method_type='GET'
                         )

        with open(
                r'C:\Users\Подуставшый\PycharmProjects\pythonProject\python_basic_diploma\weather_for_five_days.png',
                'rb'
        ) as file:

            bot.send_photo(message.from_user.id, file)

        # os.remove(r'C:\Users\Подуставшый\PycharmProjects\pythonProject\python_basic_diploma\weather_for_five_days.png')

    except Exception as exc:
        bot.send_message(message.from_user.id, 'Выберете город и попробуйте снова')
