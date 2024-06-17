import os
import time

from Util.util import get_file
from loguru import logger
from Util.util import save, get_data_car, create_folder


class Parser:

    def __init__(self, config):
        self.config = config

    def get_json_page(self):
        return get_file(self.config['folder_name']['PAGE_DIR'])

    def pars(self, data: list):
        try:
            for item in data:
                car = get_data_car(item)
                logger.info(f'pars car {car['publicUrl']}')
                create_folder(self.config['folder_name']['CAR_DIR'])
                save(car['name_todo'], car, self.config['folder_name']['CAR_DIR'])
        except Exception as error:
            logger.error(error)
