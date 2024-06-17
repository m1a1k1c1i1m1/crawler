import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from crawler.crawler import Crawler
from Util.read_yaml import Read_yaml
from time import sleep


con = Read_yaml()
config = con.conf()


if __name__ == '__main__':
    try:
        while True:
            Crawler(config)
            sleep(60)
    except Exception as error:
        print(error)
        Crawler(config)
