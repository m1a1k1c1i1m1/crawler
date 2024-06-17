import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from Util.read_yaml import Read_yaml
from todo_av.create_todo import run
from time import sleep
con = Read_yaml()
config = con.conf()


if __name__ == '__main__':
    try:
        while True:
            run(config)
            sleep(30)
    except Exception as error:
        run(config)
