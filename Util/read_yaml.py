import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import yaml


class Read_yaml:

    def conf(self):
        with open('D:/crawle_3.0/Util/config.yaml', 'r') as YamlFile:
            config = yaml.load(YamlFile, Loader=yaml.FullLoader)
            return config
