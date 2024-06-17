import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from parser.parser import Parser
from Util.read_yaml import Read_yaml
from time import sleep
from loguru import logger


con = Read_yaml()
config = con.conf()
pars = Parser(config)

if __name__ == '__main__':
    while True:
        try:
            data = pars.get_json_page()
            if data == '':
                sleep(10)
            else:
                pars.pars(data["adverts"])
                sleep(5)
        except Exception as error:
            logger.error(error)
            continue
