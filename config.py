from configparser import ConfigParser

config = ConfigParser()
config.read('conf.cfg')

YANDEX_API_KEY = config['DEFAULT']['YANDEX_API_KEY']

TOKEN = config['DEFAULT']['TELEGRAM_TOKEN']
SEND_MSG_URL = "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)

MESSAGE = "Хочу пить пиво!"
CERTAIN_MESSAGE = """Общий сбор!
Встречаемся в {}
Причина: {}
Место: {} """

