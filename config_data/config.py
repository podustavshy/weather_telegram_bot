import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('setloc', "Выбрать город"),
    ('changeloc', "Изменить город"),
    ('current_weather', "Текущая погода"),
    ('one_day', "Погода на день, с 3-часовым шагом"),
    ('five_days', "Погода на 5 деней, с 3-часовым шагом, в виде графика"),
    ('history', 'История запросов (не более 10 запросов)')
)
