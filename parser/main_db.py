import peckage
import os
from loguru import logger
from time import sleep
import json

util = peckage.Utils()

class Seve(peckage.Base):

    def __init__(self):
        self.run()

    def save_phone(self, data):
        if self.check_car(data[-1], 'car') == 1:
            id_car = self.get_id_car(data[-1], 'car')
            self.update_car(data, id_car)
        else:
            logger.info('нет такой записи : {} в базе данных'.format(data[-1]))

    def save_db(self, data):
        try:
            new_data = data
            if self.check(new_data['brand'], 'marka') == 0:
                self.insert_info_marka(new_data['brand'])
            else:
                logger.info('запись: {} в базе данных уже есть'.format(new_data['brand']))
            if self.check(new_data['model'], 'model') == 0:
                id_marka = self.get_id(new_data['brand'], 'marka')
                self.insert_info_model(new_data['model'], id_marka)
            else:
                logger.info('запись: {} в базе данных уже есть'.format(new_data['model']))
            if self.check_car(new_data['publicUrl'], 'car') == 0:
                self.insert_info_car(new_data)
            else:
                logger.info('запись: {} в базе данных уже есть'.format(new_data['publicUrl']))
        except Exception as error:
            logger.info('возникла ошбка: {} в функции save_db в файле main_save_in_db.py'.format(error))

    def run(self):
        try:
            while True:
                list_file = os.listdir(peckage.CAR_DIR)
                for item in list_file:
                        data = util.open_file(item, peckage.CAR_DIR)
                        self.save_db(data)
                        util.delet_file(peckage.CAR_DIR + item, peckage.CAR_DIR)
                if len(list_file) == 0:
                    sleep(10)
        except Exception as error:
            logger.info('возникла ошбка: {} в функции run в файле main_save_in_db.py'.format(error))


if __name__ == "__main__":
    save = Seve()
