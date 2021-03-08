TOKEN = 'You can get if from @Botfather '

URL = 'https://api.telegram.org/bot{TOKEN}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 417352875

UPDATE_ID_FILE_PATH = 'update_id'


WEATHER_TOKEN = 'You can get it from api.openweathermap.org'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = file.readline()
