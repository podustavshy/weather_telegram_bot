from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from database.common.models import db, History


@bot.message_handler(commands=['changeloc'])
def changeloc(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.location, message.chat.id)
    response = 'Введите название города'
    bot.send_message(message.from_user.id, response)

    with db:
        History.create(name=message.from_user.full_name, telegram_id=message.from_user.id,
                       message=message.text, response=response)


@bot.message_handler(state=UserInfoState.location)
def get_location(message: Message) -> None:
    if message.text.isalpha():
        response = 'Спасибо, записал.'
        bot.send_message(message.from_user.id, response)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['location'] = message.text

    else:
        response = 'Город может содержать только буквы'
        bot.send_message(message.from_user.id, response)

    with db:
        History.create(name=message.from_user.full_name, telegram_id=message.from_user.id,
                       message=message.text, response=response)