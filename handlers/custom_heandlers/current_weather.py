from loader import bot
from loader import api
from telebot.types import Message
from site_API import display


@bot.message_handler(commands=['current_weather'])
def current_weather(message: Message) -> None:
    bot.send_message(message.from_user.id,
                     display.display(method_endswith='weather',
                                     params={'q': 'Kaluga', 'appid': api, 'units': 'metric', 'lang': 'ru'},
                                     method_type='GET'
                                     ))


