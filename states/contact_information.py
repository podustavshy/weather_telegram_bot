from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    location = State()

