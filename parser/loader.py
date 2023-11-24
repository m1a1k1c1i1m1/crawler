import os
import peckage
from loguru import logger
from time import sleep
from sing_up import *


util = peckage.Utils()
config = peckage.Setings()

api_key = sing_up()


class Load(peckage.Loader):
    def __init__(self,):
        self.run_load()
        super().__init__()

    def load_url(self, data):
        self.data = data
        HEDERS = {
            "Content-type": "application/json",
            "X-Api-Key": 'p4ead4a57824d75bdc88702',
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Origin": "https://cars.av.by",
            "Referer": "https://cars.av.by/",
            "Sec-Ch-Ua": 'Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }

        response = self.type_zapros(self.data, HEDERS)
        try:
            if not util.chek_dir(peckage.PAGE_DIR):
                util.create_dir(peckage.PAGE_DIR)
                util.seve_response(config.json_content(response, self.data), peckage.PAGE_DIR)
            else:
                util.seve_response(config.json_content(response, self.data), peckage.PAGE_DIR)
        except Exception as error:
            logger.error('{} возникла в функции load_url в файле loader.py'.format(error))

    def run_load(self):
        while True:
            try:
                list_file = os.listdir(peckage.TODO_DIR)
                name_dir = peckage.TODO_DIR
                for item in list_file:
                    data = util.open_file(item, name_dir)
                    self.load_url(data)
                    util.delet_file(peckage.TODO_DIR + item, peckage.TODO_DIR)
                if len(list_file) == 0:
                    sleep(10)
            except Exception as error:
                logger.error(error)


if __name__ == "__main__":
    load = Load()
