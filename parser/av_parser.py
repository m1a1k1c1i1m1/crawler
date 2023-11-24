import os
import time
from datetime import datetime, timedelta
import peckage
from loguru import logger

config = peckage.Setings()
db = peckage.Base()


class Parser(peckage.Utils):

    def __init__(self):
        self.loop()

    def pars_phone(self, data):
        try:
            new_data = data['content'][0]
            cod_phone = new_data["country"]['code']
            number = new_data["number"]
            number_new = str(cod_phone) + str(number)
            if db.check_car(number, 'car'):
                db.update_phone(config.json_phone(data, number))
        except Exception as error:
            logger.info(error)

    def pars_all_car(self, data):
        items = data['adverts']
        car = list(map(lambda item: config.format_json(item), items))
        return car

    def flter_schow(self, data):
        items = data['adverts']
        car = []
        for item in items:
            time_publik = item['refreshedAt'].replace('T', ' ').replace('+', '.')
            date_time_obj = datetime.strptime(time_publik, '%Y-%m-%d %H:%M:%S.%f')
            if datetime.now() - date_time_obj > timedelta(minutes=5):
                logger.info(f'обьявление {item["publicUrl"]} нам не подходит')
            else:
                car.append(item)
        return car

    def pars_car(self, data):
        try:
            if data['page_all_flag'] == False:
                car = self.flter_schow(data['content'])
                self.json_car(car)
            else:
                cars = self.pars_all_car(data['content'])
                for item in cars:
                    self.create_todo(item, peckage.CAR_DIR)
                if peckage.body['page'] <= 50:
                    peckage.body['page'] += 1
                    self.create_todo(config.all_data_page(), peckage.TODO_DIR)
        except Exception as error:
            logger.error('возникла ошибка {} в функции pars_car'.format(error))

    def json_car(self, car):
        try:
            if len(car) != 0:
                map(lambda item:  self.create_todo(config.format_json(item), peckage.CAR_DIR), car)
        except Exception as error:
            print(error)
            logger.error(error)

    def loop(self):
        try:
            while True:
                list_file = os.listdir(peckage.PAGE_DIR)
                for item in list_file:
                    data = self.open_file(item, peckage.PAGE_DIR)
                    match data['type_page']:
                        case 'cars':
                            self.pars_car(data)
                        case 'phone':
                            self.pars_phone(data)
                    self.delet_file(peckage.PAGE_DIR + item, peckage.PAGE_DIR)
                if len(list_file) == 0:
                    time.sleep(10)
        except Exception as error:
            logger.error('возниклв ошибка: {} в функции loop'.format(error))


if __name__ == "__main__":
    pars = Parser()
