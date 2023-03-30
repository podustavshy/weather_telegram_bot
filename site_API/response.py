from pprint import pprint

import requests
from typing import Dict
from loader import api


def api_request(method_endswith: str, params: Dict, method_type: str):
    url = f"https://api.openweathermap.org/data/2.5/{method_endswith}"

    if method_type == 'GET':
        return get_request(
            url=url,
            params=params
        )


def get_request(url: str, params: Dict):
    try:
        response = requests.get(
            url=url,
            params=params,
            timeout=10
        )
        if response.status_code == requests.codes.ok:
            return response.json()
    except Exception as exc:
        print(exc)
        print('Проверьте название города')


# pprint(api_request(method_endswith='forecast',
#                        params={'q': 'Kaluga', 'cnt': 41, 'appid': api, 'units': 'metric', 'lang': 'ru'},
#                        method_type='GET'))