import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import requests
from Util.util import create_folder, chek_key, get_file, save
import random
from loguru import logger


class Crawler:

    def __init__(self, config, apikey=None):
        self.config = config
        self.pred_crawl()
        self.apikey = apikey

    def pred_crawl(self):
        create_folder(self.config['folder_name']['PAGE_DIR'])
        if chek_key('X-Api-Key', self.config['HEDERS']):
            self.crawl(get_file(self.config['folder_name']['TODO_DIR']))
        else:
            user = self.config['user'][f'{random.choice(list(self.config['user']))}']
            res = requests.post(url=self.config['URL_SING_IN']['url'], json=user, headers=self.config['HEDERS'])
            if self.post_crawl(res):
                data_user = res.json()
                self.config['HEDERS'].update({'X-Api-Key': data_user['apiKey']})
            self.crawl(get_file(self.config['folder_name']['TODO_DIR']))

    def crawl(self, data):
        page = requests.post(url=data['Url'], json=self.config['body'], headers=self.config['HEDERS'])
        logger.info(f'crawler page cars av')
        if self.post_crawl(page):
            save('cars', page.json(), self.config['folder_name']['PAGE_DIR'])
            logger.info(f'save pege av')
        else:
            pass

    def post_crawl(self, response) -> bool:
        if response.status_code == 200:
            return True
        else:
            return False

    def next_pege(self):
        pass