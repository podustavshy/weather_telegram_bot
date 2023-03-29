from response import api_request
from typing import Dict
from loader import api
from datetime import datetime


def display(method_endswith: str, params: Dict, method_type: str):
    data = api_request(method_endswith, params, method_type)

    if method_endswith == 'weather':
        sunrise_timestamp = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        print(
            f"Дата и время: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            f"Погода в городе: {data['name']}\n"
            f"Температура: {data['main']['temp']}C°, {data['weather'][0]['description']}\n"
            f"Влажность: {data['main']['humidity']}%\n"
            f"Давление: {data['main']['pressure']} мм.рт.ст\n"
            f"Ветер: {data['wind']['speed']} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\n"
            f"Закат солнца: {sunset_timestamp}\n"
            f"Продолжительность дня: {length_of_the_day}\n"
        )
    else:
        print(f"Погода в городе: {data['city']['name']}\n")
        for interval in data['list']:
            print(
                f"Дата и время: {interval['dt_txt']}\n"
                f"Температура: {interval['main']['temp']}C°, {interval['weather'][0]['description']}\n"
                f"Влажность: {interval['main']['humidity']}%\n"
                f"Давление: {interval['main']['pressure']} мм.рт.ст\n"
                f"Ветер: {interval['wind']['speed']} м/с\n"
            )


# display(method_endswith='weather',
#                        params={'q': 'Kaluga', 'cnt': 41, 'appid': api, 'units': 'metric', 'lang': 'ru'},
#                        method_type='GET')