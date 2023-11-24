import json
import os
from loguru import logger
import hashlib


class Utils:

    def create_todo(self, data, name_dir):
        if self.chek_dir(name_dir):
            self.seve_todo(data, name_dir)
            logger.info(f'todo create: {self.md_5(data["name_todo"])}')
        else:
            self.create_dir(name_dir)
            self.seve_todo(data, name_dir)
            logger.info(f'create todo: {self.md_5(data["name_todo"])}')

    def create_dir(self, name_dir):
        try:
            os.mkdir(name_dir)
            logger.info(f"Папка создана: {name_dir}")
        except Exception as error:
            logger.error(f'Папка с таким именем {name_dir} существует')

    def seve_response(self, data, name_dir):
        with open(f'{name_dir}{self.md_5(data["name"])}.json', 'w', encoding='utf-8') as File:
            json.dump(data, File, indent=4)

    def seve_todo(self, data, name_dir):
        with open(f'{name_dir}{self.md_5(data["name_todo"])}.json', 'w', encoding='utf-8') as File:
            json.dump(data, File, indent=4)

    def chek_dir(self, name_dir):
        if not os.path.exists(name_dir):
            return False
        else:
            return True

    def open_file(self, name_file, name_dir):
        with open(f'{name_dir}{name_file}', 'r') as File:
            file = json.loads(File.read())
            logger.info(f'открыт файл : {name_file} из папки {name_dir}')
            return file

    def delet_file(self, name_file, name_dir):
        os.remove(name_file)
        logger.info(f'файл удален: {name_file} из папки {name_dir} ')

    def md_5(self, str_hash):
        hash = hashlib.md5()
        hash.update(str_hash.encode('utf-8'))
        name = hash.hexdigest()
        return name

