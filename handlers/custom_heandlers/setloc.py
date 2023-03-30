from keyboards.reply.contact import request_contact
from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(commands=['setloc'])
def setloc(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.location, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username} введи название города')


@bot.message_handler(state=UserInfoState.location)
def get_location(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, 'Спасибо, записал.')

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['location'] = message.text

        bot.delete_state(message.from_user.id, message.chat.id)

    else:
        bot.send_message(message.from_user.id, 'Город может содержать только буквы')
