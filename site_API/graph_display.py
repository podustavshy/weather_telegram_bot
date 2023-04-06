from site_API.response import api_request
from typing import Dict
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def graph_display(method_endswith: str, params: Dict, method_type: str):
    data = api_request(method_endswith, params, method_type)

    fig, axs = plt.subplots(nrows=4, ncols=1)
    fig.suptitle(f"Погода в городе: {data['city']['name']}")

    dt = []
    temp = []
    humidity = []
    pressure = []
    wind_speed = []

    for interval in data['list']:
        dt.append(datetime.fromtimestamp(int(interval['dt'])).strftime('%d %b\n%H:%M'))
        temp.append(interval['main']['temp'])
        humidity.append(interval['main']['humidity'])
        pressure.append(interval['main']['pressure'])
        wind_speed.append(interval['wind']['speed'])

    axs[0].plot(dt, temp)
    axs[0].set_ylabel('Температура, C°')
    axs[1].plot(dt, humidity)
    axs[1].set_ylabel('Влажность, %')
    axs[2].plot(dt, pressure)
    axs[2].set_ylabel('Давление, мм.рт.ст')
    axs[3].plot(dt, wind_speed)
    axs[3].set_ylabel('Ветер, м/с')

    for index in range(4):
        axs[index].grid(which='major')
        axs[index].grid(which='minor')
        axs[index].xaxis.set_major_locator(ticker.MultipleLocator(5))
        axs[index].minorticks_on()

    fig.set_figheight(12)
    fig.set_figwidth(12)

    plt.savefig('weather_for_five_days_' + params['q'])
