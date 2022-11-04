# -*- coding: utf-8 -*-


import os
import yaml

file_path = os.path.join(os.path.dirname(__file__), 'configdata.yaml')

with open(file_path) as file:
    message = yaml.safe_load(file)
# print(message)
