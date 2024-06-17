import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from loguru import logger
from Util.util import create_folder, save


def run(config):
    create_folder(config['folder_name']['TODO_DIR'])
    save('todo_av', config['todo_cars'], config['folder_name']['TODO_DIR'])
    logger.info(f'create todo na av')
