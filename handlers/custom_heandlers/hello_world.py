from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['hello-world'])
def hello_world_message(message: Message) -> None:
    bot.send_message(message.chat.id, 'Hello World!')


