import requests
import json
import time
from pprint import pprint
import const


def get_weather(location):
    url = const.WEATHER_URL.format(city=location, TOKEN=const.WEATHER_TOKEN)
    response = requests.get(url)
    data = json.loads(response.content)
    if response.status_code != 200:
        return 'city not found'
    pprint(data)

    return parse_weather_data(data)


def parse_weather_data(data):
    for el in data['weather']:
        weather_state = el['main']
    temp = round(data['main']['temp'] - 273.15, 2)
    city = data['name']
    msg = f'The weather in {city}: Temperature is {temp}, State is {weather_state}'
    print(msg)
    return msg


def answer_user_bot(data):
    data = {
        'chat_id': const.MY_ID,
        'text': data
    }
    url = const.URL.format(TOKEN=const.TOKEN, method=const.SEND_METH)
    response = requests.post(url, data=data)
    print(response)


def get_message(data):
    return data['message']['text']


def save_update_id(update):
    pprint(update)
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    const.UPDATE_ID = update['update_id']
    return True


def main():
    while True:
        url = const.URL.format(TOKEN=const.TOKEN, method=const.UPDATE_METH)
        content = requests.get(url).text
        data = json.loads(content)
        result = data['result'][::-1]
        needed_part = None

        for el in result:
            if el['message']['chat']['id'] == const.MY_ID:
                needed_part = el
                break

        if const.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            msg = get_weather(message)
            answer_user_bot(msg)
            save_update_id(needed_part)

        time.sleep(2)


if __name__ == '__main__':
    main()
