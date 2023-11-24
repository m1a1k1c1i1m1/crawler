import peckage

from time import sleep
import schedule

util = peckage.Utils()
peckage_conf = peckage.Setings()
db = peckage.Base()


class Main_todo:

    def __init__(self):
        self.loop()

    def page_doto(self):
        try:
            data = peckage_conf.first_page()
            util.create_todo(data, peckage.TODO_DIR)
        except Exception as error:
            print(error)

    def oll_todo_page(self):
        try:
            all_page = peckage_conf.all_data_page()
            util.create_todo(all_page, peckage.TODO_DIR)
        except Exception as error:
            print(error)

    def update_phone(self):
        car = db.get_all_car()
        list_url = list(map(lambda item: item['url_car'], car))
        todo_phone = list(map(lambda item: peckage_conf.todo_phone(item.split('/')[-1], item), list_url))
        list(map(lambda item: util.create_todo(item, peckage.TODO_DIR), todo_phone))

    def loop(self):
        #schedule.every().day.at("10:00").do(self.oll_todo_page)
        #schedule.every(2).seconds.do(self.main_doto)
        schedule.every(2).seconds.do(self.update_phone)
        while True:
            schedule.run_pending()
            sleep(1)


if __name__ == "__main__":
    Main_todo()
