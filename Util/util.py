import json
import os
from loguru import logger
from time import sleep


def save(name: str, todo: dict, name_dir: str):
    with open(f'{name_dir}{name}.json', 'w') as file:
        json.dump(todo, file, indent=4)


def create_folder(name_folder: str):
    if not os.path.isdir(name_folder):
        os.mkdir(name_folder)
        logger.info(f'created folder: {name_folder}!!!')


def chek_key(key: str, data: dict) -> bool:
    for item in data:
        if not item == key:
            return False
        else:
            return True


def get_file(path: str):
    data = ''
    list_folder = os.listdir(path)
    if list_folder.__len__ != 0:
        for item in list_folder:
            with open(f'{path}{item}', 'r') as file:
                data = json.loads(file.read())
            os.remove(path + item)
        return data
    else:
        return 'not file'


def get_data_car(item: dict) -> dict:
    try:
        car = dict()
        new_car = item['properties']
        for items in new_car:
            key_name = items['name']
            value = items['value']
            if value != True:
                car.update({f'{key_name}': value})
        car.update({
            'usd': item['price']['usd']['amount'],
            'byn': item['price']['byn']['amount'],
            'locationName': item['locationName'],
            'sellerName': item['sellerName'],
            'refreshedAt': item['refreshedAt'],
            'publishedAt': item['publishedAt'],
            'publicUrl': item['publicUrl'],
            'name_todo': str(item['id'])
        })
        return car
    except Exception as error:
        logger.error(error)
