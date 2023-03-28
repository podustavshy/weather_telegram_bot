from telebot.types import Message
from loader import bot


@bot.message_handler(regexp='Привет')
def hello_message(message: Message) -> None:
    bot.send_message(message.chat.id, 'Привет!')
