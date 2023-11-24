import loguru

import peckage

db = peckage.Base()
config = peckage.Setings()


class Update_car(peckage.Utils):

    def __init__(self):
        self.loop()

    def update_phone(self):
        car = db.get_all_car()
        list_url = list(map(lambda item: item['url_car'], car))
        todo_car = list(map(lambda item: config.json_phone(item.split('/')[-1], item), list_url))

    def loop(self):
        try:
            self.update_phone()
        except Exception as error:
            loguru.logger.info(error)

