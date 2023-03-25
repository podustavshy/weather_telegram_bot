import telebot

token = '5906405404:AAFPB9p35Omd-nZwQFQ4atdH3gjqX_RH97w'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['hello-world'])
def hello_world_message(message):
    bot.send_message(message.chat.id, 'Hello World!')


@bot.message_handler(regexp='Привет')
def hello_message(message):
    bot.send_message(message.chat.id, 'Привет!')


if __name__ == '__main__':
    bot.infinity_polling()
